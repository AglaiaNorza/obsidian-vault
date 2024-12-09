## concetti base di concorrenza
Per i Sistemi Operativi moderni, è essenziale supportare più processi in esecuzione attraverso:
- multiprogrammazione
- multiprocessing
- computazione distribuita (cluster)

Un grosso problema da affrontare è quello della **concorrenza**: come questi processi interagiscono.
### multiprogrammazione
Se c'è im solo processore, i processi si alternano nel suo uso (*interleaving*)

![[interleaving.png|center|400]]

### multiprocessing
Se c'è più di un processore, i processi si alternano nell'uso di un processore (sempre interleaving) e possono sovrapporsi nell'uso dei vari processori (*overlapping*).

![[inter-overlapping.png|center|400]]

### concorrenza
La concorrenza si manifesta nelle seguenti occasioni:
- applicazioni multiple --> condividono il tempo di calcolo
- applicazioni strutturate per essere parallele --> perché generano altri processi o perché sono organizzate in thread
- struttura del sistema operativo --> gli stessi Sistema Operativo sono costituiti da svariati processi o thread in esecuzione parallela
### terminologia
- **operazione atomica** --> una sequenza *indivisibile* di comandi -  <small>il dispatcher non può interrompere queste operazioni fino alla loro terminazione (nessun altro processo può vedere uno stato intermedio o interrompere la sequenza)</small>
- **sezione critica** --> parte del codice di un processo in cui c'è un *accesso esclusivo ad una risorsa condivisa* - nessun altro processo che voglia accedere in modo esclusivo alla stessa risorsa può farlo
- **mutua esclusione** --> requisito che impone che *un solo processo sia in una data sezione critica* (avviene quando due processi cercano di accedere ad una risorsa condivisa fatta per un processo solo alla volta)
- **corsa critica** (*race condition*) --> violazione della mutua esclusione 
- **stallo** (*deadlock*) --> due o più processi non possono procedere con la prossima istruzione perché si attendono a vicenda
- **stallo attivo** (*livelock*) --> due o più processi cambian continuamente il proprio stato, l'uno in risposta all'altro, senza fare nulla di utile
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

> [!tip] buffer
> ![[prodcons-buffer.png|center|250]]

##### soluzione sbagliata
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

>[!example] esempio di errore della soluzione sopra
> ![[prod-cons-sbagliato.png|center|350]]
> Si creano problemi nel caso in cui venga mandato in esecuzione il produttore prima che il consumatore faccia il `consume()`.
> In questo caso infatti, se lo scheduler mandasse in esecuzione due volte il consumer ci si ritroverebbe in una situazione in cui `delay` è `1` (si potrebbe iniziare a consumare) ma `n` è `0` e nonostante ciò è permessa un’operazione di `take()` (`n` arriva addirittura ad essere `-1`)
> Sostanzialmente il problema è stato che il non è stata eseguita la prima `semWaitB(delay)` dopo il `consume()` in quanto è stato modificato `n`
> (il consumer viene eseguito per abbastanza tempo da leggere 2 volte di fila il buffer, e finisce a leggerlo da vuoto)