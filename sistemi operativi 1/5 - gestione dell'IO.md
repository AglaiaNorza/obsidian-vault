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
1) il *processore* controlla il dispositivo periferico
2) aggiunta di un *modulo (controllore) di I/O* direttamente sul dispositivo, che permette I/O programmato senza interrupt (il processore non si deve occupare di alcuni dettagli del dispositivo stesso)
3) modulo o controllore di I/O *con interrupt* - migliora l'efficienza del processore, che non deve aspettare il completamento dell'operazione I/O
4) *DMA* - i blocchi di dati viaggiano tra dispositivo e memoria, senza usare il processore (che fa qualcosa solo a inizio e fine operazione)
5) il modulo di I/O diventa un *processore separato general purpose* (I/O channel) -il processore principale comanda a quello I/O di eseguire un certo programma di I/O in memoria principale
6) *processore per l'I/O con memoria* dedicata (come una cache), usato per comunicazioni con terminali interattivi

Nelle architetture moderne, il chipset (un chip a parte che implementa le varie connessioni dati) implementa le funzioni di interfaccia I/O.

## problemi nel progetto del sistema operativo
i Sistemi Operativi si pongono degli obiettivi nella gestione dei sistemi I/O:
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
3) **organizzazione fisica** - si occupa di allocare e deallocare spazio su disco

## buffering dell'I/O
Per mitigare molte delle difficoltà associate alla gestione dell'I/O, è stata introdotta la tecnica dell'I/O buffering.

In particolare, i problemi principali sono:
- diversi dispositivi I/O hanno velocità diverse e
- sono ottimizzati per operazioni di certe dimensioni in base al loro tipo (per esempio, se un dispositico scrive 4mb alla volta, aspetterà di avere 4mb prima di scrivere)

la soluzione è creare un **buffer** - una zona di memoria principale che il Sistema Operativo dedica al mantenimento dei dati che saranno spostati. 
(quindi, si fanno trasferimenti di input in anticipo e di output in ritardo rispetto all'arrivo della richiesta)

### senza buffer
Senza buffer, il Sistema Operativo accede al dispositivo nel momento in cui ne ha necessità:
![[no-buffer-io.png|center|400]]

### buffer singolo
Il Sistema Operativo crea un buffer in memoria principale (nel kernel space, spesso statica, a volte dinamica). Quando arriva una richiesta di I/O, viene letta e scritta prima3 nel sistema operativo e, in un secondo momento, passata al processo utente

![[single-buffer-IO.jpg|center|500]]

- lettura e scrittura sono *separate e sequenziali*

### buffer singolo orientato ai blocchi
(riguarda i dispositivi orientati a blocchi, come i dischi)
 
I trasferimenti di **input** sono fatti al buffer in system memory - il blocco viene poi mandato nello spazio utente quando necessario.
A questo punto, nonostante non sia arrivata nessun'altra richiesta di input, il blocco successivo viene comunque letto nel buffer (*input anticipato*, o *read ahead*) 
- (si legge il blocco richiesto, ma anche intorno ad esso - per principio di località, probabilmente serviranno le informazioni vicine al blocco richiesto).

L'**output**, invece, viene posticipato (per efficienza - raccolgo quanti dati voglio e poi li do in output)

(per questo quando si fa debugging in C serve la syscall `flush` - un errore può verificarsi ben dopo un print, ma a causa dell'output posticipato non si ha niente a schermo, quindi si usa per svuotare il buffer).

### buffer singolo orientato agli stream
(riguarda i dispostitivi stream-oriented, come i terminali)

Invece di un blocco, si bufferizza una linea di input o output.
Invece, per i dispositivi in cui va gestito un singolo carattere premuto, viene bufferizzato un byte alla volta.
- in pratica, è un'istanza di un ben noto problema di concorrenza: producer/consumer

### buffer doppio
Vista la piccola dimensione di un buffer, per poter gestire al meglio tutti i dispositivi I/O (senza avere il buffer sempre pieno) è utile usare un buffer multiplo.

Un processo può trasferire dati da o a uno dei buffer, mentre il Sistema Operativo svuota o riempie l'altro.
- lettura e scrittura nel buffer sono *parallele*: uno letto, l'altro scritto.

![[buffer-doppio-IO.png|center|450]]

### buffer circolare
Vengono utilizzati più di due buffer.
Ciascun buffer viene utilizzato quando l'operazione di I/O dev tenere il passo del processo.
- questo è proprio il caso producer/consumer
![[buffer-circ-IO.png|center|450]]

### buffer: pro e contro 
Il buffering smussa i picchi di richieste di I/O (permettendo di non mantenere il processore idle), ma, se la domanda è molta, i buffer si riempiono e il vantaggio si perde.
- è utile soprattutto quando ci sono molti dispositivi I/O diversi tra di loro

#### overhead e buffer zero copy
Il buffering introduce overhead a causa della copia intermedia che viene fatta in Kernel Memory:
![[buffer-overhead.png|center|500]]

(i dati vengono prima copiati nel kernel buffer, poi nella zona utente, e solo poi nella sezione dell'I/O).

Per ovviare a questo problema, si utilizza l'architettura del **buffer zero copy**:

![[buffer-zerocopy.png|center|500]]

- evita inutili copie intermedie non passando per lo user space - fa direttamente un trasferimento da un Kernel Buffer ad un altro.

## scheduling del disco

### HDD vs SSD
Per gestire l'I/O, il Sistema Operativo deve essere il più efficiente possibile. Uno degli ambiti in cui i progettisti di sistemi operativi si sono dati più da fare è quello dei dispositivi di archiviazione di massa.

Quello che vedremo riguarda solo gli HDD (Hard Drive Disk) e non le SSD (Solid State Disk).

### il disco

![[disco-strutt.png|center|400]]

(una traccia è una corona circolare che diventa sempre più piccola avvicinandosi al centro; un settore è una parte di cerchio determinata da due raggi; l'intertrack gap separa due tracce, l'intersector gap separa due settori)

- i *dati* si trovano sulle *tracce*, su un certo numero di settori -> per leggere e scrivere occorre sapere su che traccia e settore si trovano i dati 

Per selezionare una traccia, bisogna
- spostare una testina (se ha testine mobili) (*seek*)
- selezionare una testina (se ha testine fisse)

Per selezionare un settore, bisogna aspettare che il disco ruoti (ruota a velocità costante).
Se i dati sono tanti, potrebbero trovarsi su più settori o addirittura più tracce. (un settore misura in media 512 bytes).

### prestazioni del disco
La linea generale di un'operazione su disco può essere riassunta come segue:

![[timeline-disco.png|center|500]]

**access time**, che è la somma di:
- tempo di posizionamento (*seek time*): la testina si posiziona sulla traccia desiderata
- ritardo di rotazione (*rotational delay*): l'inizio del settore raggiunge la testina

**tempo di trasferimento**: tempo necessario a trasferire i dati che scorrono sotto la tesitna.

A parte rispetto a questi:
- *wait for device*: attesa che il dispositivo sia assegnato alla richiesta
- *wait for channel*: attesa che il sottodispositivo sia assegnato alla richiesta (se ci sono più dischi che condividono un solo canale di comunicazione)

### politiche di scheduling per il disco
Come per la RAM, anche nel caso di un disco con testine mobili ci sono diverse vie per poter rendere efficienti possibile le operazioni di read/write.

>[!example] termine di confronto
>le politiche saranno confrontate su un esempio comune:
>- all'inizio la testina si trova sulla traccia numero 100.
>- ci sono 200 tracce
> 
>vengono richieste (in ordine): 55, 58, 39, 18, 90, 160, 150, 38, 184
>
>viene considerato solo il seek time, confrontato con il random (scheduling peggiore)

#### FIFO
Le richieste sono servite in modo sequenziale
- è equo nei confronti dei processi 
- se ci sono molti process in esecuzione, si comporta in modo simile al random

> [!example] tempi
> ![[FIFO-IO.png|center|500]]

### priorità
Per questa politica, l'obiettivo non è ottimizzare il disco.
- i processi batch corti potrebbero avere priorità più alta
- è desiderabile fornire un buon tempo di risposta ai processi interattivi, ma i processi più lunghi potrebbeo dover aspettare troppo
- non va bene per i DBMS

>[!example] tempi
>impossibile fare il grafico: bisognerebbe conoscere la priorità dei processi che hanno fatto le richieste

### LIFO
- ottimo per i DBMS con transazioni (quindi per sequenze di istruzioni che non possono essere interrotte). 

Il dispositivo è dato all'utente più recente - se un utente continua a fare richieste su disco, si potrebbe arrivare alla starvation.

È usata perché, se si tratta dello stesso utente, probabilmente sta accedendo sequenzialmente ad un file (ed è più efficiente mandarlo avanti).

>[!example] tempi
>impossibile fare il grafico: bisognerebbe sapere a che utente appartiene ogni richiesta

### minimo tempo di servizio
[Da questa politica in poi, l'obiettivo è di minimizzare il seek time - e serve conoscere la posizione della testina]

Sceglie la richiesta che minimizza il movimento del braccio dalla posizione attuale (quindi il tempo di posizionamento minore).
- è possibile la starvation se arrivano continuamente richieste più vicine

![[IO-mts.png|center|500]]
