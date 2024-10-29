(con memoria, si intende RAM)

- le applicazioni richiedono sempre più memoria - se il sistema operativo lasciasse a ogni processo la gestione della propria memoria, ogni processo utilizzerebbe tutta la memoria a disposizione

Quindi, il Sistema Operativo gestisce la memoria, illudendo i processi di lasciare loro tutta la memoria.
- gestire la memoria include lo swap intelligente di blocchi di dati alla memoria secondaria (disco)

### requisiti per la gestione della memoria
il sistema operativo, per la gestione della memoria, deve garantire:
- **rilocazione** e **protezione**
	- importante che ci sia aiuto hardware
- **protezione**
- **condivisione**
- **organizzazione logica**
- **organizzazione fisica**

#### rilocazione
Il programmatore (il compilatore o chi usa l'assembler) non sa e non deve sapere in quale zona della memoria il programma verrà caricato.
- se per caso viene copiato su disco, quando torna in memoria RAM può anche trovarsi un una posizione diversa.

I riferimenti alla memoria non sono quindi "veri", ma devono essere tradotti nell'indirizzo fisico che rappresentano:
- o in pre-processing, o a run-time (caso in cui serve supporto hardware)

Un processo ha quindi:

![[anatomia-indirizzi.png|400]]

- una zona che contiene le informazioni sul processo (PCB)
- una zona con il programma in linguaggio macchina (Program)
- una zona con i dati condivisi - variabili globali (Data)
- una zona con lo stack delle chiamate
 
Gli indirizzi che si possono avere sono o indirizzi di *salto* (jump) o *riferimento a dati* (lw, sw...) - tutti questi devono essere ricalcolati per trovare i veri indirizzi.

#### generazione di codice eseguibile
Un programma eseguibile viene prima scritto in una serie di moduli (che fanno cose diverse), tra cui uno ha il main. Ognuno dei moduli viene compilato separatamente e si crea un file oggetto per ciascuno - il tutto viene collegato dal **linker** per creare un programma eseguibile ()