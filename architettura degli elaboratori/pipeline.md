l'istruzione ha cinque fasi (con relative unità funzionali):
1) **instruction fetch** (IF) - memoria istruzioni e aggiornamento PC
2) **instruction decode** - blocco registri e CU
3) **execute** - ALU
4) **memory access** - memoria dati 
5) **write back** - banco registri

l'obiettivo è trasformare la CPU in una *catena di montaggio*, in cui ogni unità funzionale elabora la fase corrispondente e passa l'istruzione alla fase successiva.

![[pipeline catena di montaggio.png|center|400]]

##### esempio parallelizzazione
immaginiamo che la durata delle fasi sia la seguente:
- _Instruction Fetch_ → 200ps
- _Instruction Decode_ → 100ps
- _Instruction Execute_ → 200ps
- _Memory Access_ → 200ps
- _Write Back_ → 100ps
 
normalmente, per poter eseguire un'istruzione che richiede il completamento di tutte e 5 le fasi (come la `lw`), sarebbe necessario utilizzare un periodo di clock di 800ps
![[clock lento lw.png|center|350]]

invece, con la pipeline, il periodo può essere ridotto a quello della fase più lenta - 200ps
![[clock veloce lw.png|center|400]]

>[!Info] banco registri e periodo di clock
>poiché le fasi di `ID` e `WB`, che lavorano entrambe sul Register File, impiegano una quantità di tempo molto inferiore rispetto alle altre, se svolgo prima il `write` e poi il `read` posso, in *un'unica fase*, scrivere per l'istruzione precedente e leggere per l'istruzione corrente (anche il registro appena scritto)
>![[read e write stesso clock.png|center|300]]

#### criticità nell'esecuzione (hazard)
Con l'anticipazione delle istruzioni, possono nascere alcune criticità all'interno dell'architettura.
>[!Example]- esempio (exyss)
>Immaginiamo il caso in cui l’istruzione 1 modifichi il valore di un registro e l’istruzione 2 legga il valore di tale registro. Per via della suddivisione in fasi, durante la fase di ID dell’istruzione 2 non è ancora stata eseguita la fase di WB dell’istruzione 1, generando quindi una situazione critica in cui il dato del registro non sia ancora stato modificato. Di conseguenza, l’istruzione 2 leggerà il dato non ancora aggiornato. 

le criticità possono essere di diversi tipi:
- **structural hazard** - risorse hardware non sufficienti
- **data hazard** - il dato necessario non è ancora pronto
- **control hazard** - la presenza di un salto cambia il flusso di esecuzione delle istruzioni

>[!Example] esempio: data hazard
>immaginiamo di avere le due istruzioni:
>`addi $s0, $s1, 5` 
>`$sub $s2, $s0, $t0`
>si verificherà un *data hazard* sul registro `$s0`, il cui valore non sarà ancora stato scritto perché non sarà stato eseguito il Write Back.
>![[sub add data hazard.png|center|300]]
>per risolvere l'hazard, dobbiamo quindi alineare le fasi di `WB` e `ID`, introducendo due "*stalli*" nella pipeline:
>![[data hazard risolto con stalli.png|center|300]]
>chiarimento: ricordiamo che la scrittura sul Register File viene eseguita nella prima metà del periodo di clock, mentre la lettura nella seconda metà, dunque è sufficiente sovrapporre le due fasi affinché venga letto il dato corretto, senza la necessità di dover inserire un terzo stallo.

#### forwarding
in alcuni casi, l'informazione necessaria è già presente nella pipeline prima del `WB`  - in questo caso, possiamo aggiungere delle "*scorciatoie*", che recapiteranno il dato necessario senza dover aspettare la fase di `WB`.
>[!Example] continuando con un esempio come il precedente
>![[forwarding esempio.png|center|350]]
>in questo caso, visto che la seconda istruzione ha bisogno del registro `$s0` per effettuare la sottrazione, questo viene passato dal forwarding in avanti dopo la prima operazione
>![[forwarding es 2.png|center|300]]

Se la fase che ha bisogno del dato si trova prima di quella che lo produce, sarà comunque necessario inserire qualche stallo (o bolla) fino a quando esso non sarà generato.
>[!Example] esempio (exyss)\
>Nel seguente esempio, il dato aggiornato viene generato in fase di accesso alla memoria, dunque il dato rimarrà conservato nel banco di registri MEM/WB. Tuttavia, durante la fase di MEM viene svolta in contemporanea la fase di EXE dell’istruzione successiva, la quale necessiterebbe del dato aggiornato. Poiché il dato non può essere contemporaneamente generato e propagato tramite il forwarding, è necessario introdurre almeno uno stallo.
> 
>![[lw con stallo e fw.png|center|300]]
>![[lw con e senza forwarding.png|center|300]]