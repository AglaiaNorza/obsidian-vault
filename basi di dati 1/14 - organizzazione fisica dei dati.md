![[disco-struttura.png]]

>[!summary] terminologia
>- è importante il concetto di **blocco** - è l'unità sia di allocazione che di trasferimento
>- un *file*, nel nostro caso, è un insieme omogeneo di record delle tabelle (una tabella = un file)
>
>(ricordiamo: record = ennupla = riga di una tabella)

noi faremo **due assunzioni**:
1) un blocco deve essere *allocato completamente per un certo file* (non posso allocare frazioni di blocco)
2) in un blocco si può memorizzare solo il *numero intero di record* che ci entrano (un record non può essere diviso tra diversi blocchi)

 Il "file principale" è composto dai blocchi che contengono i record della nostra tabella.
 
 In un record, oltre ai campi che corrispondono agli attributi, possiamo trovare anche un puntatore ad altri record/blocchi o informazioni sul record

[ aggiungi da slide ]


All'inizio di un record alcuni byte possono essere utilizzati per:
- specificare il tipo di record (serve in casi reali ma non in quelli che tratteremo, in cui vale l'assunzione per cui in uno stesso blocco sono allocati solo record dello stesso file)
- specificare la lunghezza del record (se ha campi a lunghezza variabile)
- contenere un bit di "cancellazione" o di "usato/non usato" (la cancellazione non viene effettuata immediatamente, ma al momento della "garbage collection")

per accedere a un campo:
- **offset**: numero di byte del record che precedono il campo (se tutti i campi hanno lunghezza fissa, l'inizio di ciascun campo sarà sempre ad un numero fisso di byte dall'inizio del record)

se il record contiene campi a lunghezza variabile:
- a inizio campo potrebbe esserci un contatore che specifica la lunghezza del campo in numero di byte

oppure
- all'inizio del record

### puntatori
un puntatore ad un record/blocco è un dato che permette di accedere rapidamente al record/blocco.


### operazioni
un'operazione sulla base di dati consiste di:
- ricerca 
- inserimento (implica ricerca se vogliamo evitare duplicati)
- cancellazione (implica ricerca)
- modifica (implica ricerca)

di un record

>[!info] la ricerca è alla base di tutte le altre operazioni

- vedremo che una struttura hash non deve per forza avere una chiave relazionale, ma un qualsiasi attributo può fare da "chiave di hashing"

## file heap
partiamo da una "non-organizzazione": la collocazione di record nei file in ordine determinato solo dall'ordine di inserimento.

- ha le prestazioni peggiori nella ricerca
- l'inserimento è molto veloce se ammettiamo duplicati

![[file-heap-es.png|center|300]]

visto che un record viene inserito sempre come ultimo record del file, tutti i blocchi tranne l'ultimo sono pieni.
- l'accesso al file avviene attraverso la directory (che contiene i puntatori ai blocchi)

Se si vuole cercare un record, occorre scandire tutto il file, iniziando dal primo record fino a trovare quello desiderato.
(se si cerca una chiave relazionale, ci si può fermare una volta trovato il dato. se non si cerca una chiave, bisogna trovare tutti i dati)

Il costo della ricerca varia in base a dove si trova il record: se si trova nell'i-esimo blocco, occorre effettuare i accessi.
Ha senso valutare il *costo medio* della ricerca, ma solo nel caso in cui si cerca in base alla chiave: se si cerca invece in base a un altro attributo, si dovrà scorrere comunque tutto.

> [!example] esempio di valutazione
> N = 151 record
> Ogni record 30 byte
> Ogni blocco contiene 65 byte
> Ogni blocco ha un puntatore al prossimo blocco (4 byte)
> 
> Stiamo ipotizzando una struttura linkata in cui ogni blocco punta al successivo sul disco.
> 
> Per capire quanti accessi, bisogna capire quanti blocchi servono, e quindi quanti record interi vanno in ogni blocco:
> - (65 taglia blocco -4) (spazio puntatore)/30 = 2,03 - non posso metterci lo 0,3 di record, quindi bisogna prendere la parte intera inferiore: 2.
> - sapendo che ho 151 record e quanti entrano per blocco: 151/2=75,5 - qui il ragionamento è opposto: visto che devo allocare blocchi interi, devo allocare la parte intera superiore: 76
> 
> In una ricerca, devo scorrere la lista di 76 blocchi: se sono fortunato, t


## costo medio della ricerca
Cominciamo dalla ricerca quando la chiave ha un valore che non ammette duplicati.

$\text{N: numero di record}$
$\text{R: numero di record che possono essere memorizzati in un blocco}$
$n=\frac{N}{R}=\text{numero di blocchi}$

$$\large\frac{R\times1+R\times 2+\dots+R\times n}{N}=\frac{R}{N}\times \frac{n(n+1)}{2}=\frac{1}{n} \frac{n(n+1)}{2}\approx \frac{n}{2}$$


(nella parte di inserimento, manca il controllo dei duplicati - prima di lettura/scrittura, ci sarà una ricerca di duplicati - nel caso della ricerca duplicati, vale il tempo approssimato: appena trovo un duplicato, è quello:)