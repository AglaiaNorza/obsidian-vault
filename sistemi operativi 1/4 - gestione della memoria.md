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

##### indirizzi

Un processo ha quindi:

![[anatomia-indirizzi.png|400]]

- una zona che contiene le informazioni sul processo (PCB)
- una zona con il programma in linguaggio macchina (Program)
- una zona con i dati condivisi - variabili globali (Data)
- una zona con lo stack delle chiamate
 
Gli indirizzi che si possono avere sono o indirizzi di *salto* (jump) o *riferimento a dati* (lw, sw...) - tutti questi devono essere ricalcolati per trovare i veri indirizzi.

> [!summary] compilazione di un programma
> Un programma eseguibile viene prima scritto in una serie di moduli (che fanno cose diverse), tra cui uno per le librerie statiche utilizzate.
> Ognuno dei moduli viene compilato separatamente e si crea un file oggetto per ciascuno - il tutto viene collegato dal **linker** per creare un programma eseguibile - il **load module**, che può essere preso e caricato nella RAM dal *loader*. 
> Nel farlo, potrebbe aver bisogno di *librerie dinamiche*.
> 
> ![[loading-programma.png|400]]
> 

un singolo modulo è fatto da una parte di programma e una parte di dati condivisi:
- su un modulo ancora scritto su disco ci possono essere indirizzi simbolici
- invece, quando viene trasformato in qualcosa di eseguibile, ci sono due possibilità:
	1) *indirizzo assoluto* - funziona solo se si sa da dove si parta
	2) *indirizzo relativo* - suppongo di partire da 0 e uso l'indirizzo relativo rispetto al mio inizio -> l'esecuzione non va alla zona di memoria x, ma x + (indirizzo dell'inizio di dove mi trovavo)

![[indirizzi-programmi.png|400]]

>[!info] tipi di indirizzi
>i tipi di indirizzi sono quindi:
>- **logici** - il riferimento in memoria è indipendente dall'attuale posizionamento del programma in memoria - si trovano nelle istruzioni e vengono poi tradotti
>- **relativi** - il riferimento è espresso come uno spiazzamento rispetto a un punto noto (sono un caso particolare degli indirizzi noti)
>- **fisici o assoluti** - riferimento effettivo alla memoria

##### rilocazione

Vecchissima soluzione (CTSS) - gli indirizzi assoluti vengono determinati nel momento in cui il programma viene caricato in memoria:
- non si può fare senza hardware dedicato

Soluzione più recente - gli indirizzi assoluti vengono determinati nel momento in cui si fa *riferimento alla memoria*
- anche qui serve hardware dedicato

>[!tip] rilocazione a runtime con hardware speciale
>- l'hardware della macchina sa che il valore deve essere sommato a un certo registro per ottenere l'indirizzo fisico
>- il valore giusto da sommare è inserito dal sistema operativo nel Base Register
>
>![[rilocazione-1.png|450]]
>è un esempio di collaborazione tra sistema operativo e hardware: l'hardware fa sempre Base Register + Relative Address, e il Sistema Operativo deve ogni volta mettere l'inizio del processo nel Base Register.