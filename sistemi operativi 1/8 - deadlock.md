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


