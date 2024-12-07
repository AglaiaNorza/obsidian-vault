## visione d'insieme
I **file** sono l'elemento principale per la maggior parte delle applicazione (fanno spesso da input e output). 
- "sopravvivono" ai processi (a differenza della RAM dei processi, che viene sovrascritta)

proprietà desiderabili dei file:
- esistenza a lungo termine
- condivisibilità con altri processi (tramite nomi simbolici)
- strutturabilità (directory gerarchiche)
### gestione dei file
i file sono gestiti dal **File Management System** - insieme di programmi e librerie di utilità che vengono eseguiti in *kernel mode*.
- le librerie, invece, vengono invocate come syscall (sempre in kernel mode)

Hanno a che fare con la memoria secondaria (dischi, USB...).
- in Linux, invece, selezionate porzioni di RAM possono essere trattate come file

Forniscono un'astrazione sotto forma di operazioni tipiche, e per ogni file vengono mantenuti degli attributi (*metadati*) - proprietario, data di creazione ecc.

> [!summary] operazioni su file
> Le operazioni tipiche su file sono:
> - creazione (e scelta del nome)
> - cancellazione
> - apertura
> - lettura (solo su file aperti)
> - scrittura (solo su file aperti)
> - chiusura (necessaria per la performance)

### terminologia
Si introduce della terminologia utile:

**campi**
- dati di base
- contengono valori singoli
- caratterizzati da lunghezza e tipo di dato
- es. carattere ASCII

**record**
- insieme di campi correlati, ognuno trattato come un'unità
- es. un impiegato ha i record nome, cognome, matricola ecc.

**file**
- hanno un nome
- sono insiemi di record correlati
	- nei Sistemi Operativi generici moderni, ogni record è un solo campo con un byte
- ognuno trattato come un'unità con nome proprio
- possono implementare meccanismi di controllo all'accesso

**database**
- collezione di dati correlati
- mantengono relazioni tra gli elementi memorizzati
- vengono realizzati con uno o più file
- i DBMS (database managing systems) sono tipicamente processi di un Sistema Operativo 

### file managing systems
I sistemi per la gestione di file forniscono servizi agli utenti e alle applicazioni per l'uso di file, e definiscono il modo in cui i file sono usati.
#### obiettivi
- rispondere alla *necessità* degli utenti riguardo la gestione dei dati
- garantire he i dati nei file siano *validi*
- ottimizzare le *prestazioni* (sia dal punto di vista del Sistema Operativo - throughput - che dell'utente - tempo di risposta -)
- fornire supporto per diversi tipi di memoria secondaria
- *minimizzare la perdita* di dati
- fornire un insieme di *interfacce standard* per i processi utente
- fornire supporto per l'I/O effettuato da *più utenti in contemporanea*

#### requisiti
1) ogni utente deve essere in grado di creare, cancellare, leggere, scrivere e modificare un file
2) ogni utente deve poter accedere, in modo controllato, ai file di un altro utente
3) ogni utente deve poter leggere e modificare i permessi di accesso ai propri file
4) ogni utente deve poter ristrutturare i propri file in modo attinente al problema affrontato
5) ogni utente deve poter muovere dati da un file a un altro
6) ogni utente deve poter mantenere una copia di backup dei propri file (in caso di danno)
7) ogni utente deve poter accedere ai propri file tramite nomi simbolici

#### organizzazione del codice
[[4 - gestione della memoria#elementi centrali per il progetto di un sistema operativo]]

- **Directory Management** - tutte le operazioni utente che hanno a che fare con i file
- **File System** - struttura logica ed operazioni fisiche
- **Organizzazione Fisica** - da identificatori di file a indirizzi fisici su disco (allocazione/deallocazione)
- **Scheduling & Control** - qui ci sono i vari SCAN ecc.
## le directory
Le directory sono dei file speciali. Esse contengono le informazioni sui file (attributi, posizione, proprietario) e forniscono il mapping tra nomi dei file e file stessi.

> [!summary] operazioni
> Le **operazioni** che si effettuano su una directory sono:
> - ricerca
> - creazione file
> - cancellazione file
> - lista del contenuto
> - modifica della directory

### elementi di una directory
Gli **elementi** di una directory sono:
1) *informazioni di base*:
	- nome del file (unico in una directory data)
	- tipo del file
	- organizzazione del file (per sistemi che supportano diverse possibili organizzazioni)
2) *informazioni sull'indirizzo*:
	- volume --> dispositivo su cui il file è memorizzato
	- indirizzo di partenza (da quale traccia o disco)
	- dimensione attuale (in byte, word o blocchi)
	- dimensione allocata --> dimensione massima del file
3) *controllo di accesso*:
	- proprietario --> può concedere e negare i permessi ad altri utenti, e cambiare tali impostazioni
	- informazioni sull'accesso --> potrebbe contenere username e password per ogni utente autorizzato a leggere/scrivere
	- azioni permesse --> per controllare lettura, scrittura, esecuzione, spedizione tramite rete
4) *informazioni sull'uso*:
	- data di creazione
	- identità del creatore
	- date dell'ultimo accesso in lettura e in scrittura
	- identità dell'ultimo lettore e dell'ultimo scrittore
	- data dell'ultimo backup
	- uso attuale (lock, azione corrente...)

### strutture per le directory
Inizialmente, il metodo usato per la memorizzazione delle informazione era quello di una *lista di entry*, una per ogni file.
Ma questa soluzione non è sufficiente per la quantità di file presenti, e per esempio non permette di dare lo stesso nome a due file diversi.
Si è passati quindi a uno schema a due livelli:
#### schema a due livelli
Prevede una directory per ogni utente, più una (*master*) che le contiene.
- la master contiene anche indirizzo e informazioni per il controllo dell'accesso

Ma ogni directory utente è solo una lista di files di quell'utente - non offre una struttura per insieme di files.

Si è quindi passati ad un modello gerarchico ad albero:
#### schema gerarchico ad albero
Prevede una directory *master* che contiene tutte le directory utente.
Ogni directory utente può contenere file oppure altre directory utente.
- ci sono anche sottodirectory di sistema dentro la directory master.

![[dir-tree.png|center|300]]

##### nomi
Gli utenti devono poter fare riferimento ad un file usando solo il suo nome - i nomi devono essere unici (all'interno della stessa directory), ma un utente può non avere accesso a tutti i file del sistema.
La struttura ad albero permette di trovare un file seguendo un *directory path* nell'albero.

![[dir-ex.png|center|300]]

##### working directory
Dover dare ogni volta il path completo prima del nome di un file può essere lungo: per questo, solitamente, gli utenti o i processi interattivi hanno associata una *working/current directory*:
- tutti i nomi sono relativi ad essa
- è sempre possibile esplicitare l'intero percorso se necessario
## gestione della memoria secondaria
Il Sistema Operativo è responsabile dell'assegnamento di blocchi a file.
Ci sono due problemi correlati:
- occorre *allocare spazio per i file* e mantenerne traccia
- occorre *tener traccia* anche dello spazio allocabile.

I file si allocano in "porzioni" o "blocchi":
- l'unità minima è il settore del disco - ogni porzione o blocco è una *sequenza contigua di settori*

> [!bug] problemi da affrontare
> Per quanto riguarda l'allocazione dei file, ci sono vari problemi da affrontare:
> - decidere tra **preallocazione** o **allocazione dinamica**
> - decidere tra porzioni di dimensione fissa (*blocchi*) o dinamica (*porzioni*)
> - decidere il **metodo di allocazione**: contiguo, concatenato o indicizzato.
> - gestire la **file allocation table**, che mantiene le informazioni su dove sono, su disco, le porzioni che compongono i file

### preallocazione vs allocazione dinamica
Per poter attuare la **preallocazione**, occorre che la massima dimensione sia dichiarata a tempo di creazione: per alcune applicazioni, è facilmente stimabile, mentre per altre non lo è - in questi casi, utenti e applicazioni sovrastimeranno la dimensione per poter memorizzare le informazioni, risultando però in uno spreco di spazio su disco, a fronte di un modesto risparmio di computazione.

Per questo l'**allocazione dinamica** è quasi sempre preferita:
- la dimensione del file viene aggiustata in base alle syscall `append` e `truncate`
### dimensione delle porzioni
Per decidere la dimensione delle porzioni si hanno due opzioni agli estremi:
1) si alloca una *porzione larga abbastanza per l'intero file* --> opzione efficiente per il processo che vuole creare il file (viene allocata memoria contigua)
2) si alloca *un blocco alla volta* --> efficiente per il Sistema Operativo che deve gestire molti file
	- ciascun blocco è una sequenza di $n$ settori contigui, con $n$ fisso e piccolo (spesso =1)

Si cerca quindi un trade-off tra efficienza del singolo file e del sistema:
è ottimo, per le prestazioni di accesso al file, fare porzioni contigue, ma non possono essere troppo piccole (richiederebbero grandi tabelle di allocazione e quindi grande overhead).
Ma bisogna anche evitare porzioni fisse grandi per non rischiare di avere troppa frammentazione interna (rimane possibile la frammentazione esterna: i file possono essere cancellati).

Alla fine, rimangono due possibilità valide:
1) **porzioni grandi e di dimensione variabile**:
	- ogni allocazione è contigua
	- la tabella di allocazione non è troppo grande
	- complicata la gestione dello spazio libero: servono algoritmi ad hoc
2) **porzioni fisse e piccole**:
	- (tipicamente, un blocco per porzione)
	- spazio molto meno contiguo dell'opzione precedente
	- per lo spazio libero basta guardare una tabella di bit

Con la *preallocazione* viene naturale utilizzare *porzioni grandi e di dimensione variabile*. Infatti, non sarebbe necessaria la tabella di allocazione - per ogni file basta l’inizio e la lunghezza (ogni file è un’unica porzione) e come per il partizionamento della RAM si parlerebbe di best fit, first fit, next fit (ma qui non c’è un vincitore, ci sono troppe variabili). È inefficiente per la gestione dello spazio libero: neccessita periodica compattazione (più oneroso che compattare la RAM).
### come allocare spazio per i file
Ci sono tre modi per allocare spazio:
1) **contiguo**
2) **concatenato**
3) **indicizzato**

![[allocare-spazio.png|center|500]]

#### allocazione contigua
Un insieme di blocchi viene *allocato alla creazione* di un file.
- è necessaria la *preallocazione* - serve sapere quanto lungo, al massimo, sarà il file (altrimenti, se il file cresce oltre il limite massimo, può incontrare blocchi già occupati)
- basta *una sola entry nella tabella* di allocazione dei file: blocco di partenza e lunghezza del file
- ci sarà frammentazione esterna

> allocazione contigua:
>  
> ![[alloc-cont.png|center|350]]

> compattazione:
>  
> ![[comp-alloc-cont.png|center|350]]

#### allocazione concatenata
Viene allocato **un blocco alla volta**, e ogni blocco ha un *puntatore al blocco successivo* (alla fine del blocco).
- basta una sola entry nella tabella di allocazione dei file: blocco di partenza e lunghezza del file
- non c'è frammentazione esterna

Funziona bene per accedere sequenzialmente, ma se serve un blocco che si trova a x blocchi da quello iniziale, serve scorrere tutta la lista.
Per risolvere questo problema, si ricorre al **consolidamento** (analogo alla compattazione), per rendere contigui i blocchi di un file e migliorare l'accesso non sequenziale.

> allocazione concatenata:
>  
> ![[alloc-concat.png|center|350]]

> consolidamento:
>  
> ![[alloc-conc-consolid.png|center|350]]

#### allocazione indicizzata
L'allocazione indicizzata è una via di mezzo tra quella contigua e quella concatenata, e ne risolve quasi tutti i problemi.
- la tabella di allocazione dei file contiene apparentemente una sola entry, con l'*indirizzo di un blocco*, che, in realtà, ha una entry per ogni porzione allocata al file
- se il file è troppo grande, si fanno *più livelli*
- ci deve essere un bit che indica se un blocco è un indice o contiene dati

L'allocazione può essere con:
1) blocchi di *lunghezza fissa*: niente frammentazione esterna (un eventuale consolidamento migliora la località)
2) blocchi di *lunghezza variabile*: migliora la località (un eventuale consolidamento riduce la dimensione dell'indice)

> allocazione indicizzata con porzioni di dimensione fissa:
>  
> ![[alloc-index-fixed.png|center|350]]

> allocazione indicizzata con porzioni di lunghezza variabile:
>  
> ![[alloc-index-l-variabile.png|center|350]]

### gestione dello spazio libero
Per allocare i file, è necessario sapere dov'è lo spazio libero: non è realistico dover guardare la tabella di allocazione di tutti i file per determinare quali blocchi o porzioni sono liberi.
Serve una **tabella di allocazione di disco**.
- ogni volta che si alloca o cancella un file, lo spazio libero va aggiornato

>[!tip] tip
>È necessario che si sappia in RAM (almeno in minima parte) quanto e quale sia lo spazio libero sul disco.

Ci sono vari modi per gestirla:
- **tabelle di bit**
- **porzioni libere concatenate**
- **indicizzazione**
- **lista dei blocchi liberi**
#### tabelle di bit
Le tabelle di bit sono **vettori con un bit per ogni blocco su disco**: (`0 = libero`, `1 = occupato`).
- funziona con tutti gli schemi visti fino ad ora
- minimizza lo spazio richiesto alla tabella di allocazione del disco

Però, se il disco è quasi pieno, la ricerca di uno spazio libero può richiedere molto tempo:
- il problema è risolvibile con tabelle riassuntive di porzioni della tabella di bit 

#### porzioni libere concatenate
Le porzioni libere possono essere concatenate le une alle altre con un *puntatore* e un *intero per la dimensione*.
- quasi zero overhead di spazio
- va bene per tutti gli schemi visti fino ad ora

> [!warning] problemi
> - se c'è frammentazione, le porzioni sono tutte da un blocco e la lista diventa lunga
> - occorre leggere un blocco libero per sapere quale sia il prossimo (se se ne allocano molti, diventa time-consuming)
> - è lungo cancellare file molto frammentati
#### indicizzazione
Tratta lo spazio libero come un file, e usa un indice come per i file.
Per motivi di efficienza, l'indice gestisce le porzioni come se fossero di lunghezza variabile: c'è quindi una entry per ogni porzione libera nel disco.
È un approccio che fornisce un supporto efficiente a tutti i metodi di allocazione visti fino ad ora.

#### lista dei blocchi liberi
Ad ogni blocco viene assegnato un numero sequenziale, e la lista di questi numeri viene memorizzata in una parte dedicata del disco.
(sembra poco efficiente ma l'overhead di spazio non è grande)

Per avere parti della lista in memoria principale, si può:
- organizzare la lista come una pila (stack), e tenere soo la parte alta (`pop` per allocare spazio libero, `push` per deallocare spazio occupato)
- quando si fanno troppi `pop` e si esaurisce lo spazio della porzione caricata, se ne prende una nuova parte dal disco.

### volumi
Un volume è essenzialmente un *"disco logico"*: è una **partizione di un disco**, che può essere trattata in maniera indipendente dal file system, oppure è formato da **più dischi messi insieme visti come un disco solo** ([[5 - gestione dell'IO#RAID|LVM]]).
Sono quindi un insieme di settori in memoria secondaria che possono essere usati dal Sistema Operativo o dalle applicazioni, che li vedranno come formati da settori contigui anche se non lo sono.
- un volume può essere l'unione di volumi più piccoli
### dati e metadati
>[!info] info
>- dati --> **contenuto** dei file
>- metadati --> lista di blocchi liberi, lista di blocchi all'interno dei file, data di ultima modifica ecc.

I metadati, come i dati, si devono trovare su disco (perché devono essere persistenti), ma, per efficienza, vengono tenuti anche in memoria principale.
Però, mantenere consistenti i metadati in memoria principale e su disco è inefficiente - si fa quindi di tanto in tanto, quando il disco è poco usato, e con più aggiornamenti insieme.

Questa tecnica si chiama **journaling**, e consiste nel tenere traccia di cosa è stato modificato in una zona del disco dedicata (*log*), per poi scrivere tutto insieme in un secondo momento.
- in caso di reboot dopo un crash, basta leggere il log.

> [!warning] eventi imprevisti
> Se il computer viene spento all’improvviso senza una procedura di chiusura (per esempio per mancanza di corrente), o se il disco viene rimosso senza dare un appropriato comando (`unmount`), ci potrebbero essere problemi.
> Per risolverli, basta scrivere *un bit all’inizio del disco*, per indicare se il sistema è stato spendo correttamente. Al reboot, se il bit è `0`, occorre eseguire un programma di ripristino del disco, operazione assai complessa senza il journaling - con il journaling, invece, basta consultare il log.
### journaling
Per il journaling, è necessaria una zona dedicata del disco in cui scrivere le operazioni, prima di farne il commit nel file system.
- generalmente, viene implementato come log circolare
- evita di avere file system corrotti:
	- se la scrittura nel journal è completa, in caso di crash è possibile recuperare l'errore
	- se invece c'è un crash durante la scrittura nel journal, il file system rimane integro

#### recupero dati 
Se al reboot il bit di shutdown è `0`:
1) si confronta il journal allo stato corrente del file system
2) si correggono le inconsistenze nel file system basandosi sulle operazioni salvate nel journal

Ci sono due tipi di journaling:
- **fisico** --> copia nel journal tutti i blocchi che dovranno essere scritti nel file system, inclusi i metadati
	- nel caso di crash, basta copiare il contenuto del journal nel file system al boot successivo
- **logico** --> copia nel journal soltanto i metadati delle operazioni effettuate
	- nel caso di crash, si copiano i metadati dal journal al file system, ma si rischia la corruzione di dati (per esempio un append modifica la lunghezza, ma i contenuti aggiunti sono andati persi perché non salvati nel journal)

#### alternative al journaling
- **Soft Updates File Systems** → Le scritture su file system sono riordinate in modo da non avere mai inconsistenze, o meglio, consentono solo alcuni tipi di inconsistenze che non portano a perdita di dati (*storage leaks*)
- **Log-Structured File Systems** → L’intero file system è strutturato come un buffer circolare, detto log: dati e metadati sono scritti in modo sequenziale, sempre alla fine del log e ci possono essere diverse versioni dello stesso file, corrispondenti a diversi momenti.
- **Copy-on-Write File Systems** → Evitano sovrascritture dei contenuti dei file; scrivono nuovi contenuti in blocchi vuoti, poi aggiornano i metadati per puntare ad i nuovi contenuti.