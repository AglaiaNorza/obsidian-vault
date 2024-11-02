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
>
>Servono quindi i registri:
>- Base register
>- Bounds register - indica il limite oltre il quale il processo non si può spingere
>
>e i loro valori vengono settati quando il processo viene posizionato in memoria.
>
>è un esempio di collaborazione tra sistema operativo e hardware: l'hardware fa sempre Base Register + Relative Address, e il Sistema Operativo deve ogni volta mettere l'inizio del processo nel Base Register.
##### protezione
- i processi **non devono poter accedere a locazioni di memoria di un altro processo** a meno che non siano autorizzati
- non si può fare a tempo di compilazione a causa della compilazione, quindi serve aiuto hardware
##### condivisione
- deve essere possibile permettere a più processi di **accedere alla stessa zona di memoria**
- può succedere sia per opera del programmatore, che per opera del Sistema Operativo: se più processi vengono creati eseguendo più volte lo stesso codice sorgente, è efficiente che lo condividano.
##### organizzazione logica
a livello hardware, la memoria è organizzata in modo lineare (si parte da 0 e si va avanti), ma, a livello software non vi si può accedere così.
- il Sistema Operativo deve quindi fare da **ponte tra il software e l'organizzazione della memoria**

##### organizzazione fisica
- gestione del **flusso di dati tra RAM e disco**
- non può essere lasciata al programmatore - per esempio, se si scrive un programma che richiede troppa memoria, in passato il programmatore doveva gestire manualmente lo swapping attraverso l'overlaying (sovrapposizione di moduli nella stessa zona di memoria in tempi diversi), ma ora ci pensa il Sistema Operativo
### partizionamento
uno dei primi metodi per la gestione della memoria è quello del **partizionamento** (oggi non molto usato), che può essere:
- fisso - uniforme e variabile
- dinamico
- paginazione semplice
- segmentazione semplice
- paginazione con memoria virtuale
- segmentazione con memoria virtuale

#### partizionamento fisso uniforme
la memoria è suddivisa in **partizioni di ugual lunghezza**.
- se un processo ha una dimensione <= di una partizione, può essere caricato in una partizione libera
	- se un processo ha una dimensione maggiore, sta al programmatore organizzarlo così da non occupare mai più di una partizione in ogni momento
- il Sistema Operativo può rimuovere un processo da una partizione

![[part-fisso-uni.png|center|100]]
- un programma potrebbe non entrare in una partizione
- uso inefficiente della memoria
	- problema della *frammentazione interna* - all'interno di una partizione c'è una parte usata e una non usata
#### partizionamento fisso variabile
- mitiga i problemi di quello fisso ma non li risolve

le partizioni sono di dimensione variabile, piccole e grandi - non "dinamiche", vengono decise all'inizio e non cambiano più.
![[part-fisso-variabile.png|center|100]]

>[!bug] algoritmo di posizionamento
>questa organizzazione pone fin da subito un problema: dove collocare un processo? ci vuole un algoritmo !
>- un processo va nella *partizione più piccola che può contenerlo*, per minimizzare lo spazio sprecato
>
>ci sono due possibilità di progettazione:
>- una coda per ciascun tipo di partizione, o una coda unica 
>	- (nel caso della coda unica, se per esempio la partizione della dimensione corretta è occupata, potrebbe essere necessario collocare un processo in una partizione più grande di esso per non far attendere i processi in coda)
>
>![[algo-partizione.png|center|500]]

rimangono dei problemi irrisolti:
- c'è un *numero massimo di processi* in memoria principale
- se ci sono molti processi piccoli, la memoria verrà usata in modo inefficiente

#### partizionamento dinamico
- le partizioni **variano in misura e in quantità**
- per ciascun processo viene allocata esattamente la quantità di memoria che serve

![[partiz-dinamico.png|center|100]] 
- nota: quando arriva un nuovo processo, se la memoria non basta, il Sistema Operativo sceglie un altro processo da copiare su disco e il nuovo processo lo sostituisce

> [!warning] problemi
> Se ci troviamo nella situazione della foto e arriva un processo > 6M, la memoria libera non potrà essere "sommata" e utilizzata perché non contigua, quindi questo dovrà prendere il posto di un altro processo - *frammentazione esterna*: la memoria che non è usata per nessun processo viene frammentata:
> -  si può risolvere con la *compattazione*: il Sistema Operativo sposta i processi in modo che siano contigui, ma ha un elevato overhead
>  
> Il Sistema Operativo deve decidere a quale blocco assegnare un processo:
> - algoritmo **best-fit**:
> 	- si sceglie il blocco più piccolo tra quelli adatti
> 	- è l'algoritmo con risultati peggiori, perché lascia frammenti molto piccoli, costringendo spesso a fare la compattazione
> - algoritmo **first-fit**:
> 	- comincia dall'inizio della memoria e sceglie il primo blocco con abbastanza memoria (funziona perché il partizionamento è dinamico - la memoria rimasta libera può essere assegnata)
> 	- molto veloce, ma tende a riempire solo la prima parte della memoria
> - algoritmo **next-fit**:
> 	- come il first-fit, ma parte dall'ultima posizione di mnemoria assegnata ad un processo
> 	- assegna più spesso il blocco a fine memoria
> 
> ![[es-allocazione.png|center|400]]

#### buddy-system
- compromesso tra partizionamento fisso e dinamico

Abbiamo a disposizione una dimensione per lo spazio utente di $2^U$.
Supponiamo che arrivi un processo che richiede $s$ bytes di RAM.
Il buddy-system comincia a dividere per due fino a che non si arriva a una dimensione che è un logaritmo intero di quello che voglio (un $X$ tale che $2^X-1<s\leq 2^X$) 
- con $L\leq X\leq U$  ($L$ lower bound: non si possono creare partizioni troppo piccole).

Ho quindi creato due partizioni, e una si userà per il processo.
 
Quando un processo finisce, dovrei farlo *combaciare con un altro (buddy) per creare una partizione libera più grande* - la fusione può essere effettuata solo nel caso in cui è possibile costruire una partizione di dimensione $2^{x+1}$ (il successivo multiplo di due)

> [!example]- esempio
> ![[buddy-sys.png|center|400]]
> - bisogna stare attenti a come si ricreano le partizioni del buddy system - se rilascio B (release B), ora la sua partizione è libera, ma andrebbe ricomposta: dovrei farlo *combaciare con un suo compagno per creare una porzione libera più grande* (a release B non posso, perché la successiva di 256 sarebbe 512 ma non posso ancora formarla perché la memoria contigua non basta - la formo a release E)
> 
> il buddy system si presta bene ad essere rappresentato con un albero:
> 
> ![[buddy-tree.png|center|400]]

#### paginazione semplice
(non usata, importante concettualmente)
- sia la memoria che i processi vengono spezzettati in pezzetti di grandezza uguale e piccola
	- i pezzetti di processi sono chiamati **pagine**
	- i pezzetti di memoria sono chiamati **frame**
<br>
- ogni pagina, per essere usata, *deve essere collocata in un frame* (visto che pagine e frame hanno la stessa dimensione, avviene in maniera semplice)
	- pagine contigue di uno stesso processo possono essere collocate in frame distanti (perché una pagina può essere messa in qualunque frame)

I Sistemi Operativi che adottano la paginazione devono mantenere una **tabella delle pagine** per ogni processo - (gli indirizzi devono essere reali, la tabella dice in quale frame effettivo si trova)

- quando c'è un process switch, la tabella delle pagine del nuovo processo deve essere ricaricata

>[!example] esempio 
>(i numeri rappresentano i numeri di frame - es. se il frame è grande 1k, dentro 0 ci saranno gli indirizzi da 0 a 1023)
>
>partiamo con la RAM vuota:
>![[es-pag-1.png|center|200]]
>
>- supponiamo che arrivino prima un processo da 4 pagine, poi uno da 3 e un altro da 4
>  
>  ![[es-pag-2.png|center|200]]
>  
>  - supponiamo poi che il processo B se ne vada, e che ne arrivi uno da 5 pagine: con il partizionamento dinamico, avrei dovuto compattare A e C per avere lo spazio necessario - qui invece non devo:
>    
> ![[es-pag-3.png|center|200]]
> 
> da un punto di vista delle tabelle delle pagine, la situazione è questa:
> 
> ![[es-pag-4.png|center|350]]


#### segmentazione
- un programma può essere diviso in segmenti di lunghezza variabile con un limite massimo
- un indirizzo di memoria è un numero di segmento e uno spiazzamento al suo interno
- (come per la tabella delle pagine, ci deve essere una tabella dei segmenti)
- simile al partizionamento dinamico, ma è il programmatore a decidere come deve essere segmentato un processo (a mettere i segmenti i RAM e risolvere gli indirizzi ci pensa il Sistema Operativo)

#### paginazione e segmentazione: indirizzi
Bisogna gestire gli indirizzi:
- anche qui, gli indirizzi sono logici - non sono i veri indirizzi in memoria

Per la **paginazione**:
- sappiamo che la frammentazione interna, se c'è, è molto piccola e si trova solo nell'ultima pagina del processo
- per trovare un indirizzo devo: 
	- capire in quale pagina si trova
	- ho un offset rispetto all'inizio della pagina
	- devo usare la tabella delle pagine per capire dove si trova quella pagina (dal numero di frame so dove si trova ogni pagina) e sommare l'offset

>[!example] come funziona
>- supponiamo che si riceva un indirizzo logico di 16 bit
>	- le dimensioni delle pagine sono sempre scelte per essere una potenza di 2 - per trovare la pagina dovrei dividere per la potenza di due, ma a quel punto posso direttamente ignorare gli ultimi x bit (con x=esponente di 2), e prendere i bit rimanenti - quelli avranno il risultato corretto
>	- invece, l'offset sarà rappresentato dal resto dei bit
>	- quindi, trovata la pagina nella process page table, prendo l'indirizzo e lo sostituisco a quello che era il numero della pagina (essenzialmente concatenandolo all'offset)
>	- ![[bit-paginazione.png|center|300]]

Per i **segmenti**:
- funziona in maniera analoga rispetto alla paginazione, ma bisogna considerare che i segmenti sono di dimensione variabile