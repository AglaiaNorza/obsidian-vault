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
```c
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

