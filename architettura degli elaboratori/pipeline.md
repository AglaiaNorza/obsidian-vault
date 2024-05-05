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
Immaginiamo il caso in cui l’istruzione 1 modifichi il valore di un registro e l’istruzione
2 legga il valore di tale registro. Per via della suddivisione in fasi, durante la fase di
ID dell’istruzione 2 non è ancora stata eseguita la fase di WB dell’istruzione 1,
generando quindi una situazione critica in cui il dato del registro non sia ancora stato
modificato. Di conseguenza, l’istruzione 2 leggerà il dato non ancora aggiornato. (exyss)