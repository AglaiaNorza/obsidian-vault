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

#### elementi di un processo
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

>[!tip] process spawning
>la creazione di un processo da parte di un altro processo.
>- il processo *padre* crea il nuovo processo
>- il processo *figlio* è il nuovo processo
>- (tipicamente) il numero di processi aumenta, perché il padre rimane in esecuzione

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

#### processi e risorse
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

#### come si identifica un processo
Ad ogni processo è assegnato un numero identificativo unico: il **PID** (Process Identifier).
Questo numero viene utilizzato da molte tabelle del sistema operativo per realizzare collegamenti con la tabella dei processi (es. tabella I/O mantiene una lista dei PID dei processi che stanno usando I/O).

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