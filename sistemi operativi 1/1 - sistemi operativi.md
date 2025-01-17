---
sticker: lucide//git-compare
---

> [!info]- index
> - [[#sistema operativo (e i suoi componenti)|sistema operativo (e i suoi componenti)]]
> 	- [[#sistema operativo (e i suoi componenti)#registri visibili all'utente|registri visibili all'utente]]
> 	- [[#sistema operativo (e i suoi componenti)#registri interni|registri interni]]
> 	- [[#sistema operativo (e i suoi componenti)#registri di controllo e stato|registri di controllo e stato]]
> - [[#esecuzione di istruzioni|esecuzione di istruzioni]]
> 	- [[#esecuzione di istruzioni#caratteristiche di una macchina ipotetica|caratteristiche di una macchina ipotetica]]
> 	- [[#esecuzione di istruzioni#interruzioni|interruzioni]]
> - [[#fase di interruzione|fase di interruzione]]
> 	- [[#fase di interruzione#interruzioni annidate e sequenziali|interruzioni annidate e sequenziali]]
> - [[#gestione I/O|gestione I/O]]
> - [[#multiprogrammazione|multiprogrammazione]]
> - [[#gerarchia della memoria|gerarchia della memoria]]
> 	- [[#multiprogrammazione#memoria secondaria|memoria secondaria]]
> 	- [[#multiprogrammazione#cache|cache]]
> - [[#gerarchia della memoria#kernel|kernel]]
> - [[#gerarchia della memoria#caratteristiche hardware|caratteristiche hardware]]
> - [[#gerarchia della memoria#sistemi a time sharing|sistemi a time sharing]]
> - [[#gerarchia della memoria#dal job al processo|dal job al processo]]
> 	- [[#dal job al processo#gestione della memoria|gestione della memoria]]
> 

### sistema operativo (e i suoi componenti)
gestisce le risorse hardware di un sistema computerizzato (processori, RAM, i/o) e fornisce un insieme di servizi agli utenti. 

![[PC-components.png]]

1) **processore** - si occupa delle computazioni
2) **memoria principale** - è volatile, se il PC si spegne se ne perde il contenuto (chiamata reale o primaria)
3) **I/O** - memoria secondaria non volatile (dischi), comunicazione (scheda di rete..), tastiera ecc.
4) **"bus" di sistema** - fanno comunicare le parti interne del computer 
5) **registri** 
	1) *visibili all'utente*: usati dai linguaggi non interpretati
	2) *di controllo e di stato*: usati dal processore per controllare il suo utilizzo, e dal sistema operativo per controllare l'esecuzione dei programmi
	3) *interni*: usati dal processore, responsabili della comunicazione con memoria e I/O

#### registri visibili all'utente
- sono gli unici che possono essere *usati direttamente* quando si programma in linguaggio macchina. 
- possono contenere dati o indirizzi (puntatori diretti, registri-indice, puntatori a segmento, puntatori a stack)

#### registri interni
i principali registri interni sono:
- **registro dell'indirizzo di memoria** (MAR): contiene l'indirizzo della prossima operazione di lettura/scrittura
- **registro di memoria temporanea** (Memory Buffer Register): contiene i dati da scrivere in memoria, o lo spazio dove scrivere i dati letti dalla memoria
- **I/O address register** (self explanatory)
- **I/O buffer register**: registro di memoria temporanea per I/O

#### registri di controllo e stato
- **Program Counter**: contiene l'indirizzo dell'istruzione da prelevare dalla memoria
- **Instruction Register**: contiene la più recente istruzione prelevata
- **Program Status Word**: contiene le informazioni di stato
- **Flag** (codici di condizione): singoli bit settati dal processore come risultato di operazioni (es. flag ALU)
 
Questi registri vengono letti e modificati in modo implicito dalle istruzioni assembler.
Nell'architettura x86 sono considerati registri di controllo anche quelli per la gestione della memoria.

### esecuzione di istruzioni
ha due passi:
1) fase di **fetch** delle istruzioni: il processore legge il program counter e preleva le istruzioni dalla memoria principale (il PC è incrementato dopo ogni prelievo, oppure modificato da un jump)
2) fase di **execute**: il processore esegue ogni istruzione prelevata:
	1) l'istruzione prelevata viene caricata nell'Instruction Register 
 
	![[fasi-istruzioni.png]]

#### caratteristiche di una macchina ipotetica
Le istruzioni hanno un formato da 16 bit: 4 sono presi dall'OPcode, e 12 dall'address.
Anche gli interi hanno un formato da 16 bit: 1 bit per il segno, e 15 per la magnitudo

![[formato-istruzioni.png|400]]
#### interruzioni
le interruzioni interrompono la normale esecuzione sequenziale del processore (who would have thought).
- come consequenza, viene eseguito software "di sistema", parte del sistema operativo.

Le cause sono molteplici, e danno luogo a diverse *classi* di interruzioni:
- da programma (sincrone)
- da I/O, da fallimento hardware, da timer (asincrone)

Le interruzioni sincrone interrompono immediatamente l'esecuzione del programma, mentre mentre quelle asincrone vengono sollevate successivamente.

>[!example] classi di interruzioni asincrone
>- interruzioni da I/O
>- interruzioni da fallimento HW (es. power failure)
>- interruzioni da comunicazione tra CPU
>- interruzioni da timer
> 
>per i processori intel, sono chiamati *interrupt*

>[!example] classi di interruzioni sincrone
>- interruzioni di programma causate da: overflow, divisione per 0, debugging, errori di riferimenti a memoria, istruzioni errate, syscall
> 
> per i processori intel, sono chiamate *exception*

Per le interruzioni asincrone, una volta che l'handler è terminato, si riprende dall'istruzione *successiva a quella interrotta*. Per quanto riguarda le interruzioni sincrone, invece, non è detto.
Esistono infatti diversi tipi di errori:

| errore            | risoluzione                                                       |
| ----------------- | ----------------------------------------------------------------- |
| fault             | errore *corregibile*, viene rieseguita la stessa istruzione       |
| abort             | errore *non corregibile*, si esegue software collegato all'errore |
| trap, system call | si continua dall'istruzione successiva                            |
### fase di interruzione
ad ogni ciclo fetch-execute, viene controllato anche se c'è stata un'interruzione o un'exception - in quel caso, il programma viene sospeso e viene eseguita la 
 *interrupt-handler routine*.
 
![[interrupt-handler.png]]

Nell'interrupt handler, sistema operativo e hardware collaborano per salvare le informazioni e settare il Program Counter.

![[PC-interrupt-handler.png|300]]

>[!info] iter dell'interruzione di un programma
> ![[interruption-iter.png|300]] ![[interruzione.png|200]]
>Una volta completato l'handler, si torna all'indirizzo N+1 (o N, nel caso fosse una fault corregibile)


>[!question] interruzioni disabilitate
In alcuni casi, le interruzioni possono essere disabilitate.
In quel caso
![[interruzioni-disabilitate.png|400]]

#### interruzioni annidate e sequenziali
Le interruzioni possono essere di due tipi:
- **interruzioni annidate**: se, mentre eseguo un'interruzione, mi arriva una seconda interruzione, metto momentaneamente in pausa la prima per eseguire la seconda
- **interruzioni sequenziali**: se, mentre eseguo un'interruzione, mi arriva una seconda interruzione, finisco di eseguire la prima per poi passare alla seconda

### gestione I/O

[ questo argomento viene approfondito [[5 - gestione dell'IO|qui]] ]

**INPUT/OUTPUT PROGRAMMATO**

![[io-programmato.png|center|200]]

In passato, l'I/O veniva gestito tramite l'**input/output programmato**: 
- l'azione (di lettura/scrittura) viene effettuata, invece che dal processore, dal modulo di I/O, che setta i bit appropriati sul registro di stato dell'I/O
- il processore controlla lo status finché l'operazione non è completa (busy waiting) e rimane quindi bloccato
- non ci sono interruzioni

**INPUT/OUTPUT DA INTERRUZIONI**

![[io-interruzioni.png|center|200]]

Una gestione più moderna è quella dell'**input/output da interruzioni**:
- il processore viene interrotto quando il modulo I/O è pronto a scambiare dati (la CPU non deve aspettare e controllare costantemente, ma può fare altre cose)
- il processore salva il contesto del programma che stava eseguendo e comincia ad eseguire il gestore dell'interruzione
- non c'è inutile attesa, ma consuma comunque tempo di processore, poiché ogni singolo dato letto o scritto interrompe l'esecuzione del processore
 
 > [!example] flusso di controllo
> ![[flusso-IO.png|500]]
>  
>  1) nel primo caso, si può notare che il processore deve finire di eseguire il write prima di continuare con le operazioni precedenti <br></br>
>  2) nel secondo caso, il processore, una volta ricevuto un write, manda un comando al modulo dell'I/O e continua a svolgere le operazioni fino a quando l'interrupt handler non lo notifica del fatto che l'operazione è terminata <br></br>
>  3) nel terzo caso vediamo come, se l'operazione di I/O è particolarmente lunga, se riceve una seconda richiesta di write prima che la prima sia terminata, la CPU termina la prima prima di mandare il comando per la seconda e continuare le altre operazioni

**ACCESSO DIRETTO IN MEMORIA**
 
![[DMA.png|center|300]]
Il processo utilizzato dai computer più attuali è invece quello dell'**accesso diretto in memoria**:
- le istruzioni di I/O tipicamente richiedono di trasferire informazioni tra dispositivo di I/O e memoria: la *DMA* trasferisce un blocco di dati direttamente da/alla memoria
- un'interruzione viene mandata quando il trasferimento è completato
### multiprogrammazione
- un processore deve eseguire più programmi contemporaneamente
- la sequenza con cui i programmi sono eseguiti dipende dalla loro priorità e dal fatto che siano o meno in attesa di I/O
- Alla fine della gestione di un’interruzione, il controllo potrebbe non tornare al programma che era in esecuzione al momento dell’interruzione

## gerarchia della memoria
![[gerarchia-memoria.png|300]]

La memoria è organizzata in modo gerarchico, ed è divisa in:
- **inboard memory**:
	- registri
	- cache
	- main memory (RAM)
- **outboard storage**
	- disco magnetico, CD-ROM, CD-RW, DVD-RW, DVD-RAM
- **off-line storage**
	- nastro magnetico

Dall'alto verso il basso:
- diminuisce la velocità di accesso
- diminuisce il costo al bit
- aumenta la capacità
- diminuisce la frequenza di accesso alla memoria da parte della CPU
#### memoria secondaria

corrisponde ad outboard e offline storage.
- è una memoria ausiliaria ed esterna
- non è volatile, quindi il contenuto non si perde allo spegnimento del computer
- viene usata per memorizzare files
#### cache
anche all'interno dell'inboard memory stessa ci sono importanti differenze di velocità: infatti, la velocità del processore è maggiore della velocità di accesso alla memoria principale (RAM).
- per evitare eccessivi tempi di attesa, tutti i computer hanno una memoria *cache*, piccola e veloce, che sfrutta il principio di località (se si utilizzano dei dati a un determinato indirizzo, è probabile che a breve serviranno i dati ad esso vicini)
- la cache contiene copie di porzioni della RAM (quelle a cui accedere più velocemente)
- il processore controlla se un dato è nella cache: se non è presente (miss), il blocco corrispettivo viene caricato (per il principio di località)
- è gestita completamente dall'hardware: assembler, compilatore, SO ecc. non la vedono

>[!info] altre info cache
>(architettura degli elaboratori de base)
> - cache anche piccole hanno un grande impatto sulla performance 
> - bisogna trovare un "sweet spot" per la dimensione di una cache: l'accesso a una cache più piccola è più veloce, ma una cache più grande può contenere più dati
> - la cache utilizza una funzione di mappatura per determinare dove mettere il blocco proveniente dalla RAM, e un algoritmo di rimpiazzamento per scegliere quale blocco eliminare (comunemente LRU)
> - la politica di scrittura della cache determina quando scrivere in memoria (o quando un blocco viene modificato - write through, o quando un blocco viene rimpiazzato - write through)

# sistema operativo
- gestisce le risorse hardware (processori, RAM, I/O)
- il suo scopo è fornire servizi agli utenti

> [!info] servizi offerti da un sistema operativo
> - esecuzioni di programmi
> - accesso ad I/O e al sistema operativo stesso (shell)
> - sviluppo di programmi
> - rilevamento di/reazione ad errori
> - accounting (statistiche dell'uso, monitoraggio performance...)

- controlla l'esecuzione dei programmi applicativi e fornisce un'interfaccia tra applicazioni e hardware

>[!abstract] obiettivi di un sistema operativo
> - convenienza, efficienza, capacità di evolvere

- è responsabile anche della gestione delle risorse: funziona come un software, ma con privilegi più alti.
	- concede il controllo del processore ad altri programmi e controlla l'accesso alle altre risorse
### kernel
il kernel ("nucleo") è la parte di sistema operativo che si trova sempre **nella RAM**.
- contiene le funzioni più usate

### caratteristiche hardware
- protezione della memoria - non permette che la zona di memoria contenente il monitor venga modificata
	- i programmi utente vengono eseguiti in *modalità utente*, mentre il monitor viene eseguito in *modalità sistema* o kernel - (le istruzioni privilegiate possono essere eseguite e si può accedere alle aree protette della memoria)
- timer - impedisce che un job monopolizzi l'intero sistema
- istruzioni privilegiate - possono essere eseguite solo dal monitor (es. interruzioni)

>[!question] programmazione singola vs multiprogrammazione
> - con la *programmazione singola*, il processore deve aspettare che le istruzioni I/O siano completate prima di procedere
> - con la *multiprogrammazione*, se un job deve aspettare che un'istruzione I/O sia completata, il processore può passare ad un altro job

### sistemi a time sharing
- usano la multiprogrammazione per gestire contemporaneamente più jobs *interattivi* 
- il tempo del processore è condiviso tra più utenti, che accedono contemporaneamente al sistema tramite terminali

> [!info] batch vs time sharing
> (il *batch* è un semplice sistema non interattivo degli anni 60.
> utilizza un programma esterno di monitoraggio, del software per controllare le sequenze di eventi, e permette di raggruppare jobs da eseguire insieme - il programma, una volta concluso, ritorna il controllo al programma esterno di monitoraggio)
> 
> |                                    | batch                                                          | time sharing                     |
> | ---------------------------------- | -------------------------------------------------------------- | -------------------------------- |
> | **scopo**                          | massimizzare l'uso del processore                              | minimizzare il tempo di risposta |
> | provenienze delle direttive all'OS | comandi del job control language, sottomessi con il job stesso | comandi dati da terminale        |
> 

### dal job al processo
il **processo** riunisce in un unico concetto il job non-interattivo e quello interattivo.
- incorpora anche il job "transazionale real-time" (degli anni 70, es. prenotazione biglietti aerei)
 
è un'unità di attività caratterizzata da:
- un singolo *thread* di esecuzione
- uno *stato* corrente e un insieme di risorse di sistema ad esso associate

>[!warning] difficoltà della multiprogrammazione dei processi
>- errori di *sincronizzazione*: gli interrupt si perdono o vengono ricevuti due volte
>- violazione della *mutua esclusione*: ci sono problemi se due processi vogliono accedere alla stessa risorsa
>- programmi con *esecuzione non deterministica*: un processo accede ad una porzione di memoria modificata da un altro processo
>- *deadlock* (stallo): processo A attende processo B che attende A

per questo, è necessaria una buona *gestione della memoria*
#### gestione della memoria
- i **processi** vengono **isolati**
- gli **accessi** sono **protetti e controllati**
- la gestione della memoria (compresa allocazione/deallocazione) è automatica
- è supportata la **programmazione modulare** (stack)
- memorizzazione a lungo termine

>[!info] protezione dell'informazione e sicurezza
>- **disponibilità** - il dover proteggere il sistema contro l'interruzione di servizio (DoS)
>- **confidenzialità** - garanzia che gli utenti non leggano informazioni per le quali non hanno l'autorizzazione
>- **integrità dei dati** - protezione dei dati da modifiche non autorizzate
>- **autenticità** - dover verificare l'identità degli utenti/la validità di messaggi e datib