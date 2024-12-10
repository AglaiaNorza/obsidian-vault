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

### algoritmo di Dekker
![[dekker-algo.png|center|550]]

Qui fin dall’inizio dichiaro di voler entrare nella sezione critica. Se il `wants_to_enter` dell’altro processo è `false` entro nella sezione critica. Nel caso in cui invece il valore è `true`, si ha una variabile `turn` condivisa. Per il `P0` se `turn` è `0` (non tocca a me), rimetto a falso il fatto che voglio entrare e faccio un’attesa attiva finché il `turn` è `1`. Una volta finita l’attesa reimposto il fatto che voglio entrare a `true`.
- se il dispatcher è fair, funziona
- garantisce il **bounded-waiting** - un processo può aspettarne un altro al massimo una volta
- non c'è deadlock, ma c'è busy-waiting
- non richiede nessun supporto dal Sistema Operativo (bisogna disattivare le ottimizzazioni dei sistemi operativi moderni)
- vale solo per 2 processi - l'estensione a N è possibile ma non banale

### algoritmo di Peterson
![[peterson-algo.png|center|350]]

Il processo "fa passare" l’altro processo - si entra nel `while` solamente se è il turno dell’altro processo e si vuole entrare (non si hanno problemi se in esecuzione si ha un solo processo). Anche qui, facendo un interleaving perfetto, non si avrebbero problemi in quanto viene mandato in esecuzione il penultimo processo che ha impostato `turn`

- ha le stesse caratteristiche dell'algoritmo di dekker
## passaggio di messaggi
Quando un processo interagisce con un altro, devono essere soddisfatti due requisiti fondamentali:
- **sincronizzazione** (mutua esclusione)
- **comunicazione**

Il *message passing* è una soluzione al secondo requisito, e:
- funziona sia con memoria condivisa che distribuita
- può essere usata anche per la sincronizzazione

Funziona con due primitive:
- `send(destination, message)` - qui `message` è il messaggio da mandare`
- `receive(source, message)` - qui `message` è la zona di memoria in cui vogliamo ricetvere il messaggio
- + a volte, il test di ricezione

>[!tip] send e receive sono sempre atomiche
>

- possono essere bloccanti oppure no (mentre il test di ricezione è sempre bloccante)



