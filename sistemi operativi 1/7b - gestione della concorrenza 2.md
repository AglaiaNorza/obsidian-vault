## mutua esclusione: soluzioni software
Proviamo ora a gestire la mutua esclusione senza aiuto dal parte dell’hardware o dal Sistema Operativo. Tenteremo quindi di gestire tutto nel codice (senza la sicurezza di avere operazioni atomiche).

>[!tip] le soluzioni che vedremo valgono per 2 processi
>fare il passaggio a n processi è possibile ma non semplice
### tentativi
> [!summary] tentativo 1
> ![[me-tentativo-1.png|center|400]]
> 
> implementa la mutua esclusione MA
> - c'è busy-waiting
> - se ci fosse solo un processo, non funzionerebbe

> [!summary] tentativo 2
> ![[me-tentativo-2.png|center|400]]
> 
> uso un array per indicare se uno dei due processi è in sezione critica (P1 legge il valore di P2 e viceversa)
> - all'inizio sono tutti e due inizializzati a 0, quindi, se lo scheduler interrompesse P1 una volta entrato nel while ma prima che setti la variabile, anche P2 entrerebbe nella sezione critica (race condition)

> [!summary] tentativo 3
> ![[me-tentativo-3.png|center|400]]
> 
> si utilizza una flag per comunicare l'intenzione di entrare in una sezione critica
> - anche qui, se lo scheduler interrompe subito dopo l'impostazione della `flag`, i due processi rimangono bloccati nel while (deadlock)

> [!summary] tentativo 4
> ![[me-tentativo-4.png|center|400]]
> 
>si tenta di risolvere il problema del tentativo precedente modificando nuovamente la `flag` dentro il while, ma anche in questo caso non funziona sempre.
>può avvenire *livelock*: 
>![[livelock-es.png|200]]

### algoritmo 