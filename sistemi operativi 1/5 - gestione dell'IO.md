[ rilettura utile: [[1 - sistemi operativi#gestione I/O|gestione I/O generale]]]
## dispositivi di I/O

ci sono tre macrocategorie di IO:
- leggibili dall'utente
- leggibili dalla macchina - comunicazione con materiale elettronico (es. dischi, USB)
- di comunicazione (input: tastiera, mouse, output: scheda di rete)

Queste macrocategorie sono molto diverse tra di loro, il che causa problemi al sistema: bisogna gestirli tutti e pensare a come tener conto delle diversità.
### funzionamento

Un dispositivo di *input* prevede di **essere interrogato sul valore** di una certa grandezza fisica al suo interno (es. codice Unicode di un tasto premuto) - un processo effettua una syscall `read` su un dispositivo per leggere un dato.
- al processo non interessa che tipo di macchina sia, ma solo il valore da leggere

Un dispositivo di *output* prevede di poter cambiare il valore di una certa grandezza fisica al suo interno (es. monitor - valore rgb dei pixel) - un processo effettua una syscall `write` per cambiare qualcosa.
- spesso l'effetto è direttamente visibile, alcune volte serve usare una funzionalità di lettura

Esistono quindi, al minimo, due syscall: `read` e `write` (che prendono in input, tra le varie cose, un identificativo del dispositivo). Al momento di una syscall, il Kernel si interpone tra processo utente e dispositivo fisico: comanda l'inizializzazione del trasferimento di informazioni, mette il processo in blocked e passa ad altro.

A trasferimento completato arriva l'interrupt (si termina l'operazione e il processo ritorna ready)
- ci possono essere dei problemi: es. un disco si è smagnetizzato
- potrebbe essere necessario fare anche altri trasferimenti, per esempio dalla RAM dedicata al DMA a quella del processo (se c'è il DMA di mezzo si complica - è il DMA a prendere i dati dalla zona utente e portarli nella zona I/O)

> [!info] driver
> La parte di Kernel che gestisce un particolare dispositivo I/O si chiama **driver** (è formata da una serie di moduli di sistema che implementano funzionalità specifiche in base al dispositivo).

### differenze tra dispositivi I/O
i dispositivi I/O possono differire sotto molti aspetti:
- *data rate* (quanto velocemente si legge/scrive)
- *applicazione*
	- ogni dispositivo I/O ha una diversa applicazione ed uso: i dischi sono usati per memorizzare file (e richiedono software per quello), ma anche per la memoria virtuale (per cui servono altri software e hardware)
- *difficoltà nel controllo*
	- una tastiera o un mouse sono più banali, mentre una stampante è più articolata (per esempio a causa dei dischi magnetici), e un disco è tra le cose più complicate
	- fortunatamente, molte cose sono controllate da hardware dedicato - la *divisione dei compiti* è (in ordine) tra: 
		- processo utente
		- syscall del Sistema Operativo 
		- driver
		- hardware (controller dei dispositivi)
- *unità di trasferimento dati* 
	- in stream di byte o caratteri (usati da memoria non secondaria, es. stampanti, schede audio...)
	- in blocchi di byte di lunghezza fissa (usati per esempio dai dischi)
- *rappresentazione dei dati*
	- i dati sono rappresentati secondo codifiche diverse su dispositivi diversi (es. ASCII vs UNICODE)
- *condizioni di errore*
	- (la natura degli errori varia molto da dispositivo a dispositivo)
	- es. diverse conseguenze: fatali (come leggere da un blocco rotto) o ignorabili (come scrivere su un blocco rotto - si scrive direttamente sul successivo)
## organizzazione della funzione di I/O
>[!summary]- ripasso diverse gestioni I/O
>I/O *programmato*:
>- l'azione su I/O viene eseguita dal modulo I/O e non dal processore, quindi il processore deve controllare costantemente lo stato dell'I/O fino a quando l'operazione non è completa (rimanendo bloccato)
> 
>I/O *da interruzioni*:
>- il processore viene interrotto quando il modulo I/O è pronto a scambiare dati (il processore, una volta ricevuto un write, manda un comando al modulo dell'I/O e continua a svolgere le operazioni fino a quando l'interrupt handler non lo notifica del fatto che l'operazione è terminata)
> 
>I/O con *Direct Access Memory*
> - (le istruzioni richiedono di trasferire informazioni tra dispositivo e memoria) - la DMA trasferisce un blocco di dati dalla memoria, e un'interruzione viene mandata quando il trasferimento è completo

Ci sono sostanzialmente quattro modi di gestire l'I/O:


|                         | senza interruzioni | con interruzioni               |
| ----------------------- | ------------------ | ------------------------------ |
| passando per la CPU     | I/O programmato    | I/O guidato dalle interruzioni |
| direttamente in memoria |                    | DMA                            |
### approfondimento: DMA

- il processore **delega le operazioni di I/O al modulo DMA**, che trasferisce i dati direttamente da o verso la memoria principale (evitando perdite di tempo)
- quando l'operazione è completata, il modulo DMA genera un interrrupt per il processore (tramite un dispositivo hardware)

![[DMA.jpg|center|450]]

### evoluzione della funzione di I/O
in ordine cronologico, l'I/O si è evoluto così:
1) il processore controlla il dispositivo periferico
2) aggiunta di un modulo (controllore) di I/O direttamente sul dispositivo, che permette I/O programmato senza interrupt (il processore non si deve occupare di alcuni dettagli del dispositivo stesso)
3) modulo o controllore di I/O con interrupt - migliora l'efficienza del processore, che non deve aspettare il completamento dell'operazione I/O
4) DMA - i blocchi di dati viaggiano tra dispositivo e memoria, senza usare il processore (che fa qualcosa solo a inizio e fine operazione)
5) il modulo di I/O diventa un processore separato general purpose (I/O channel) -il processore principale comanda a quello I/O di eseguire un certo programma di I/O in memoria principale
6) processore per l'I/O con memoria dedicata (come una cache), usato per comunicazioni con terminali interattivi

Nelle architetture moderne, il chipset (un chip a parte che implementa le varie connessioni dati) implementa le funzioni di interfaccia I/O.

## problemi nel progetto del sistema operativo
i Sistemi Operativi si pongono degli obiettivi nella gestione dei sistemi I/O

### efficienza
il problema principale è causato dal fatto che la maggior parte dei dispositivi I/O sono molto *lenti* rispetto alla memoria principale.
come gestirlo?
- un'opzione è la multiprogrammazione - la lentezza non impatta troppo sull'utilizzo del processore, che può eseguire altri processi mentre alcuni sono in attesa
- ma se ci sono molte operazioni I/O, l'I/O potrebbe comunque non stare al passo, e potrebbero non esserci più processi ready.
	- si potrebbe pensare di portare altri processi sospesi in memoria principale, ma anche questa è un'operazione I/O.
- bisogna quindi cercare soluzioni software dedicate, a livello del Sistema Operativo, per l'I/O
### generalità
i dispositivi I/O sono molto diversi tra di loro, ma sarebbe bene gestirli in modo uniforme.
- bisogna quindi nascondere la maggior parte dei dettagli dei dispositivi I/O nelle procedure di basso livello
- si offrono una serie di funzionalità (quasi) uguali per tutti: `read`, `write`, `lock`, `unlock`, `open`, `close`, che sanno come gestire i diversi dispositivi

### progettazione gerarchica
è una gerarchia simile a quella del progetto di un sistema operativo, che ci permette di nascondere dettagli specifici ai livelli più alti.
- ogni livello si basa sul fatto che il livello sottostante sa effettuare operazioni più primitive, fornendo servizi al livello superiore
- modificare l'implementazione di un livello non dovrebbe avere effetti sugli altri

per l'I/O, ci sono 3 macrotipi di gerarchie maggiormente usate:

#### 1 - dispositivo locale
riguarda i dispositivi attaccati esternamente al computer (es. stampante, monitor, tastiera...)

i livelli sono:
1) **logical I/O** - (che il Sistema Operativo offre ai processi utente) il dispositivo viene visto come una risorsa lgica con operazioni standard (es. `open`, `read`, etc)
2) **device I/O** - trasforma le richieste logiche (del livello superiore) in sequenze di comandi di I/O
3) **scheduling and control** - esegue e controlla le sequenze di comandi, eventualmente gestendo l'accodamento per massimizzare l'efficienza

#### 2 - dispositivo di comunicazione
riguarda i dispositivi che permettono la comunicazione (es. scheda ethernet, wifi...)

- organizzato come prima, ma al posto del logical I/O c'è un'**architettura di comunicazione**: il dispositivo viene visto come una risorsa logica composta a sua volta di una serie di livelli (es. TCP/IP)

#### 3 - file system
riguarda i dispositivi di archiviazione (HDD, SSD, CD, DVD, USB, floppy disk...)

i livelli sono:
1) **directory management** - operazioni utente sui file 
2) **file system** - sruttura logica ed operazioni (apri, chiudi, leggi, scrivi) (come vengono salvate e come sono mantenute le informazioni)
3) **organizzazione fisica** - 