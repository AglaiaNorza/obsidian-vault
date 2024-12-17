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
- *attesa circolare*

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
- uno stato è *safe* se da esso parte almeno un cammino che non parte al deadlock
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

Mi serve per verificare se posso concedere una risorsa oppure no.

>[!important] l’algoritmo del banchiere è implementato nel SO, e viene quindi eseguito in kernel mode
>è per questo che l’algoritmo può bloccare i processi quando una richiesta non si può soddisfare

- inizia con un safety check - con `(alloc[i,*]+request[*] > claim[i,*])` controllo che i processi non richiedano più risorse di quante sono disponibili (basta una elemento solo perché non vada bene)
- se non ci sono abbastanza risorse disponibili per una richiesta, il processo viene sospeso (in attesa che un altro liberi )

