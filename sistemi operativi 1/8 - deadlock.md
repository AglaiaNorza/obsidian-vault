Il deadlock è un *blocco permanente* di un insieme di processi, che competono per le risorse o comunicano tra loro.
- il motivo di base è la **richiesta contemporanea delle stesse risorse** da parte di due o più processi.

Non esiste un'unica soluzione efficiente: bisogna valutare i diversi casi.
- il deadlock potrebbe essere anche causato da una combinazione rara di eventi (corner case), ma va prevenuto in ogni caso.

>[!example] esempio 
>![[deadlock-es.png|center|350]]

## joint progress diagram

> [!example] esempio 1
> - le righe sono le possibili esecuzioni dei processi
> - l'x-axis rappresenta il progresso di `P`, il y-axis quello di `Q`
>  
> ![[jpr-diag-1.png|center|500]]
> 
> qui è importante notare che:
> - `P` e `Q` richiedono le stesse risorse (`A` e `B`), ma in ordine opposto
> - entrambi richiedono la nuova risorsa prima di rilasciare quella vecchia
> 
> Quindi il deadlock è inevitabile nel momento in cui un processo detiene una risorsa e vuole l'altra, ma questa è detenuta dall'altro processo (che a sua volta vuole la risorsa del primo) (3 e 4)

>[!example] esempio 2
>![[jpr-diag-2.png|center|500]]
>Qui invece non può esserci deadlock.
>- in questo caso, `P` è molto più "generoso" di prima e non ha bisogno di due risorse contemporaneamente

## risorse: reusable e consumable
### risorse riusabili
Le risorse riusabili sono utilizzabili da *un solo processo alla volta*, e **l'essere usate non le consuma**.
- una volta che un processo ottiene una risorsa riusabile, prima o poi la rilascerà così che altri processi la possano usare.
- esempi: processori, I/O channel, RAM, memoria secondaria, dispositivi, file, database, semafori...

Lo stallo può esistere solo se un processo ha una risorsa e ne richiede un'altra.

> [!example] esempio
> ![[reusable-res.png|center|350]]
> 
> (la sezione critica è `perform function`)
> - si bloccano perché `P` richiede `T` prima di rilasciare `D`, e `Q` richiede `D` prima di rilasciare `T`.

>[!example] esempio 2
>supponiamo di avere 200KB di memoria disponibili:
>
>![[resusable-res-2.png|center|350]]
>- il deadlock avverrà quando uno dei due processi farà la seconda richiesta

#### condizioni per il deadlock
Il deadlock si verifica solo se ci sono queste quattro condizioni:
1) **mutua esclusione** --> solo un processo alla volta può usare una risorsa
2) **hold-and-wait** --> richiesta di una risorsa quando se ne ha già una
3) **niente preemption per le risorse** --> non si può sottrarre una risorsa ad un processo prima che questo la rilasci
4) **attesa circolare** --> esiste una catena chiusa di procesi, in cui ciascun processo detiene una risorsa richiesta dal processo che lo segue nella catena

### risorse consumabili
Le risorse consumabili vengono prodotte e distrutte consumate.
- esempi: interrupt, segnali, messaggi, informazioni nei buffer I/O

Il deadlock è possibile se si fa una richiesta bloccante di una risorsa ancora non creata.

>[!example] esempio 
>![[consumable-res-dl.png|center|350]]