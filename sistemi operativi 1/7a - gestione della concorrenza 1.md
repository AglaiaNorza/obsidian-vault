---
{}
---
## concetti base di concorrenza
Per i Sistemi Operativi moderni, è essenziale supportare più processi in esecuzione attraverso:
- multiprogrammazione
- multiprocessing
- computazione distribuita (cluster)

Un grosso problema da affrontare è quello della **concorrenza**: come questi processi interagiscono.
### multiprogrammazione
Se c'è un solo processore, i processi si alternano nel suo uso (*interleaving*)

![[interleaving.png|center|400]]

### multiprocessing
Se c'è più di un processore, i processi si alternano nell'uso di un processore (sempre interleaving) e possono sovrapporsi nell'uso dei vari processori (*overlapping*).

![[inter-overlapping.png|center|400]]

### concorrenza
La concorrenza si manifesta nelle seguenti occasioni:
- applicazioni multiple --> condividono il tempo di calcolo
- applicazioni strutturate per essere parallele --> perché generano altri processi o perché sono organizzate in thread
- struttura del sistema operativo --> gli stessi Sistemi Operativi sono costituiti da svariati processi o thread in esecuzione parallela
### terminologia
- **operazione atomica** --> una sequenza *indivisibile* di comandi -  <small>il dispatcher non può interrompere queste operazioni fino alla loro terminazione (nessun altro processo può vedere uno stato intermedio o interrompere la sequenza)</small>
- **sezione critica** --> parte del codice di un processo in cui c'è un *accesso esclusivo ad una risorsa condivisa* - nessun altro processo che voglia accedere in modo esclusivo alla stessa risorsa può farlo
- **mutua esclusione** --> requisito che impone che *un solo processo sia in una data sezione critica* (avviene quando due processi cercano di accedere ad una risorsa condivisa fatta per un processo solo alla volta)
- **corsa critica** (*race condition*) --> violazione della mutua esclusione 
- **stallo** (*deadlock*) --> due o più processi non possono procedere con la prossima istruzione perché si attendono a vicenda
- **stallo attivo** (*livelock*) --> due o più processi cambiano continuamente il proprio stato, l'uno in risposta all'altro, senza fare nulla di utile
- **starvation** --> un processo, pur essendo ready, non viene scelto dallo scheduler
### difficoltà
La difficoltà principale, quando si parla di concorrenza, è che non is può fare **nessuna assunzione sul comportamento dei processi**, e neanche su come funzionerà lo scheduler.

Un altro problema è quello della **condivisione delle risorse**, che si presenta quando due processi cercano di accedere alla stessa risorsa.

C'è anche il problema dell'**allocazione delle risorse condivise** (decidere se dare o no una risorsa condivisa ad un processo) - la concorrenza fa sì che non esista una gestione ottimale del carico - per esempio, un processo potrebbere richiedere I/O e poi essere rimesso in ready prima di usarlo: l'I/O va considerato libero e utilizzabile dagli altri processi, o ancora locked?

Infine, si pone il problema della **difficoltà nel tracciare gli errori di programmazione**. Infatti, spesso il manifestarsi di un errore dipende dallo scheduler e dagli altri processi presenti (e ri-runnare l'ultimo processo non darebbe lo stesso errore)

### esempio facile
``` C
/* chin e chout globali */
void echo()
{
	chin = getchar();
	chout = chin;
	putchar(chout);
}
```

Su **un processore**:
supponiamo che ci siano due processi che tentano di eseguire la stesa procedura su un processore:
```C
Process P1                    Process P2
    .                             .
chin = getchar();                 .
		.        -->        chin = getchar(); /* qui chin riassegnato */
chout = chin;                     .
	.                         chout = chin;
putchar(chout);                   .
	.                         putchar(chout);
	.                             .
```
In questo caso, avremo in output lo stesso carattere, nonostante ai due processi siano stati dati due input diversi.

Su **più processori**:
non necessariamente l'uso di più processori risolverebbe il problema
```c
Process P1                    Process P2
    .                             .
chin = getchar();                 .
	.                         chin = getchar();
chout = chin;                 chout = chin;
putchar(chout);                   .
	.                         putchar(chout);
	.                             .
```
anche in questo caso avremmo infatti lo stesso problema.
### restrizione all'accesso singolo
Risolvere il problema dell'esempio precedente risulta particolarmente facile. La soluzione, infatti, sta nel permettere l'esecuzione della funzione `echo` ad un solo processo alla volta --> *rendere atomica una funzione*.

<small> quindi, andrebbe così</small>
- P1 entra per primo
- P2 ci prova, ma viene bloccato finché P1 non finisce
- a quel punto, P2 viene resumato e può essere completato
### race condition
Si ha una race condition quando:
- più processi o thread leggono e scrivono sulla stessa risorsa condivisa, in modo tale che lo stato finale della risorsa dipende dal loro ordine di esecuzione

La parte di codice che può portare ad una race condition si chiama **sezione critica**.
### per il Sistema Operativo 
I problemi di progetto e gestione legati alla concorrenza, per il Sistema Operativo, sorgono dal fatto che esso deve:
- tener traccia dei vari processi
- allocare e deallocare risorse 
- proteggere dati e risorse dall'interferenza non autorizzata di altri processi
- assicurare che processi e output siano *indipendenti dalla velocità di computazione* (dallo scheduling)
### interazione tra processi

| Relazione    | Comunicazione                                                                      | Influenza                                                                                                                     | Problemi di controllo                                     |
| ------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Competizione | Nessuna (ogni processo pensa di essere solo)                                       | Risultato di un processo è indipendente dagli altri. Tempo di esecuzione di un processo dipende dagli altri                   | Mutua esclusione; deadlock; starvation                    |
| Cooperazione | Memoria condivisa (i processi sanno che c’è qualche altro processo)                | Risultato di un processo dipende dall’informazione data da altri. Tempo di esecuzione di un processo dipende dagli altri      | Mutua esclusione; deadlock; starvation; coerenza dei dati |
| Cooperazione | Primitive di comunicazione (i processi sanno anche i PID di alcuni altri processi) | Risultato di un processo è dipendente dall’informazione data da altri. Tempo di esecuzione di un processo dipende dagli altri | Deadlock; starvation                                      |
### processi e competizione per le risorse
I problemi principali per i processi in competizione (prima riga della tabella) sono tre:
1) necessità di mutua esclusione (sezioni critiche)
2) deadlock
3) starvation
#### mutua esclusione
Per risolvere il problema della mutua esclusione, basta che chiamino una syscall che entri nella sezione critica, faccia l'operazione ed esca.
Tuttavia, non è sempre possibile: se occorre accedere ad una risorsa che potrebbe essere condivisa con altri processi, bisogna fare una richiesta esplicita di "bloccaggio" - se avviene, si ricade nel caso di processi cooperanti.

![[mutua-escl-es.png|center|500]]

##### per i processi cooperanti
Questi processi devono essere scritti pensando già alla cooperazione, quindi scrivendo opportune syscall come `entercritical` ed `exitcritical`.
### deadlock e starvation
>[!example] esempio di deadlock
>- A richiede accesso prima alla stampante e poi al monitor
>- B prima al monitor e poi alla stampante
>- capita che lo scheduler faccia andare B in mezzo alle due richieste di A: B prende il monitor, A deve aspettare
>- le successive richieste (A monitor e B stampante) non possono essere soddisfatte (perché A ha la stampante, e B il monitor)
>- A e B restano bloccati per sempre, eppure la mutua esclusione non è stata violata

>[!example] esempio di starvation
>- A chiede accesso prima alla stampante
>- anche B
>- il Sistema Operativo dà la stampante ad A
>- A rilascia la stampante e lo scheduler gli permette di richiederla nuovamente (A rimane in esecuzione)
>- il Sistema Operativo dà di nuovo la stampante ad A (e così via per sempre...)
>- B muore di starvation (con tanti processi è probabile che succeda)
### requisiti per la mutua esclusione
Qualsiasi meccanismo si usi per offrire la mutua esclusione deve soddisfare i seguenti requisiti:
- solo un processo alla volta può essere nella sezione critica per una risorsa
- niente deadlock né starvation
- nessuna assunzione sullo scheduling o sul numero di processi
- se nessun processo usa la sezione critica, un processo deve entrarci subito (senza farlo attendere)
- un processo che si trova nella sua sezione non-critica non deve subire interferenze da altri processi (in particolare non può essere bloccato)
- un processo che si trova nella sua sezione critica ne deve prima o poi uscire
	- ci vuole cooperazione: per esempio, se è stato pensato un protocollo (es `entercritical`) per entrare nella sezione critica, non si può non rispettarlo
### mutua esclusione for dummies
Ci sono n processi che eseguono la funzione `P`, e tutti possono scrivere nella variabile condivisa `bolt`.
```C
int bolt = 0;
void P(int i) {
	while (true) {
		bolt = 1;
		while (bolt == 1) /* do nothing */;
		/* critical section */;
		bolt = 0;
		/* remainder */
	}
}

// n processi iniziano in contemporanea P()
parbegin(P(0), P(1), ..., P(n))
```
In questo esempio (<small>un processo mette `bolt` a `1` quando vuole entrare nella sezione critica, e aspetta finché non viene messo a `0` per entrarci</small>), due processi in interleaving perfetto vanno in deadlock - rimangono bloccati nel while, nessun singolo processo entrerà mai nella sezione critica (nonostante abbiamo rispettato la mutua esclusione).

La **soluzione**:
basta scambiare il momento in cui si assegna `bolt` 
```C
int bolt = 0;
void P(int i) {
	while (true) {
		while (bolt == 1) /* do nothing */;
		bolt = 1;
		/* critical section */;
		bolt = 0;
		/* remainder */
	}
}
```
Per alcuni tipi di scheduler, viene rispettata la mutua esclusione (se un solo processo entra nella critical section e un altro viene mandato in esecuzione dopo che il primo ha settato `bolt=1`) - ma non funziona per tutti i tipi di scheduling ! per esempio, basta che lo scheduler faccia eseguire P1 e P2 in interleaving, e si viola la mutua esclusione:
- se P2 viene mandato in esecuzione dopo che P1 è uscito dal while, ma prima di `bolt=1`, P1 e P2 entreranno entrambi nella sezione critica.

>[!warning] lo scheduler interrompe a livello di istruzione macchina
>Dobbiamo pensare il codice a livello assembler. un ciclo while (come nell’esempio sopra) non viene eseguito “tutto insieme” solo perchè è in una sola riga. Solo le singole istruzioni assembler vegnono sempre completate, e tra una istruzione assembler e la prossima il dispatcher può togliere la CPU al processo.
><small>(quindi, per esempio, lo scheduler potrebbe togliere la CPU anche a metà di `while(bolt == 1)`, ovvero al caricare il valore di `bolt` (0 al momento) in un registro - quindi, all'arrivo di P2, `bolt==0`)</small>
## mutua esclusione: supporto hardware
### disabilitazione delle interruzioni
```C
while (true) {
	/* prima della sezione critica */;
	disabilita_interrupt();
	/* sezione critica */;
	riabilita_interrupt();
	/* rimanente */;
}
```
Così, si toglie allo scheduler la possibilità di interrompere il processo che sta per entrare nella sezione critica, garantendo la mutua esclusione.

![[instr-cycle-interr.png|center|450]]

Questa strategia ha però dei *problemi*:
- se i processi abusano della disabilitazione, cala la multiprogrammazione e quindi le prestazioni del Sistema Operativo peggiorano
- funziona solo su sistemi con un processore solo - la disabillitazione funziona sul singolo processore, e non ha effetti su un processo eseguito su un altro processore
### istruzioni macchina speciali
Si possono utilizzare delle istruzioni macchina speciali, come `compare_and_swap` e `exchange`, entrambe *atomiche* (l'hardware garantisce che un solo processo per volta possa eseguire una chiamata a queste istruzioni, anche se ci sono più processori)
#### `compare_and_swap`
```C
int compare_and_swap(int word, int testval, int newval){
	int oldval;
	oldval = word; /*C "finto"*/
	if (word == testval) word = newval;
	return oldval;
}
```
(compara il vecchio valore con un valore "test" e, se sono uguali, setta `word` al nuovo valore. ritorna il vecchio valore)

> [!error] mutua esclusione
> ```C
> /* program mutualexclusion */
> const int n = /* number of processes */
> int bolt;
> void P(int i) {
> 	while (true) {
> 		while (compare_and_swap(bolt, 0, 1) == 1) /* do nothing */
> 		/* critical section */
> 		bolt = 0;
> 		/* remainder */
> 	}
> }
> 
> void main() {
> 	bolt = 0;
> 	parbegin(P(1), P(2), ..., P(n));
> }
> ```
> in questo caso, `compare_and_swap` controlla se `bolt == 0` - se è così, lo assegna ad `1`, e ritorna `0` --> si esce dal while, e il processo può entrare nella sezione critica
> - se un altro processo esegue `P`, `bolt` sarà `1`, quindi potrà uscire dal while solo quando il primo processo sarà uscito dalla sezione critica (e avrà quindi settato `bolt=0`)
> 
>>[!warning] attenzione
>>potrebbe però succedere che dopo aver impostato `bolt` a `0`, il primo processo vada avanti e ritorni nella sezione critica, lasciando il secondo processo in attesa (starvation)

#### `exchange`
```C
void exchange (int register, int memory){
	int temp;
	temp = memory;
	memory = register;
	register = temp;
}
```
(swappa due valori di base)
> [!error] mutua esclusione
> ```C
> /* program mutualexclusion */
> const int n = /* number of processes */;
> int bolt;
> void P(int i) {
> 	while (true) {
> 		int keyi = 1;
> 		do exchange(keyi, bolt)
> 		while (keyi != 0);
> 		/* critical section */
> 		bolt = 0;
> 		/* remainder */
> 	}
> }
> 
> void main() {
> 	bolt = 0;
> 	parbegin(P(1), P(2), ..., P(n));
> }
> ```
> in questo caso, il primo processo ad entrare scambierà `keyi` con `0`, uscirà dal while e entrerà nella sezione critica - un secondo processo continuerà invece a cercare di scambiare `keyi` (variabile locale, quindi ne esiste una per ogni processo - ed inizializzata a `0`) e `bolt`, ma questi saranno entrambi 1 fino a quando il primo processo non uscirà dalla sezione critica
> 
>>[!warning] attenzione
>>è importante che l'assegnazione `int keyi = 1` si trovi all'interno del while - altrimenti, se un processo facesse due iterazioni, non setterebbe `bolt` a `1` e altri processi potrebbero entrare, dando luogo ad una race condition

#### vantaggi e svantaggi
**vantaggi**:
- applicabili a qualsiasi numero di processi, sia con uno che con più processori
- semplici e quindi facili da verificare
- possono essere usate per gestire sezioni critiche multiple

**svantaggi**:
- basate sul *busy-waiting* (eseguono un ciclo all'infinito fino a quando non hanno il via libera per andare avanti - stanno solo aspettando - risultando in uno spreco di computazione) 
- è possibile la starvation (come visto sopra)
- è possibile il deadlock se a questi meccanismi viene associata la priorità fissa (se un processo A a bassa priorità viene interrotto mentre è nella sezione critica e un processo B a priorità alta entra nel busy waiting, B non può essere interrotto a favore di A a causa della priorità, e A non può andare avanti perché solo B, finendo la sua sezione critica, può farlo uscire dal busy-waiting)
## semafori
I semafori sono delle particolari strutture dati (con al loro interno valori interi) usate dai processi per scambiarsi segnali, forniti di tre *operazioni atomiche*:
- `initialize`
- `decrement/semWait` --> può mettere il processo in `BLOCKED` - la CPU non viene sprecata come con il busy-waiting
- `increment/semSignal` --> può portare un processo da `BLOCKED` a `READY`

(sono syscall, quindi vengono eseguite in kernel mode e possono agire direttamente sui processi)

**semafori**:
```C
struct semaphore {
	int count;
	queueType queue;
};
void semWait(semaphore a) {
	s.count--;
	if (s.count < 0) {
		/* place this process in s.queue */;
		/* block this process */
	}
}
void semSignal(semaphore a) {
	s.count++;
	if (s.count <= 0) {
		/* remove a process P from s.queue */;
		/* place process P on ready list */;
	}
}
```
- il valore assoluto di `count`, se esso è negativo, corrisponde al numero di processi in `queue`

**semafori binari**:
```C
struct binary_semaphore {
	enum {zero, one} value;
	queueType queue;
};
void semWait(binary_semaphore a) {
	if (s.value == one)
		s.value = zero;
	else {
		/* place this process in s.queue */;
		/* block this process */;
	}
}
void semSignalB(binary_semaphore a) {
	if (s.queue is empty())
		s.value = one;
	else {
		/* remove a process P from s.queue */;
		/* place process P on ready list */;
	}
}
```
- la particolarità è che, se `value == 1`, non ci sono processi in queue

>[!important] il semaforo è uno, non uno a processo

> [!note] semafori con compare_and_swap 
> ```C
> semWait(s){
> 	while(compare_and_swap(s.flag, 0, 1) == 1) /* do nothing */;
> 	s.count--;
> 	if (s.count < 0){
> 		/* place this process in s.queue */;
> 		/* block this process (must also set s.flag to 0) */;
> 	}
> 	else s.flag = 0;
> }
> 
> semSignal(s){
> 	while(compare_and_swap(s.flag, 0, 1) == 1) /* do nothing */;
> 	s.count++;
> 	if (s.count <= 0){
> 		/* remove a process P from s.queue */;
> 		/* place process P on ready list */;
> 	}
> 	s.flag = 0;
> }
> ```
> consideriamo 3 processi: A, B, C:
> 1) A ha già completato la `semiWait` e sta eseguendo codice in sezione critica. `s.count == 0`
> 2) B entra in `semiWait`, `count` va a `-1` e B diventa `BLOCKED`, `s.flag = 0`
> 3) tocca ad A, che esegue la sezione critica e `semSignal` --> `s.count++` (diventa `0`), rimuove B dalla queue e lo mette `READY`.
> 	- A completa `semSignal` e setta `s.flag = 0`
> 4) C entra in `semWait`, passa il `while compare_and_swap`, e viene fermato dallo scheduler --> `s.flag = 1`
> 5) B ripende l'esecuzione, e imposta `s.flag = 0`.
> 	- esegue la sua sezione critica e chiama `semSignal`. Passa il while. Setta `s.flag=1`
> 	- imposta `s.count=1`, termina `semSignal` e imposta `s.flag=0`
> 	- (C è fermo prima di `s.count--`, `s.count` è `1`, e `s.flag` è `0`)
> 6) arriva un nuovo processo D, che entra in `semWait`. 
> 	- passa il `while`, ora `s.flag = 1`
> 7) D esegue `s.count--` 
> 	- legge `s.count` da memoria e lo porta in `eax` (registro accumulatore). `eax == 1`
> 	- lo scheduler interrompe D ed esegue C
> 8) C continua da dov'era: esegue `c.count--` (diventa `0`), quindi non va in block
> 9) C preempted (interotto prima di terminare) nella sezione critica
> 10) tocca a D, che continua il calcolo di prima: salva `eax -1` in `s.count`, che rimane `0`
> 11) D non va in block, e continua nella sezione critica
> 
> **RACE CONDITION** :(

> [!note]- semafori con disabilitazione di interrupt (sistema monoprocessore)
> ```C
> semWait(s){
> 	inhibit interrupts;
> 	s.count--;
> 	if (s.count < 0){
> 		/* place this process in s.queue */;
> 		/* block this process and allow interrupts */;
> 	}else
> 		allow interrupts;
> }
> 
> semSignal(s){
> 	inhibit interrupts;
> 	s.count++;
> 	if (s.count <= 0){
> 		/* remove a process P from s.queue */;
> 		/* place process P on ready list */;
> 	}
> 	allow interrupts;
> }
> ```
> 

### semafori deboli e forti
In base alla politica usata per prendere un processo dalla coda dei processi, si parla di semafori deboli o semafori forti.
- **strong semaphore**:  politica FIFO
- **weak semaphore**: politica non specificata

Con i semafori forti, se usati bene, si può evitare la starvation. Con quelli deboli no.

>[!example] strong semaphore
>![[strong-semaphore.png|center|400]]
>
>(s è `s.count`)
>in (1), A è il processo in esecuzione. viene chiamata `semWait` su A, e decrementato `s.count` e visto che `s.count-1 >= 0`, A non diventa `BLOCKED`, ma va solo in `READY`
>lo stesso accade in (2), che però manda B in `BLOCKED` in (3), viene chiamata `semSignal` (si nota come `s.count` viene incrementato), e viene mandato da `BLOCKED` a `READY`
>
>![[strong-semaphore2.png|center|400]]
>in (5) viene eseguito C, e verrà chiamata `semWait`, e ciò succederà anche quando andranno in esecuzione A e B. (saltiamo quindi alcuni passaggi da (5) a (6))...
>in (6) D è in esecuzione, e gli altri 3 processi sono `BLOCKED`. viene chiamata `semSignal` e viene mandato C da `BLOCKED` a `READY`( un weak semaphore avrebbe potuto sbloccare anche A o B)

### mutua esclusione con i semafori
```C
/* program mutualexclusion */
const int n = /* number of processes */;
semaphore s = 1;

void P(int i) {
	while (true) {
		semWait(s);
		/* critical section */
		semSignal(s);
		/* remainder */
	}
}

void main() {
	parbegin(P(1), P(2), ..., P(n));
}
```

Se due processi sono eseguiti concorrentemente (P1, P2), dato che `semWait` atomica, solo uno dei due la eseguirà nella sua interezza per primo (in questo caso diciamo P1).
P1 non verrà messo in blocked, mentre P2, quando eseguirà `semWait`, sì (perché `s.count == 1`), e in questo modo non ci sarà busy-waiting.
Quando P1 avrà finito la sua sezione critica, chiamerà `semSignal`, che riporterà P2 da `BLOCKED` a `READY`, e quando P2 verrà eseguito, finirà la sua chiamata a `semWait` ed eseguirà la sua sezione critica.
>[!warning] è fondamenta che il semaforo sia inzializzato con count = 1

<small>graficamente:</small>
 
![[m-e-semafori.png|center|400]]
### problema del producer/consumer
La situazione è questa:
- uno o più processi produttori creano dati e li mettono in un buffer
- un consumatore prende dati dal buffer uno alla volta
- al buffer può accedere un solo processo, che sia produttore o consumatore

Il problema è:
- assicurare che i produttori non inseriscano dati quando il buffer è pieno
- assicurare che il consumatore non prenda dati quando il buffer è vuoto
- *mutua esclusione* sull'intero buffer
	- in realtà sarebbe possibile permettere a consumatori e produttori di agire in contemporanea, ma non considereremo questo caso
#### implementazioni
Per ora, facciamo finta che il buffer sia infinito: il produttore non ha motivo di fermarsi.
```C
/* produttore */
while (true) {
	/* produce item v */
	b[in] = v;
	in++;
}
```

(`b` è il buffer)

```C
/* consumatore */
while (true) {
	while (in <= out) /* do nothing */;
	w = b[out];
	out++;
	/* consume item w */
}
```

(`v` e `w` sono variabili locali, mentre `out` e `in` globali)

> [!tip] buffer
> ![[prodcons-buffer.png|center|250]]

(coda vuota vuol dire che `in == out`)
##### soluzione SBAGLIATA
questa soluzione usa due semafori binari, `s` e `delay`.
- il semaforo `s` è quello che garantisce la mutua esclusione - è come l'esempio sopra (mutua esclusione con semafori) - inizializzo un semaforo a 1, faccio una `semWait` subito prima e `semSignal` subito dopo 
- `produce` e `consume` sono operazioni locali di cui non ci interessa (non c'è motivo di renderle mutualmente esclusive)
- `take` e `append` sono gli equivalenti del prendersi qualcosa o aggiungere qualcosa alla coda e incrementare il puntatore
- `n` serve a ricordarsi quanti elementi ci sono nel buffer
- se il consumatore va in esecuzione per primo, come prima cosa si blocca (`semWait`, `delay` è `0`)
- quando il produttore produce, se per caso è la prima cosa che produce (`if (n==1)`), sveglia l'altro processo (settando `delay` a `1`)
- se il consumatore trova `n == 0`, va in attesa

```C
/* program producerconsumer SBAGLIATO */
int n; // numero elementi buffer
binary_semaphore s = 1, delay = 0;

void producer() {
	while (true) {
		produce();
		semWaitB(s);
		append(); 
		n++;
		if(n == 1) semSignalB(delay);
		semSignalB(s);
	}
}

void consumer() {
	semWaitB(delay);
	while (true) {
		semWaitB(s);
		take();
		n--;
		semSignalB(s);
		consume();
		if(n == 0) semWaitB(delay);
	}
}

void main() {
	n = 0;
	parbegin(producer, consumer);
}
```

>[!question] perché non funziona?
> ![[prod-cons-sbagliato.png|center|350]]
> - supponiamo che vada prima in esecuzione il produttore
> - poi il consumatore - `delay == 1`, quindi non si blocca (è ok, c'è un elemento nella coda)
> - supponiamo che, mentre faccia la consume, il dispatcher mandi in esecuzione il produttore
> 	- il produttore fa quello che deve fare
> 	- `n` vale di nuovo `1` (ha appena prodotto un nuovo dato), quindi fa di nuovo la `semSignal` su `delay`
> - ma ora il consumatore va di nuovo in esecuzione - `n` non è `0`, quindi non aspetta
> - se il consumatore va in esecuzione per due iterazioni di seguito, alla seconda, entra nella `semWait(delay)` (perché `n == 0`), ma non si blocca, perché `delay == 1` - lo mette a `0` e va avanti
> - a questo punto, il buffer è vuoto, ma il consumer può fare comunque un'altra operazione di `take`
>   
> Sostanzialmente il problema è nato perché non è stata eseguita la prima `semWaitB(delay)` dopo il `consume()`, in quanto il produttore è andato in esecuzione e ha modificato `n`.
#### soluzione corretta
Il problema sopra è stato il cambiamento di `n` da parte del produttore "a metà" dell'esecuzione di `consumer()` del consumer.
In questa soluzione, quindi si salva il valore di `n` in `m`, variabile locale, così, anche se il producer cambia `n` durante la chiamata di `consume()`, il consumatore guarda il valore "vecchio" di `n` salvato nella variabile `m`.
 
```C
int n; // numero elementi buffer
binary_semaphore s = 1, delay = 0;

void producer() {
	while (true) {
		produce();
		semWaitB(s);
		append();
		n++;
		if(n == 1) semSignalB(delay);
		semSignalB(s);
	}
}

void consumer() {
	int m; /* a local variable */
	semWaitB(delay);
	while (true) {
		semWaitB(s);
		take();
		n--;
		m = n;
		semSignalB(s);
		consume();
		if(m == 0) semWaitB(delay);
	}
}

void main() {
	n = 0;
	parbegin(producer, consumer);
}
```
#### soluzione con semafori generali
tutto quello che si può fare con i semafori binari si può fare anche con i generali e viceversa.
```C
semaphore n = 0, s = 1;
void producer() {
	while (true) {
		produce();
		semWait(s);
		append();
		semSignal(s);
		semSignal(n);
	}
}

void consumer() {
	while (true) {
		semWait(n);
		semWait(s);
		take();
		semSignalB(s);
		consume();
	}
}

void main() {
	parbegin(producer, consumer);
}
```

### produttori e consumatori con buffer circolare
Nei casi reali, il buffer non sarà infinito - si usa un **buffer circolare**.
In questo caso, se `in == out`, non vuol dire necessariamente che il buffer sia vuoto - per gestire questa cosa, forziamo la *dimensione effettiva* del buffer a `n-1` (invece che a `n`).

| Block on                           | Unblock on              |
| ---------------------------------- | ----------------------- |
| Producer: insert in full buffer    | Consumer: item inserted |
| Consumer: remove from empty buffer | Producer: item removed  |

![[buffer-circolare.png|center|350]]

#### implementazioni
**producer**:
```C
while (true) {
	/* produce item v */
	while ((in+1)%n == out) /* do nothing*/;
	b[in] = v;
	in = (in+1)%n;
}
```

**consumer**:
```C
while (true) {
	while (in == out) /* do nothing*/;
	w = b[out];
	out = (out+1)%n;
	/* consume item w */
}
```

>[!info] come funziona?
>- per l'incremento, viene utilizzato il modulo per gestire la natura circolare del buffer
>- se `(in+1)%n == out`, allora *il buffer è pieno* (vuol dire che il prossimo indice di scrittura - `in+1` - coincide con il prossimo indice di lettura - `out` -, e quindi che si sovrascriverebbe un elemento ancora non consumato)
>- se `in == out`, allora *il buffer è vuoto* - quando il produttore produce, `in` avanza, e quando il consumatore consuma, `out` avanza - quindi, se si trovano nella stessa posizione, vuol dire che sono stati prodotti tanti elementi quanti sono stati consumati

**semafori**:
- basta aggiungere un terzo semaforo, inizializzato alla lunghezza del buffer
- il producer fa una `semWait` su `e`, così, se è da solo e fa x iterazioni con x = `sizeofbuffer`, alla x+1esima si blocca (finito lo spazio)
- (la rule of thumb per i semafori è che ad ogni `wait` corrisponda una `signal`)
- il produttore, se riesce a fare un'intera iterazione, sveglia il consumatore
- `append` e `take` sono quindi protette dalle `wait` per garantire la mutua esclusione, e per il resto i due si comportano in maniera "complementare"
```C
/* program boundedbuffer */
const int sizeofbuffer = /* buffer size */;
semaphore n = 0, s = 1, e = sizeofbuffer;

void producer() {
	while (true) {
		produce();
		semWait(e); // viene decrementato ogni volta finché non si arriva
		semWait(s); // fino a 0 quando il buffer è pieno
		append();
		semSignal(s);
		semSignal(n);
	}
}

void consumer() {
	while (true) {
		semWait(n); //se è per primo si blocca subito
		semWait(s);
		take();
		semSignalB(s);
		semSignalB(e); // viene incrementato e "sveglia" il produttore
		consume();
	}
}

void main() {
	parbegin(producer, consumer);
}

```
## semafori: esempi
### trastevere
> [!summary] dati
> ![[trastevere.png|center|500]]
> - i blocchetti sono macchine, il tubo è una strada di trastevere
> - la strada si restringe e diventa a senso unico alternato: massimo 4 auto per volta
> - vince chi arriva primo, non c'è parità
> - assumendo semafori strong, le macchine dovrebbero impegnare la strettoia nell'ordine di arrivo

>[!warning] (diego dixit) se non c’è mutua esclusione si fa un frontale

```C
semaphore z = 1;
semaphore strettoia = 4;
semaphore sx = 1;
semaphore dx = 1;

int nsx = 0; // curr numero di macchine in coda a sinistra
int ndx = 0; // curr numero di macchine in coda a destra

macchina_dal_lato_sinistro () {
	wait(z) //evita deadlock sulla wait
	wait(sx);
	nsx++;
	if(nsx == 1) //se sono il primo, blocco le macchine a dx
		wait(dx); 
	signal(sx); 
	signal(z);
	
	wait(strettoia);
	passa_strettoia();
	signal(strettoia);
	
	wait(sx);
	nsx--;
	if(nsx == 0) //se sono l'ultimo, tocca a quelle a dx
		signal(dx);
	signal(sx);
}
```

- due funzioni: lato sinistro e lato destro 
#### walkthrough
la prima parte gestisce il fatto che **dentro ci devono essere massimo 4 macchine**:
- prendo un semaforo, `strettoia`, e lo inizializzo a `4`
	- quindi, se ho la funzione `passa_strettoia()`, basta fare una `wait` su questo semaforo prima di passare e una `signal` dopo essere passati
	- in questo modo, 4 macchine riescono ad eseguire `passa_strettoia`, e la quinta si fermerà sulla `wait`

ora bisogna gestire il **senso unico alternato** - se arrivano contemporaneamente una macchina da dx e una da sx, una sola deve passare e bisogna gestire le code (quelle che si accodano a quella che è passata, passano, e le altre aspettano)
 
 La prima parte di codice decide chi passa per primo, la seconda fa sì che, dopo che l'ultimo passa, tocchi all'altro lato

- ho due interi, `nsx`, `ndx` --> contano le macchine in attesa a sx e a dx
- (incremento `nsx` - sono una macchina arrivata in coda) 
	- `if (nsx == 1) wait(dx)` se sono il primo ad essere arrivato, devo bloccare le macchine dall'altro lato
- decremento `nsx` dopo essere passato
	- se ero l'ultimo (`if (nsx == 0)`) faccio passare l'altro lato

per poter fare questa cosa, sono necessarie due cose:
- `nsx` è condivisa da più processi (tutti quelli che arrivano da sx)
- ma fare un incremento su una variabile globale nasconde una possibile *race condition* (se i processi vengono eseguiti con tempistiche particolari rispetto alle istruzioni assembly che la compongono)
- questa cosa viene gestita con il semaforo `sx`, che garantisce una mutua esclusione sulla variabile (come abbiamo visto nella mutua esclusione con semafori)
- (la stessa cosa vale anche per il decremento `--nsx`)

come funziona la `wait(dx)`?
- se io arrivo ad eseguire la `wait(dx)` da sinistra, vuol dire che una macchina di destra dovrà eseguire `wait(dx)` (prima riga, equivalente alla mia `wait(sx)`) - io non mi blocco perché `dx` è inizializzato a `1`, ma lo porto a zero e quindi la macchina a destra si blocca.

Se non avessimo `wait(z)`, si rischierebbe il deadlock - verrebbero eseguite sia `wait(sx)` che `wait(dx)` ed entrambe si bloccherebbero vicendevolmente.
- il semaforo `z` è quindi di mutua esclusione e fa sì che la `wait` possa essere eseguita solo da una macchina dal lato destro o una dal lato sinistro
### il negozio del barbiere
> [!summary] dati
> ![[negozio-barbiere.png|center|350]]
> - `max_cust` - dimensione massima del negozio
> - prima ci si siede sul divano, poi da lì si accede ad una delle sedie
> 	- si compete per entrambe le risorse: un certo numero di posti sul divano (`sofa`), e uno minore di posti sulle sedie
> 	- tra divanari si compete per le sedie, tra persone in piedi si compete per il divano
> 	- i barbieri (1 per sedia) possono: dormire, tagliare i capelli, prendere i soldi dopo il taglio

#### soluzione 1
- si possono servire, nel corso di una giornata, un massimo numero di clienti (`finish`)
- c'è una sola cassa per la quale competono i barbieri

```C
// finish=numero massimo di persone servibili nel periodo
// max_clust=numero massimo di persone contemporaneamente nel negozio
// coord=numero di barbieri
semaphore
	max_clust=20, sofa=4, chair=3, coord=3, ready=0, leave_ch=0,
	paym=0, recpt=0, finish[50]={0};
	mutex1=1, mutex2=1;

int count = 0;

void customer() {
	int cust_nr;
	
	wait(max_cust); //ok se sono <= 50esimo
	enter_shop();
	
	wait(mutex1);
	cust_nr = count;
	count++;
	signal(mutex1);
	wait(sofa);
	sit_on_sofa();
	wait(chair);
	get_up_from_sofa();
	signal(sofa);
	sit_in_chair();
	wait(mutex2);
	enqueue1(cust_nr);
	signal(mutex2);
	signal(ready);
	wait(finish[cust_nr]);
	leave_chair;
	signal(leave_cr);
	pay();
	wait(recpt);
	exit_shop();
	signal(max_cust);
}

void barber() {
	int b_cust;
	while(true) {
		wait(ready);
		wait(mutex2);
		dequeue1(b_cust);
		signal(mutex2);
		wait(coord);
		cut_hair();
		signal(coord);
		signal(finish[b_cust]);
		wait(leave_ch);
		signal(chair);
	}
}

void cashier() {
	while(true) {
		wait(paym);
		wait(coord);
		accept_pay();
		signal(coord);
		signal(recpt);
	}
}
```
##### walkthrough
- alcuni semafori servono, come a trastevere, per limitare il numero di processi che possono fare una cosa (es. `sofa`, `chair`, ecc.)
**customer**:
- ha la variabile locale `cust_nr` (il numeretto) - `count` mi dice quante persone ci sono, e lo salvo nella mia variabile locale - visto che `count` è globale, è protetta dal semaforo `mutex1`
- aspetto il semaforo `sofa` - se mi fa passare, mi siedo
- aspetto `chair` - se mi fa passare, mi alzo dal divano e mi siedo sulla sedia
- a questo punto, metto il numeretto nella coda `enqueue1`, da dove il barbiere prende i clienti 
	- (i semafori `chair` e `mutex2` sono tra cliente e barbiere)
	- (notiamo che si usano due semafori diversi, `mutex1` e `mutex2` per due sezioni critiche diverse - usarne uno avrebbe funzionato, ma sarebbe stato meno efficiente)
- `signal(ready)` avvisa che sono pronto 
- `wait(finish[cust_nr])` - aspetto che un barbiere finisca - `finish[cust_nr]` è un vettore di 50 semafori, quindi devo specificare quale sto aspettando
	- ci si "libera" quando il barbiere `signal(finish[b_cust])`
- [ qui si passa al barbiere, che taglia ]
- una volta che il barbiere ha finito, segnalo che me ne sto andando
- pago e lo segnalo (il **cassiere** è inizialmente bloccato, si sblocca se qualcuno deve pagare - qui c'è l'altra parte del `coord` del barbiere - il numero di barbieri che tagliano i capelli + quelli che fanno pagare = tutti i barbieri - poi il cassiere accetta il pagamento e fa la ricevuta)
- aspetto la ricevuta, me ne vado, e reincremento `max_cust`

**barbiere**:
- (se viene eseguito per primo, aspetta che un customer sia `ready`)
- il barbiere vede qual è il numeretto da servire - `dequeue1(b_cust)` mette il numeretto nella variabile locale `b_cust`
- `wait(coord)` gestisce la coordinazione dei barbieri - se ci sono troppi barbieri che cercano di tagliare i capelli, quelli in più si fermano
- quando ha finito di tagliare i capelli, lo segnala così che il cliente si liberi
#### soluzione 2 (migliore)
- non c'è il limite massimo di clienti serviti al giorno
- niente processo separato per pagare, ma paga comunque un barbiere (libero) qualsiasi
- il semaforo `coord` non serve più (non si dividono barbieri e cassieri)
- ci sono tanti semafori `finish` quanti barbieri
- niente semaforo `leave_ch` - solo un cliente alla volta poteva alzarsi
- piccola inefficienza: solo un barbiere alla volta può preparare la propria sedia

```C
void Customer(i) {
	int my_barber;
	wait(max_cust);
	enter_shop();
	wait(sofa);
	sit_on_sopfa();
	wait(chair);
	get_up_from_sofa();
	signal(sofa);
	my_barber = next_barber;
	sit_in_chair();
	signal(ready);
	wait(finish[my_barber]);
	leave_chair();
	pay();
	signal(paym);
	wait(recpt);
	exit_shop();
	signal(max_cust);
}

int next_barber;
void Barber(i) {
	while(true) {
		wait(mutex);
		next_barber = i;
		signal(chair);
		wait(ready);
		signal(mutex);
		cut_hair();
		signal(finish[i]);
		wait(paym);
		accept_pay();
		signal(recpt);
	}
}
```
##### walkthrough
**customer**:
- mentre prima la variabile locale del cliente era il suo numeretto, ora è il numero del suo barbiere `my_barber = next_barber`
- una volta claimato un barbiere, si siede sulla sua sedia e segnala di essere pronto

**barber**:
- ora il barbiere prende un argomento, il suo numero
- il barbiere, quando è pronto, setta la variabile `next_barber` con il suo indice - per farlo, si mette in una sezione critica `mutex` (tra barbieri) che dura fino a quando qualcuno non si siede nella sedia (`signal ready` del cliente)

>[!important] variabile condivisa non protetta da semafori
>qui, c'è una variabile condivisa (`next_barber`) non protetta in lettura dentro `customer` - l'importante è che sappiamo che `next_barber` non può essere modificato da più di un barbiere contemporaneamente (perché c'è `mutex`)
