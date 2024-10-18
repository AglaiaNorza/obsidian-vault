---
sticker: lucide//file-clock
---
Il compito fondamentale di un sistema operativo è la **gestione dei processi** - computazioni di tipi diversi.
Deve quindi: 
- permettere l'esecuzione alternata di processi multipli (interleaving)
- assegnare le risorse ai processi (es. stampante, monitor ecc), e proteggere le risorse assegnate
- permettere ai processi di scambiarsi informazioni
- permettere la *sincronizzazione dei processi*

>[!info] definizioni di processo
>- un **programma in esecuzione** (o un'istanza di un programma in esecuzione, ogni esecuzione anche dello stesso programma è un processo diverso).
>- l'entità che può essere assegnata a un processore per l'esecuzione
>- un'unità di attività caratterizzata dall'esecuzione di una **sequenza di istruzioni**, da uno **stato**, e da un insieme associato di **risorse**
>- è composto da:
>	- *codice*: le istruzioni da eseguire
>	- un insieme di *dati*
>	- attributi che descrivono lo *stato* del processo

un "processo in esecuzione" vuol dire solo che "un utente ha richiesto l'esecuzione di un programma che non è ancora terminato" (quindi non vuol dire che sia necessariamente in esecuzione su un processore).
Dietro ogni processo c'è un *programma* (tipicamente memorizzato su archiviazione di massa - tranne per alcuni processi creati dal sistema operativo stesso), che, quando viene eseguito, genera almeno un processo.

>[!summary] macrofasi di un processo
>un processo ha 3 macrofasi: **creazione**, **esecuzione**, **terminazione**.
>- la terminazione può essere *prevista* (es. quando ha finito di eseguire le istruzioni, o quando un utente lo chiude) o *non prevista* (es. interrupt, eccezioni, accessi non consentiti)

### elementi di un processo
Finché il processo è in esecuzione, ad esso è associato un insieme di informazioni, tra cui: 
- un identificatore (il sistema operativo deve poter identificare i processi)
- uno stato
- una priorità
- hardware context - valore corrente dei registri della CPU
- puntatori alla memoria
- informazioni sullo stato dell'I/O
- informazioni di accounting - quale utente lo segue

#### process control block
per ogni processo ancora in esecuzione, esiste un **process control block**, che racchiude le informazioni sul processo e si trova nella zona di memoria riservata al kernel.
- è creato e gestito dal sistema operativo, e gli permette di gestire più processi contemporaneamente
- la sua funzione principale è di avere abbastanza informazioni per poter fermare un programma in esecuzione e farlo riprendere dallo stesso punto in cui si trovava.

#### traccia ed esecuzione di un processo
La traccia di un processo (**trace**) è la *sequenza di istruzioni che vengono eseguite*.
- il *dispatcher* è un piccolo programma che sospende un processo per farne andare in esecuzione un altro.

>[!example] esecuzione di un processo
>![[es-processo.png|100]]
>![[es-processo2.png|400]]

#### stato di un processo
>[!info] modello dei processi a due stati
>- in esecuzione
>- non in esecuzione (ma comunque "attivo")
> 
avrebbe una struttura del genere:
>![[stati-processo.png|450]]

- in ogni istante, in un sistema operativo, ci sono n>=1 processi (come minimo una CLI o una GUI)
- ad ogni comando dell'utente, quasi sempre si crea un nuovo processo - attraverso il processo di **process spawning**

>[!error] terminazione di un processo
>avviene per:
>- normale completamento: viene generato un HALT che genera un'interruzione per il sistema
>- uccisioni: dal SO per errori (es. memoria non disponibile, operazioni fallite, errore fatale), dall'utente, da un altro processo
>
>e si passa da n>=2 processi a n-1

>[!info] modello di processi a 5 stati
>![[stati-processo-5.png|450]]
>
>(in realtà si può passare anche da ready a blocked o exit se un processo viene killato da un altro processo)
> 
>![[stati-processo-5-dati.png|400]]

##### processi sospesi
il processore è più veloce dell'I/O, quindi potrebbe succedere che tutti i processi in memoria siano in attesa di I/O - questi vengono swappati su disco, così da liberare memoria e non lasciare il processore inoperoso.
- lo stato *blocked* diventa *suspended* quando il processo è swappato su disco.
- ci sono quindi due nuovi stati:
	- *blocked/suspend* - swappato mentre era bloccato
	- *ready/suspend* - swappato mentre non era bloccato

![[stati-processo-tutti.png|450]]


| motivo                       | commento                                                                   |
| ---------------------------- | -------------------------------------------------------------------------- |
| swapping                     | la memoria serve per un processo ready                                     |
| interno al SO                | il SO sospetta che il processo stia causando problemi                      |
| richiesta utente interattiva | es. debugging                                                              |
| periodicità                  | il processo viene eseguito periodicamente e può venire sospeso nell'attesa |
| richiesta del padre          | il padre lo vuole sospendere per motivi di efficienza computazionale       |

### processi e risorse
Il Sistema Operativo è l'entità che gestisce l'uso delle risorse di sistema da parte dei processori, e deve dunquem conoscere lo stato di ogni processo e di ogni risorsa.
Per ogni processo/risorsa, il SO costruisce tabelle.

![[tabelle-so.png|400]]

(soprattutto i processi, si trovano nella parte di RAM riservata al kernel)
Nel **process control block** ci sono solo le informazioni essenziali i cosiddetti "attributi" - nella Primary Process Table.
Tutta la memoria necessaria al processo è nella Process Image (programma sorgente, dati, stack, PCB).
- eseguire un'istruzione cambia l'immagine del processo

(le tabelle saranno trattate in maniera più approfondita).

>[!info] attributi di un processo
![[attributi-processo.png|300]]
Le informazioni relative a un processo possono essere divise in tre categorie:
> - identificazione
> - stato
> - controllo

### come si identifica un processo
Ad ogni processo è assegnato un numero identificativo unico: il **PID** (Process Identifier).
Questo numero viene utilizzato da molte tabelle del sistema operativo per realizzare collegamenti con la tabella dei processi (es. tabella I/O mantiene una lista dei PID dei processi che stanno usando I/O).

> [!info] se un processo viene terminato il suo PID può essere riassegnato

>[!tip] stato del processore
(diverso dallo stato del processo) o Hardware Context.
Dato dai contenuti dei registri del processore in un dato momento:
> - visibili all'utente
> - di controllo e stato
> - puntatori allo stack
> - PSW (Program Status Word)

>[!Info] control block del processo
>Contiene informazioni di cui il sistema operativo ha bisogno per controllare e coordinare i vari processi attivi.
>(ovvero)
>- *PID*
>- ID del processo padre: PPID
>- ID dell'utente proprietario
> - l'*hardware context* (registri, PC, stack pointer ecc) può essere copiato sul PCB stesso in alcune occasioni.
> - informazioni per il *controllo del processo* (stato, priorità, informazioni sullo scheduling)
> - supporto per *strutture dati* (puntatori ad altri processi)
> - *comunicazioni* tra processi (flag, segnali, messaggi)
> - permessi speciali
> - gestione della memoria (puntatori)
> - uso delle risorse (file aperti, quante volte ho usato un processo ecc.)
>  
>   ![[control-block.png|400]]
>   - è la struttura più importante del sistema operativo, perché definisce il suo stato
>   - richiede protezione

### modalità di esecuzione
la maggior parte dei processori supporta almeno due modalità di esecuzione:
- modalità sistema: pieno controllo, si può accedere a qualsiasi locazione per la RAM - serve al kernel
- modalità utente: molte operazioni sono vietate - serve ai programmi utente

>[!warning] kernel mode
>esempi di operazioni kernel mode:
>- gestione dei processi (creazione e terminazione, scheduling, switching, sincronizzazione e comunicazione)
>- gestione della memoria principale (allocazione di spazio, gestione memoria virtuale)
>- gestione I/O
>- funzioni di supporto (interrupt, eccezioni, accounting (chi ha richiesto un'operazione), monitoraggio)

#### passaggio da user mode a kernel mode e ritorno
Un processo utente inizia sempre in modalità utente: per poter cambiare modalità, serve un *interrupt* (l'hardware fa partire una procedura all'interno del kernel, ma prima di farlo cambia la modalità da utente a kernel)
Quindi, *tutti gli interrupt handler sono gestiti in modalità kernel*.
Prima di restituire il controllo all'utente, l'ultima istruzione dell'interrupt handler fa lo switch a modalità utente.

- quindi, un processo utente può passare alla modalità kernel *solo per eseguire software di sistema*.

alcuni casi in cui può capitare:
- codice eseguito per conto dello stesso processo interrotto - che lo ha voluto (es. system call)
- codice eseguito per conto dello stesso processo interrotto - che non lo ha voluto (es. abort - processo viene terminato, fault - non fatale, viene eseguito qualcosa e poi si torna in user mode e si continua il processo)
- codice eseguito per conto di un altro processo

>[!example] system call sui pentium
>una system call è un pezzo di codice che 
>1) prepara gli argomenti della chiamata in opportuni registri - tra questi, il primo è un numero che identifica una system call - *system call number*
>2) esegue l'istruzione `int 0x80`, che solleva un'eccezione (dal Pentium 2 in poi, `sysenter`, che omette alcuni controlli

### creazione di un processo

>[!tip] process spawning
>la creazione di un processo da parte di un altro processo.
>- il processo *padre* crea il nuovo processo
>- il processo *figlio* è il nuovo processo
>- (tipicamente) il numero di processi aumenta, perché il padre rimane in esecuzione


per creare un processo, il sistema operativo deve:
- allocargli spazio in memoria principale (nella tabella dei processi)
- assegnargli un PID unico
- (<font color="#953734">solo unix</font>) copiare l'immagine del padre (escludendo dalla copia alcune cose)
- (<font color="#953734">solo unix</font>) incrementare i contatori di ogni file aperto dal padre (ora sono anche del figlio)
- inizializzare il process control block (con, come minimo, il nuovo PID)
- inserire il processo nella giusta coda (es. ready o ready/suspended)
- creare o espandere altre strutture dati (es. per l'accounting)
- (<font color="#953734">solo unix</font>) far ritornare alla syscall fork il PID del figlio al padre, e 0 al figlio.

[da [appunti exyss](https://raw.githubusercontent.com/Exyss/university-notes/main/Secondo%20Anno/Sistemi%20Operativi%20I.pdf):]

> [!info]
> Per poter creare i processi figli vengono utilizzate le seguenti syscall:
> - `fork()` (solo su UNIX), dove il *figlio creato è una copia esatta del padre*, condividendo con esso le stesse risorse ed ognuno avente il proprio PCB
> - `spawn()` (solo su Windows), dove *il figlio creato è un processo legato ad un programma diverso* da quello del padre e avente uno spazio d’indirizzamento diverso, dunque con istruzioni, dati e PCB diversi dal padre.
>  
> Nei sistemi UNIX-like, viene utilizzata la syscall `exec()` a seguito della chiamata `fork()` per poter ottenere lo stesso effetto della chiamata `spawn()` di Windows. 
> In particolare, la syscall `exec()` rimpiazza completamente il processo precedente, evitando di riprendere l’esecuzione del precedente una volta completato il processo avviato dalla syscall.
> 

il decision tree del processo fork si sviluppa quindi così

![[dt-fork.png]]
[back to lezioni]
(quindi, se il pid è zero, sono il figlio e faccio la parte di computazione del figlio, e altrimenti sono il padre e devo aspettare il figlio)
 
Dopodiché il Kernel può scegliere se:
- continuare ad eseguire il padre
- switchare al figlio
- switchare a un altro processo
### switching tra processi
lo switching tra processi pone svariati problemi:
- quali eventi determinano uno switch? perché il sistema operativo decide di rimpiazzare un processo?
- cosa deve fare il sistema operativo per tenere aggiornate tutte le strutture dati dopo uno switch tra processi?

quando effettuare uno switch?

| meccanismo                              | causa                                             | uso                                                                                                                                               |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| interruzione                            | esterna all'esecuzione dell'istruzione corrente   | reazione ad un evento asincrono (es. a chiede I/O, a diventa blocked e si passa a b, arriva la risposta ad a e il SO lo fa tornare in esecuzione) |
| eccezione                               | associata all'esecuzione dell'istruzione corrente | gestione di un controllo sincrono (es. pagina sbagliata della memoria virtuale)                                                                   |
| chiamata al sistema operativo (syscall) | richiesta esplicita                               | chiamata a funzione di sistema                                                                                                                    |
passaggi (in kernel mode):
- *salvare il contesto* del programma (registri CPU) nel process control block 
- aggiornare il process control block (che è running)
- spostare il PCB nella *coda* appropriata: ready, blocked, ready/suspend
- scegliere il *nuovo processo* (può avvenire anche prima) - fatto dal dispatcher
 
(passi di sopra al contrario per il nuovo processo)
- *aggiornare il process control block* del nuovo processo
- aggiornare le strutture dati per la gestione della memoria
- *ripristinare il contesto* del processo selezionato (si prende il context dal PCB e si ripristina ciò che è necessario)

### il sistema operativo è un processo?
- il sistema operativo è solo un **insieme di programmi**, ed è eseguito dal processore come ogni altro programma.
- semplicemente, ogni tanto, il SO "lascia" il processore ad altri programmi

dipende da sistema operativo a sistema operativo:
![[strutture-OS-kernel.png|400]]
1) **kernel eseguito al di fuori dei processi** 
	- il concetto di processo si applica solo ai programmi utente
	- il SO è eseguito come un'entità separata, con privilegi più elevati e una sua zona di memoria dedicata (sia per i dati che per il codice sorgente)
2) **esecuzione all'interno dei processi utente**
	- il SO viene eseguito nel contesto di un processo utente (e cambia solo la modalità di esecuzione) 
	- non c'è bisogno di un process switch per eseguire una funzione del SO, ma solo di un mode switch
	- lo stack delle chiamate (user stack) è comunque separato, mentre dati e codice macchina sono condivisi con i processi
	- il process switch avviene solo, eventualmente, alla fine, se lo scheduler decide che tocca ad un altro processo
3) **SO basato su processi** (tutto è un processo)
	- il SO è implementato come un insieme di processi di sistema, con privilegi più alti
	- l'unica cosa che non è un processo è lo switch tra processi

>[!info] caso concreto: linux
>Linux utilizza una via di mezzo tra la seconda e la terza opzione
>- le funzioni del kernel sono per lo più eseguite tramite interrupt, on behalf of il processo corrente
>- ci sono però dei processi di sistema che partecipano alla normale competizione del processore senza essere evocati esplicitamente (tipicamente processi ciclici)
>	- creati in fase di inizializzazione del SO
>	- es: creare spazio usabile nella RAM liberando zone non usate, eseguire operazioni di rete
> 
>diagramma degli stati di UNIX (molto simile ai sette stati)
> ![[unix-dgstati.png|450]]
> - si passa per forza per Kernel Running prima di arrivare a User Running perché vuol dire che si fa uno swap
> - quando un processo finisce, passa allo stato *Zombie* - perché ci si aspetta che il padre sopravviva al figlio e, finché il figlio non comunica al padre il suo exit status, resta nello stato di Zombie - l'immagine sparisce
> - lo schema non è interrompibile quando è in Kernel-Mode (ora per Linux non è così)

### processo Unix
Un processo Unix è diviso in vari livelli: utente, registro, sistema.
##### livello utente
- **process text**: codice sorgente in linguaggio macchina del processo
- **process data**: dati (valori variabili ecc)
- **user stack**: stack delle chiamate del processo (e argomenti con cui è stato chiamato)
- **shared memory**: memoria confivisa con altri processi

##### livello registro
i vari registri nel PCB, che vengono copiati al momento di un process switch (PC, Processor Status Register, SP, General Purpose Registers)

##### livello sistema
- **process table entry**: puntatore alla tabella di tutti i processi, dove individua il corrente
![[process-table-entry.png|450]]
- **u area**: informazioni per il controllo del processo
- **per process region table**: definisce il mapping tra indirizzi virtuali e fisici (page table)
- **kernel stack**: stack delle chiamate, usato per le funzioni da eseguire in modalità sistema

## thread
Per alcune applicazioni è importante essere organizzate in maniera parallela - un'applicazione viene suddivisa in diverse esecuzioni (i thread)



