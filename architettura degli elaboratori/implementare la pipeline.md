---
sticker: lucide//align-vertical-distribute-center
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

