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
