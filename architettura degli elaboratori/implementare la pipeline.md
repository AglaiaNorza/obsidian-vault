---
created: 2024-09-12T14:48
updated: 2025-04-16T17:12
---

per poter implementare la pipeline all'interno di una CPU MIPS, per permettere il **forwarding** è necessario inserire dei registri tra le unità funzionali, per poterci inserire dati e utilizzarli quando necessari.
![[registri pipeline.jpg|center|400]]
 
>[!Example] esempio:
>![[esempio codice forwarding.jpg|center|500]]
>qui il problema si genera perché la `sw` effettua l'instruction fetch prima che la `lw` scriva su `$t4` - quindi, nel banco registri, c'è il registro `$t6` pronto ad essere scritto (e non `$t4`)
>![[esempio pipeline fw fasi.jpg|center|300]]
>per questo, tutte le informazioni ed i segnali di controllo devono trovarsi nel registro precedente della pipeline (e non dove sarebbero normalmente)
>![[fw info nel registro giusto.png|center|400]]

##### logica dei salti
aggiungendo la logica dei `beq` si spostano tutti i controlli (tranne `RegWrite`, che però viene attivato solo durante il Write Back) dopo l'Instruction Decode così da non avere la necessità di effettuare controlli solo durante le ultime tre fasi dell'istruzione .
![[pipeline con logica di salti.png|center|500]]
si noti che ora serve il campo `funz` (codice funzione) di 6 bit, che esce dal registro ID/EX e viene utilizzato come segnale di controllo della ALU.

##### segnali di controllo Control Unit
si possono quindi dividere i segnali di controllo in 3 gruppi:
- *fase EXE*
- *fase MEM*
- *fase WB*
 
![[fasi segnali CU pipeline.png|500]]

e i segnali si propagano all'interno della CPU
 
![[propagazione segnali cpu.png|300]]

>[!Tip] CPU completa con segnali di controllo
>![[cpu con segnali pipelne.png|center|550]]

---
### scoprire un data hazard in EXE
immaginiamo questo codice:
![[data hazard in exe.png|center|500]]
- in questo esempio, visto che il risultato del `sub` viene scritto in `$s2` solo nella fase di WB della prima istruzione, le istruzioni `and` e `or` leggeranno il valore sbagliato.
- è facile però notare che il risultato della sottrazione sia già disponibile alla fine della fase EX
- anche `and` e `or` hanno bisogno del dato all'inizio della fase EX, quindi è possibile evitare stalli *propagando* il dato alle unità che lo richiedono non appena sia disponibile

possiamo quindi notare che le casistiche che portano a un data hazard in EXE sono:

> [!Important]  casistiche
> 1. $\text{EX/MEM.RegistroRd}=\text{ID/EX.RegistroRs}$
> 2. $\text{EX/MEM.RegistroRd}=\text{ID/EX.RegistroRt}$
> 3. $\text{MEM/WB.RegistroRd}=\text{ID/EX.RegistroRs}$
> 4. $\text{MEM/WB.RegistroRd}=\text{ID/EX.RegistroRt}$

(la casistica dell'esempio è del primo tipo -  `EX/MEM.RegistroRd = ID/EX.RegistroRs = $s2`)

ma, dato che non tutte le istruzioni scrivono il risultato nel register file, questa strategia non basta e potrebbero esserci casi in cui viene propagato un dato non necessario.
- una possibile soluzione sarebbe controllare se il segnale `RegWrite` è attivo nella sezione `EX/MEM` e `MEM/WB`
- in più, dobbiamo controllare che il registro di destinazione non sia `$s0`, perché l'architettura MIPS impedisce di scriverci.
- si aggiunge anche `MemRead == 0` perché, nel caso di istruzioni di tipo i, alcuni dei bit della parte immediata potrebbero essere interpretati come un registro e potrebbero risultare uguali a i registri usati in operazioni precedenti

>[!Important] quindi, si ha un data hazard in EXE se:
>![[segnali hazard in EXE.png]]

quindi, il forwarding in EXE si implementa così:
![[forwarding in exe.png|center|500]]
>[!info] cosa fa? 
>consiste nel *sostituire* il valore letto dal blocco dei registri con quello prodotto dall'istruzione precedente (in fase EXE) o quella prima ancora (in fase MEM)
- **modifiche al datapath**: inserire un MUX prima della ALU per selezionare tra i tre casi:
	1) *non c'è forwarding* - il valore per la ALU viene letto dal registro `ID/EXE` della pipeline
	2) *forwarding dall'istruzione precedente* - il valore per la ALU viene letto dal registro `EX/MEM` della pipeline
	3) *forwarding da due istruzioni prima* - il valore per la ALU viene letto dal registro `MEM/WB` della ALU
 
questo vale sia per il primo che per il secondo argomento della ALU (infatti sono presenti 2 MUX)

i segnali di controllo sono i seguenti:
![[segnali di controllo fw exe.jpeg]]

### scoprire data hazard in MEM
si ha un data hazard in MEM quando vengono fatti in sequenza un `lw` e uno `sw` con lo stesso registro `$rt` (creando quindi una sorta di swap di valori in memoria)
 
![[fw mem.png]]

è possibile rilevarlo se: 
![[segnali hazard mem.png]]

>[!info] CPU con forwarding MEM
![[cpu fw mem.jpeg]]

### stallo dell'istruzione
a volte l'istruzione deve **attendere che sia pronto il dato** prima di poter effettuare il forwarding.

![[stallo con fw.jpeg]]

poiché il risultato della `lw` non è disponibile prima della fase MEM, bisognerà aggiungere uno stallo.

per fermare l'istruzione con uno stallo dobbiamo (nella fase ID):
- annullare l'istruzione che deve attendere (**bolla**)
	- *azzerare i segnali di controllo* `MemWrite` e `RegWrite` e `IF/ID.Istruzione` - rendendo l'istruzione una NOP 
- **rileggere** la stessa istruzione affinché possa essere eseguita un ciclo di clock dopo:
	- *impedire che il PC si aggiorni*
 
>[!Example] stallo in azione
>![[stallo esempio.jpeg]]

---
quindi, la CPU in questo momento si presenterà così

>[!Tip] CPU quasi completa
>![[CPU quasi completa pipeline.jpeg]]

---
### anticipare il jump
la decisione di eseguire il Jump viene presa dalla Control Unit nella fase ID - nel frattempo, un'altra istruzione è stata caricata ed occorre che si annulli.

ma è possibile *anticipare il jump alla fase IF*.
per farlo, occorre:
- anticipare il riconoscimento dell'istruzione (che di solito avviene nella fase ID) con un **comparatore con il valore dell'Opcode della j** (000010)
- **spostare** la logica di aggiornamento del PC alla fase IF

così, la jump anticipata non introduce stalli 
 
![[jump anticipata.jpeg|center|250]]

##### control hazard
l'istruzione `beq` usa la ALU per fare il confronto tra i registri, per cui:
- il salto avviene dopo la fase EXE (nella fase MEM) ⟶ in caso di salto, le istruzioni seguenti già caricate vanno annullate
- necessita degli argomenti nella fase EXE ⟶ può aver bisogno di uno stallo se preceduta da una `lw`

per **anticipare la decisione di salto** alla fase ID, occorre *non usare la ALU*
- inserendo un *comparatore* tra i due argomenti letti dal blocco registri
- spostando la logica di salto e il calcolo del salto relativo dalla fase EXE alla *fase ID*
- inserendo un'*unità di forwarding* apposita per la fase ID
 
>[!info] CPU con branch anticipato
>![[branch anticipato a id.jpeg|center|500]]

il flush identifica il branch, e "scarica" la pipeline di IF/ID (rendendo l'operazione successiva una nop)
 
![[flush pipeline.jpg|center|400]]

ma l'abbassamento del numero di stalli (da 2 a 1) in caso di predizione sbagliata non è gratuito: infatti, la fase in cui `bneq` e `beq` necessitano dei dati viene anticipata da EXE ad ID

??? chiedi ???

---
### cpu "finale" con pipeline
![[cpu con pipeline.jpeg]]

---
### salto ritardato
la tecnica del salto ritardato consiste nell'inserimento di una o più istruzioni che verrebbero eseguite in entrambi i casi (salto o non salto) per evitare di dover inserire salti dopo un branch.





