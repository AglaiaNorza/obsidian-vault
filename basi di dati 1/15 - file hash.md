il file è suddiviso in **bucket** numerati da 0 a $B-1$.
- ciascun bucket è costituito da uno o più blocchi collegati tramite puntatori, ed è organizzato come un heap

![[file-hash.png|center|400]]

### bucket directory
L'accesso ai bucket avviene attraverso la **bucket directory**, che contiene $B$ elementi.
L'i-esimo puntatore contiene l'indirizzo (*bucket header*) del primo blocco dell'i-esimo bucket.

![[bucket-dir.png|center|400]]

### funzione hash
Il numero del bucket in cui deve trovarsi un record con chiave **v** è calcolato tramite una **funzione hash** h(v), che restituisce un valore da 0 a $B-1$ (sicuramente si userà quindi $\%B$)
## operazioni
Una qualsiasi operazione su un file hash richiede:
- la valutazione di h(v) per individuare il bucket
- l'esecuzione dell'operazione sul bucket, che è organizzato come un heap

Poiché l'inserimento di un record viene effettuato sull'ultimo blocco del bucket (perché ogni bucket è una heap), è opportuno che la bucket directory contenga anche, per ogni bucket, un *puntatore all'ultimo record* del bucket.

>[!summary] costo operazioni
>Se la funzione hash distribuisce uniformemente i record nei bucket, ogni bucket è costituito da $\frac{n}{B}$ blocchi, e quindi
>- il costo richiesto di un'operazione è approssimativamente 1/B-esimo del costo dell'operazione se il file fosse organizzato come una heap

### funzione hash
Una buona funzione hash deve **ripartire uniformemente i record nei bucket**, cioè, al variare della chiave, deve assumere con la stessa probabilità uno dei valori compresi tra 0 e B-1.

In genere, una funzione hash trasforma la chiave in un intero, lo divide per B e usa il resto della divisione come numero del bucket in cui deve trovarsi il record.
### considerazioni
Appare evidente che quanti più sono i bucket, tanto più è basso il costo di un'operazione. Ma il numero di bucket è limitato dalle seguenti considerazioni:
- ogni bucket deve avere almeno un blocco
- conviene che la bucket directory sia contenuta in memoria principale, o saranno necessari ulteriori accessi per leggere il suo contenuto
## esempi
>[!example] esempio 1
>abbiamo i seguenti dati:
>- il file contiene 250.000 record --> $NR = 250.000$
>- ogni record occupa 300 byte --> $R=300$
>- il campo chiave occupa 75 byte ("trappola" - è un dato inutile per questo tipo di organizzazione) --> $K=75$
>- ogni blocco contiene 1024 byte --> $CB=1024$
>- un puntatore a un blocco occupa 4 byte --> $P=4$
>
>a) Se usiamo un'organizzazione hash con 1200 bucket ($B=1200$), quanti blocchi occorrono per la bucket directory ?
>
>>Indichiamo con $B$ il numero di bucket e con $BD$ il numero di blocchi per la bucket directory (array di puntatori indicizzato da $0$ a $B-1$).
>
>1) *quanti puntatori entrano in un blocco?*
>
>$PB=\left\lfloor  \frac{CB}{P}  \right\rfloor$ (dimensione blocco/dimensione puntatore) - parte intera inferiore perché devono essere contenuti interamente
>$PB=\frac{1024}4=256$
>
>2) *quanti blocchi ci servono per la bucket directory?*
>
>$BD=\left\lceil  \frac{B}{PB} \right\rceil=\left\lceil  \frac{1200}{256}  \right\rceil=\lceil 4,69 \rceil=5$ - parte superiore perché i blocchi vengono allocati interamente
>
>b) Quanti blocchi occorrono per i bucket, assumendo una distribuzione uniforme dei record nei bucket?
>
>> supponiamo di non avere un direttorio di record all'inizio del blocco (e quindi che tutto lo spazio sia occupato dai dati). serve però un puntatore per ogni blocco per linkare i blocchi dello stesso bucket.
>
>   [ da finire :) ]
>    
>![[todo-1.png]]
>![[todo-2.png]]
>![[todo-3.png]]
>![[todo-4.png]]
