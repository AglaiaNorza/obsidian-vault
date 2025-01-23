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

## risorse
### risorse riusabili (reusable)
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
### risorse consumabili (consumable)
Le risorse consumabili vengono prodotte e distrutte consumate.
- esempi: interrupt, segnali, messaggi, informazioni nei buffer I/O

Il deadlock è possibile se si fa una richiesta bloccante di una risorsa ancora non creata.

>[!example] esempio 
>![[consumable-res-dl.png|center|350]]

#### condizioni per il deadlock
- **mutua esclusione** --> la risorsa va a chi riesce a fare richiesta per primo
- **hold-and-wait** --> richiesta di una risorsa quando non è stata ancora creata
- **niente preemption per le risorse** --> appena concessa, una risorsa viene distrutta
- **attesa circolare** --> una catena chiusa di processi, in cui ciascuno dovrebbe creare una risorsa richiesta dal processo che lo segue nella catena
#### grafo dell'allocazione delle risorse
è un grafo diretto che rappresenta lo stato di risorse e processi 
- ogni cerchio è un nodo
- ogni quadrato è un tipo di risorsa, ci sono tanti pallini quante istanze di una stessa risorsa

Per le risorse riusabili, esiste l'"held by", mentre per quelle consumabili i pallini compaiono e scompaiono.

![[grafo-allocazione-res.png|center|450]]

>[!example] esempio di grafo di attesa circolare
>![[attesa-circolare.png|center|400]]
>
>nella figura a:
>- mutua esclusione: sia `Ra` che `Rb` possono essere prese da un solo processo alla volta
>- hold-and-wait: `P1` richiede `Ra` e detiene `Rb` e viceversa
>- non c'è preemptionm, quindi il Sistema Operativo non può togliere le risorse ai processi
>  
> nella figura b non c'è invece deadlock o mutua esclusione - vengono allocate più istanze delle risorse necessarie

>[!example] esempio delle macchine all'incrocio
>![[macchine-deadlock.png|center|450]]
>![[deadlock-macchine-grafo.png|center|450]]
> - possiamo vedere che c'è un ciclo e nessun pallino è scoperto

## possibilità ed esistenza di deadlock
Il deadlock è *possibile* quando sono presenti:
- mutua esclusione
- hold-and-wait
- mancanza di preemption per le risorse

Ma un deadlock **è effettivamente presente** quando è verificata anche la quarta condizione:
- attesa circolare
## deadlock e SO
![[SO-che-fare.png|center|300]]

Il Sistema Operativo ha diverse tecniche per gestire il deadlock:
- **prevenire** --> cercare di far sì che una delle 4 condizioni sia sempre falsa
- **evitare** --> decidere di volta in volta cosa fare con l'assegnazione di risorse
- **rilevare** --> lasciare che ci sia deadlock, controllare ogni tanto se si è verificato, e prendere decisioni per rimuoverlo
- **ignorare** --> se processi utente vanno in deadlock, è colpa dell'utente (metodo non accettabile per processi del sistema operativo)

### prevenzione
Come prevenire le condizioni?
- *mutua esclusione* --> impossibile da prevenire
- *hold-and-wait* --> si impone a un processo di richiedere tutte le sue risorse in una volta
	- può essere difficile per software complessi
	- si tengono risorse bloccate per troppo tempo
- *mancanza di preemption* --> il Sistema Operativo può richiedere ad un processo di rilasciare le sue risorse (il processo poi le dovrà richiedere in seguito)
- *attesa circolare* --> ordinamento crescente delle risorse: una risorsa viene assegnata solo se segue quella che il processo detiene

### evitare
Il Sistema Operativo fa sì che il deadlock possa accadere, ma che il sistema si muova in modo che non capiti (decidendo volta per volta cosa fare per le risorse)
- in particolare, si cerca di evitare l'attesa circolare
 
Bisogna decidere se l'attuale richiesta di una risorsa, se esaudita, porterebbe ad un deadlock.
Ci sono due possibilità:
1) non mandare in esecuzione un processo se le sue richieste possono portare ad un deadlock 
2) non concedere una risorsa ad un processo se allocarla può portare a deadlock (*algoritmo del banchiere*)
#### algoritmo del banchiere
>[!warning] è valido solo per le risorse riutilizzabili, e non per quelle consumabili

Il sistema ha uno **stato** (attuale allocazione delle risorse dei processi) :
- uno stato è *safe* se da esso parte almeno un cammino che non porta al deadlock
- uno stato è *unsafe* altrimenti
##### strutture dati
![[algo-banchiere.png|center|400]]

- $m$ --> numero di tipi di risorse diverse (es. stampante, mouse, tastiera...)
- $R_{i}$ --> numero di istanze dell'i-esima risorsa
- $V_{i}$ --> numero di istanze disponibili (non allocate) dell'i-esima risorsa
- $C_{ij}$ --> matrice composta da:
	- $m$ colonne, una per tipo di risorsa
	- $n$ righe, una per ogni processo che sto monitorando
	- ogni valore si legge come: il processo $i$-esimo, prima o poi chiederà massimo $x$ (valore) istanze della risorsa $j$-esima
- $A_{ij}$ --> ha la stessa struttura della matrice $C$, e contiene il numero di allocazioni correnti di ogni tipo di risorsa per ogni processo
- esiste anche un vettore `request`, che contiene il tipo di richiesta che viene fatta (ha $m$ elementi, e ogni valore corrisponde al numero di istanze di un tipo di risorsa chiesta dal processo)

##### determinazione dello stato sicuro
![[stato-sicuro.png|center|450]]

Voglio monitorare quattro processi, ci sono 3 tipi di risorse (le cui istanze sono descritte nei vettori $R$ e $V$).
- <small>chiaramente si può fare un sanity check iniziale: ogni riga di $C$ (ogni elemento) deve essere $\leq$ del vettore $R$ (altrimenti il processo non può fisicamente essere eseguito)</small>

Verifichiamo il cammino che non porta al deadlock:
- supponiamo di far eseguire `P2` fino alla fine - gli manca infatti un'istanza di $R_{3}$, che è disponibile (non avremmo potuto scegliere per esempio `P1`, perché ha bisogno di 2 istanze di $R_{1}$, che non sono disponibili)
 
![[stato-sicuro2.png|center|450]]

- le risorse utilizzate da `P2`, a fine esecuzione, tornano disponibili - possiamo quindi portare gli altri processi a completamento

Facciamo quindi eseguire `P1` fino al completamento

![[stato-sicuro-3.png|center|450]]

... e anche `P3`:

![[stato-sicuro-4.png|center|450]]

- poi `P4`, e abbiamo finito

Abbiamo quindi trovato un cammino che non porta a deadlock - lo stato è sicuro.
##### determinazione dello stato non sicuro
La situazione di partenza è la stessa.
Partiamo da questo stato (sicuro).

![[stato-unsafe-1.png|center|450]]

Supponiamo che l'algoritmo del banchiere non venga usato o venga usato male, e che ci porti a questa situazione:
- `P1` ha ricevuto un'unità di $R_{1}$ e una di $R_{3}$

![[stato-unsafe-2.png|center|450]]

Questo è uno stato non sicuro - nessuno dei processi può essere selezionato per andare in esecuzione (non ci sono le risorse per nessun processo).

#### implementazione algo banchiere

**strutture dati**:
```C
struct state {
	int resource[m];  // R
	int available[m]; // V
	int claim[n][m];  // C
	int alloc[n][m];  // A
}
```
- sono gli array e matrici di prima

**algoritmo**:
```C
if(alloc[i,*]+request[*] > claim[i,*]) 
	<error>;                           // total request > claim
else if(request[*] > available[*])
	<suspend process>;
else {
	<define newstate by:
	alloc[i,*] = alloc[i,*] + request[*];
	available[*] = available[*] - request[*]>;
}
if(safe(newstate)) {
	<carry out allocation>;
} else {
	<restore original state>;
	<suspend process>;
}

boolean safe(state S) {
	int currentavail[m];
	process rest[<number of processes>];
	currentavail = available;
	rest = {all processes};
	possibile = true;
	while(possible) {
		<find a process Pk in rest such that
		claim[k, *]-alloc[k, *] <= currentavail;>
		if(found) {
			currentavail = currentavail+alloc[k,*];
			rest = rest - {Pk}
		} else possible = false;
	}
	return (rest == null)
}
```

**walkthrough**:
Mi serve per verificare se posso concedere una risorsa oppure no.

>[!important] l’algoritmo del banchiere è implementato nel SO, e viene quindi eseguito in kernel mode
>è per questo che l’algoritmo può bloccare i processi quando una richiesta non si può soddisfare

- inizia con un safety check - con `(alloc[i,*]+request[*] > claim[i,*])` controllo che i processi non richiedano più risorse di quante sono disponibili (basta una elemento solo perché non vada bene)
- se non ci sono abbastanza risorse disponibili per una richiesta, il processo viene sospeso (in attesa che un altro liberi le risorse)
- se invece le risorse ci sono, si fa una simulazione di cosa succederebbe se si concedessero le richieste - si definisce un nuovo stato, e, 
	- se è safe, si allocano le risorse. 
	- altrimenti, si sospende il processo.

La safeness si controlla con la funzione `safe`
- si considerano tutti i processi, e si vede se almeno uno può essere eseguito fino alla fine
- si fa varie volte, e, se si arriva a far eseguire tutti i processi, lo stato è safe

>[!tip] requisiti perché funzioni
>Perché l'algoritmo funzioni, i processi devono essere indipendenti, ovvero "liberi" di andare in esecuzione in qualsiasi ordine
>- per esempio, non si possono mandare messaggi

### rilevare
Per rilevare il deadlock si possono usare le stesse strutture dati dell'algoritmo del banchiere, ma la $\text{claim matrix}$ è sostituita da $Q$, ovvero le richieste effettuate da tutti i processi.

#### algoritmo 
1) marca tutti i processi che non hanno allocato nulla (processi che non causano problemi)
2) $w \leftarrow V$ (inizializzo un vettore $w$ con l'attuale vettore delle risorse disponibili)
3) cerco un processo $i$ che non sia marcato t.c. $Q_{ik}\leq w_{k}$ (la sua riga è $<w$, quindi gli si possono concedere le risorse)
	- in questo caso, quindi il processo può non creare deadlock
4) se $i$ non esiste, vai al passo 6
5) (se invece $i$ esiste), marcalo, aggiorna $w \leftarrow w+A_{i}$ (faccio finta che il processo vada fino alla fine e rilasci quello che aveva allocato) e torna al passo 3 
6) c'è deadlock se esiste un processo non marcato (sono uscito o perché erano finiti i processi - ok, li ho marcati tutti -, o perché ne ho trovato uno che causa deadlock)

>[!example] esempio 
>![[rilevare-deadlock-es.png|center|350]]

#### (deadlock trovato) e poi?
Una volta trovato un deadlock, ci sono diverse opzioni:
- **terminare forzatamente tutti i processi** coinvolti nel deadlock (soluzione comune)
- **mantenere punti di ripristino** ed effettuare il ripristino al punto precedente (lo stallo può verificarsi nuovamente, ma è improbabile che succeda all'infinito)
- **terminare forzatamente uno ad uno i processi** coinvolti, finché lo stallo non c'è più
- **sottrarre forzatamente risorse** ai processi coinvolti nel deadlock uno ad uno, finché lo stallo non c'è più

### vantaggi e svantaggi soluzioni
 
> [!tip] vantaggi/svantaggi
> ![[deadlock-sol.png|center|500]]

## deadlock e linux
Linux implementa una gestione minmale ma il più efficiente possibile.
Se dei processi utenti sono "scritti male" e vanno in deadlock, peggio per loro (letteralmente).
- saranno tutti bloccati `TASK_INTERRUPTIBLE`
- sta all'utente accorgersene e killarli - sono solo processi utente, non fanno molto danno

Per quanto riguarda il kernel, c'è la *prevenzione dell'attesa circolare*.

## quattro filosofi a cena
![[filosofi-cena.png|center|250]]

Ad un tavolo ci sono uno stesso numero di forchette, piatti e sedie per un egual numero di filosofi.
Il problema è che per mangiare, ogni filosofo ha bisogno di due forchette. Ogni filosofo può solamente prendere le forchette accanto al suo piatto (a destra e a sinistra).
Una volta finito di mangiare, ripone le forchette e torna a pensare (as they do).

Il problema e che due filosofi seduti vicini non possono mangiare contemporaneamente.

### prima "soluzione" (genera deadlock)
```C
semaphore fork[5] = {1};

void philosopher(int i) {
	while(true) {
		think();
		wait(fork[i]);
		wait(fork[(i+1)%5]);
		eat();
		signal(fork[(i+1)%5]);
		signal(fork[i]);
	}
}

void main() {
	parbegin(philosopher[0], philosopher[1], philosopher[2], philosopher[3], philosopher[4])
}
```
- ci sono `n` semafori (con `n` numero di filosofi), tutti inizializzati a `1`.
- il filosofo `i`-esimo avrà bisogno della forchetta `i`-esima e di quella `i+1%n`-esima
- i filosofi pensano - `think` operazione locale, la possono fare senza problemi
- un filosofo prova a prendere la forchetta di sx - `wait(fork[i])` - e, se qualcuno l'ha già presa, si blocca e poi stessa cosa per quella di destra `wait(fork[(i+1)%5])`

Ci può essere deadlock: può succedere che lo scheduler lasci fare a tutti i filosofi la `wait` sulla forchetta sinistra (senza problemi) - poi, tutti cercheranno di prendere quella di destra, e rimarranno bloccati (non ci sono più forchette)

### seconda soluzione (cambio premesse)
```C
semaphore fork[5] = {1};
semaphore room = {4}

void philosopher(int i) {
	while(true) {
		think();
		wait(room)
		wait(fork[i]);
		wait(fork[(i+1)%5]);
		eat();
		signal(fork[(i+1)%5]);
		signal(fork[i]);
		signal(room)
	}
}

void main() {
	parbegin(philosopher[0], philosopher[1], philosopher[2], philosopher[3], philosopher[4])
}
```
- visto che prima il problema era che tutti gli `n` filosofi volevano mangiare, ora risolviamo in modo diverso <small>(bariamo un po')</small>
- invece di avere tutti i filosofi seduti, facciamo finta che ci sia un cameriere che fa entrare a mangiare al massimo `n-1` filosofi
- non c'è più deadlock (c'è sempre un filosofo che riesce a mangiare)

### terza soluzione: semafori (senza cambiare premesse)
Si torna al canone: non cambiamo i termini del problema.

```C
semaphore fork[N] = {1, 1, ..., 1};

philosopher(int me) {
	int left, right, first, second;
	left = me;
	right = (me+1)%N;
	first = right < left ? right : left;
	second = right < left ? left : right;
	
	while(true) {
		think();
		wait(fork[first]);
		wait(fork[second]);
		eat();
		signal(fork[first]);
		signal(fork[second]);
	}
}
```

Questa soluzione funziona perché:
- mentre prima si prendeva sempre la forchetta di sinistra e poi quella di destra, qui si fa in modo che l'*ultimo processo si comporti al contrario* (prenderà prima la dx e poi la sx)
	- l'operatore ternario funziona perché, per l'ultimo processo, `(me+1)%n` sarà `0`
- questo basta a rompere il ciclo vizioso: se anche si presentasse la situazione di prima, l'ultimo si bloccherebbe cercando di prendere la forchetta di destra, già occupata (e quindi lascerebbe libera la sua sinistra)

### quarta "soluzione": messaggi (sbagliata e corretta)
- possiamo implementare la prima "soluzione" anche con i semafori, ma continuerà a non funzionare (i filosofi vanno tutti prima a sinistra e poi a destra)

La versione corretta è invece l'analoga dii quella appena vista (terza soluzione), ma con i messaggi.

```C
mailbox fork[N];

// rendo tutte le forchette prendibili
init_forks() {
	int i;
	for(i=0; i<N; i++) {
		nbsend(fork[i], "fork");
	}
}

philosopher(int me) {
	int left, right;
	message fork1, fork2;
	left = me;
	right = (me+1)%N;
	first = right < left ? right : left;
	second = right < left ? left : right;
	
	while(true) {
		think_for_a_while();
		receive(fork[first], fork1);
		receive(fork[second], fork2);
		eat();
		nbsend(fork[first], fork1);
		nbsend(fork[second], fork2)
	}
}
```

### quinta soluzione (corretta, ma possibile livelock)
```C
philosopher(int me) {
	int left, right;
	message fork1, fork2;
	left = me;
	right = (me+1)%N;
	
	while(true) {
		think_for_a_while();
		// receive non bloccanti
		if(nbreceive(fork[left], fork1)) {
			if(nbreceive(fork[right], fork2)) {
				eat();
				nbsend(fork[right], fork1);
			}
		nbsend(fork[left], fork2)
		}
	}
}
```

Mantengo la scelta di andare prima a sinistra e poi a destra, ma uso i messaggi per usare un "trucco" che non posso mettere in atto con i semafori:
- uso la `receive` non bloccante - provo a vedere se posso prendere una forchetta, e se non ci riesco, smetto di provarci
- se posso ricevere la prima, vado avanti e cerco di ricevere anche la seconda - altrimenti, smetto di provare a mangiare

>[!warning] attenzione: livelock
>Questa soluzione può però causare **livelock**: infatti, se tutti i processi prendono la forchetta sinistra, ma vengono bloccati e non possono prendere quella di destra, entrano in un circolo vizioso in cui prendono e rilasciano la forchetta sinistra senza mai prendere quella di destra.
> 
>Tuttavia, accettiamo questa soluzione perché i filosofi pensano per un tempo casuale, non correlato a quello degli altri (ed è quindi improbabile che questa soluzione si presenti davvero).