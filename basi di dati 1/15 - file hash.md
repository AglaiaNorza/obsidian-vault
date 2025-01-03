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
>2) *quanti blocchi ci servono per la bucket directory? e per il file hash?* 
>
>$BD=\left\lceil  \frac{B}{PB} \right\rceil=\left\lceil  \frac{1200}{256}  \right\rceil=\lceil 4,69 \rceil=5$ - parte superiore perché i blocchi vengono allocati interamente
>
>b) Quanti blocchi occorrono per i bucket, assumendo una distribuzione uniforme dei record nei bucket?
>
>> supponiamo di non avere un direttorio di record all'inizio del blocco (e quindi che tutto lo spazio sia occupato dai dati). serve però un puntatore per ogni blocco per linkare i blocchi dello stesso bucket.
>
>In un blocco dobbiamo quindi memorizzare il maggior numero possibile di record + un puntatore per un eventuale prossimo blocco nel bucket.
>Abbiamo due modi per calcolare il *massimo numero di record per blocco*:
>1) Sappiamo che $M\cdot R+P\leq CB$ , ovvero il massimo numero di record x la dimensione di un record con aggiunto il puntatore deve essere minore o uguale della dimensione di un blocco (sono tutte le informazioni che inseriamo in un blocco)
>   Quindi, $M\leq \frac{1020}{300}=3,4$. Sappiamo che $M$ deve essere intero (i record non possono stare a cavallo), quindi possiamo assumere $M=3$
>2) possiamo anche sottrarre la taglia del puntatore dallo spazio utilizzabile in un blocco e prendere la parte intera inferiore della divisione dello spazio rimanente per la taglia dei record - $M=\left\lfloor  \frac{CB-P}{R}  \right\rfloor=\left\lfloor  \frac{1020}{300}  \right\rfloor=3$
> 
>>[!note] se il blocco ha un puntatore al blocco precedente
>>in questo caso devo sottrarre lo spazio di un altro puntatore da quello disponibile (o moltiplicare per due $P$ nella diseguaglianza)
> 
> Se la distribuzione dei record nei bucket è uniforme, avremo $RB=\left\lceil  \frac{NR}{B}  \right\rceil$ ovvero numero di record in un bucket = $\frac{\text{numero di record}}{\text{numero di bucket}}$
> 
> Occorrono quindi $NB=\left\lceil  \frac{RB}{M}  \right\rceil=\left\lceil  \frac{209}{3}  \right\rceil=70$ blocchi per bucket  <small>(ho $RB$ record "totali" in un bucket da distribuire in diversi blocchi)</small>
> 
> Per trovare il numero di blocchi necessario per il file hash, basta moltiplicare il numero di blocchi necessari per un bucket per il numero di bucket: $BB=NB\times B=70\times 1200=8400$
>
>3) *qual è il costo medio della ricerca?*
> 
>Se la distribuzione è uniforme, visto che la ricerca avviene solo sul bucket individuato dalla fuzione hash, <small>(avremo un numero di accessi pari a quello che si avrebbe su un heap della stessa dimensione del bucket)</small> accederemo in media alla metà dei blocchi di un bucket. Avremo quindi $MA=\left\lceil  \frac{NB}{2}  \right\rceil =\left\lceil  \frac{70}{2}  \right\rceil=35$
>
>4) *quanti bucket dovremmo creare per avere un numero medio di accessi a blocco <= 10, assumendo comunque una distribuzione uniforme?*
> 
>Dobbiamo riscrivere l'espressione di $MA$ in modo che compaia esplicitamente il numero di bucket $B$ (tralasciando gli arrotondamenti).
>Avremo quindi $\large MA=\left\lceil  \frac{NB}{2}  \right\rceil=\left\lceil \frac{\left( \frac{RB}{M} \right)}{2} \right\rceil=\left\lceil  \frac{\frac{\left( \frac{NR}{B} \right)}{M}}{2}  \right\rceil=\left\lceil  \frac{NR}{2(B\times M)}  \right\rceil$.
>Dobbiamo calcolare $B$ in modo tale che $\left\lceil  \frac{NR}{2(B\times M)}  \right\rceil\leq 10$, ovvero $B\geq \frac{NR}{20M}$.
>Nel nostro caso, avremmo $B\geq \frac{250000}{(20\times {3})}=4167$.
>
>Si può anche ragionare in un altro modo:
>sappiamo che $MA=\left\lceil  \frac{NB}{2}  \right\rceil$, quindi, per avere $MA\leq 10$, dobbiamo avere $NB\geq 20$ (con $NB$ numero di blocchi in un bucket).
>Quindi, dobbiamo avere $RB=M\times NB\leq M\times 20$, quindi $RB\leq 60$.
>Perché sia possibile, serve $\frac{NR}{B}\leq 60$ e quindi $B\geq \frac{250000}{60}$