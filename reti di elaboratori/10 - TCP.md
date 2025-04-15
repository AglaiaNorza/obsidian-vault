---
created: 2025-04-01
updated: 2025-04-14T22:54
---
# introduzione
>[!info] overview
>- è un protocollo **orientato alla connessione**: è richiesto un *setup* tra i processi client e server.
>- il trasferimento dei dati è **affidabile**
>- è un protocollo con pipeline (ammette più pacchetti in transito)
>- è **bidirezionale** con piggybacking (un host è sia mittente che destinatario)
>- è **stream-oriented** (possiamo immaginare la trasmissione di dati come uno stream di byte continuo)
>- permette:
>	- **controllo di flusso** (il mittente non sovraccarica il destinatario)
>	- **controllo della congestione** (si "strozza" il processo di invio quando la rete è sovraccarica)
>	- **controllo degli errori**
>	- (comunicazione tra processi)
>	- (incapsulamento/decapsulamento)
>	- (multiplexing/demultiplexing)
>- non permette:
>	- temporizzazione
>	- garanzie su ampiezza di banda minima
>	- sicurezza

## segmenti TCP
TCP riceve i dati da trasmettere dal processo applicativo mittente come uno stream di byte. Poiché utilizza il servizio di comunicazione tra host del livello di rete che invia pacchetti, deve raggruppare un certo numero di byte in **segmenti**, aggiungere un'intestazione e consegnarli al livello di rete per la trasmissione.

![[seg-TCP.png|center|450]]

>[!summary] struttura dei segmenti TCP
>
>![[TCP-seg-struc.png|center|500]]
>
>in particolare:
>- source port e destination port ⟶ identificano i numeri di porta dell'host mittente e dell'host destinatario associati alla connesione TCP
>- **sequence number** ⟶ indica lo scostamento (in byte) dell'inizo del segmento TCP all'interno del flusso completo (a partire dall'initial sequence number, deciso all'apertura della connessione) - quindi il numero del primo byte di dati contenuto nel segmento
>- **acknowledgement number** ⟶ indica il numero di sequenza del *prossimo byte* che il destinatario si aspetta di ricevere (ha significato solo se il flag ACK è a 1)
>
>Le **flag di controllo** rappresentano:
>- `URG` ⟶ il segmento contiene un messaggio urgente 
>	- il campo ugent pointer punta alla *fine* dei dati urgenti: questi vengono infatti inseriti in testa al pacchetto, e possono essere seguiti da dati non urgenti
>- `ACK` ⟶ riscontro (campo acknowledgement) valido
>- `PSH` ⟶ i dati in arrivo non devono essere bufferizzati ma passati subito ai livelli superiori dell'applicazione
>- `RST` ⟶ la connessione non è valida; viene utilizzato in caso di grave errore, o insieme al flag ACK per la chiusura della connessione
>- `SYN` ⟶ l'host mittente del segmento vuole aprire una connessione TCP con l'host destinatario e specifica nel campo sequence number il valore dell'Initial Sequence Number
>- `FIN` ⟶ l'host mittente del segmento vuole chiudere la connessione TCP 

## connessione TCP
La connessione TCP è il percorso virtuale tra il mittente e il destinatario, sopra IP che è privo di connessione.

Essa è composta da tre fasi:
1) apertura della connessione
2) trasferimento dei dati
3) chiusura della connessione

>[!info] servizio connection-oriented
>TCP è un servizio connection-oriented, percò viene stabilita una **connessione logica** prima dello scambio dei dati.
>
>![[connection-oriented.png|center|400]]


>[!info] rappresentazione FSM
>
>![[FSM-conn-oriented.png|center|400]]

### apertura della connessione
Per l'apertura della connessione, viene effettuato un **three-way handshake**:

![[three-way.png|center|550]]

- il client manda un pacchetto composto da:
	- `SYN=1` (vuole aprire una connessione)
	- `seq` ⟶ numero generato randomicamente, che diventerà il numero di sequenza durante il trasferimento
- il server risponde con un pacchetto composto da:
	- `ACK` del pacchetto ricevuto
	- `SYN=1` (anche il server vuole aprire una connessione dati con il client)
	- `rwnd` ⟶ dimensione della finestra di ricezione
- il client risponde con un pacchetto composto da:
	- un `ACK` del pacchetto ricevuto
	- la sua `rwnd`

La **connessione è aperta** da entrambi i lati, e il trasferimento dati può iniziare.
### trasferimento dei dati

![[push-TCP.png|center|550]]

- nei primi due casi, la flag `P` è attiva, quindi il server riceve il pacchetto e lo passa subito al livello applicazione
- il terzo pacchetto, inviato dal client al server, è un ACK cumulativo per i due pacchetti ricevuti (si aspetta come prossimo pacchetto quello con sequence number `1001`)
- il quarto pacchetto non ha la flag `P`, quindi i dati verranno bufferizzati dal server; contiene anche l'ACK per il pacchetto precedente, inviato dal server.

### chiusura della connessione
Ciascuna delle due parti coinvolte nello scambio dei dati può chiedere la chiusura della connessione (sebbene sia di solito chiesta dal client o da timer nel server).

![[TCP-close.png|center|550]]

- viene usato il flag `FIN` per indicare una richiesta di chiusura di connessione
	- il server risponde con `FIN+ACK`

>[!tip] half-close
>L'half-close permette la chiusura della connessione in *una sola direzione*.
>
>![[TCP-halfclose.png|center|550]]
>
>- nel secondo caso (passive close), il client richiede la chiusura della connessione in uscita, e il server risponde solo con un `ACK` ⟶ potrà continuare a mandare dati al client

## demultiplexing orientato alla connessione
La **socket TCP** è identificata da 4 parametri, utilizzati dall'host per inviare il segmento alla socket appropriata
1) indirizzo IP di origine
2) numero di porta di origine
3) indirizzo IP di destinazione
4) numero di porta di destinazione

Un host server può supportare più socket TCP contemporaneamente: ogni socket sarà identificata dai suoi 4 parametri.

>[!tip] i server web hanno **socket differenti** per ogni connessione client
>- con HTTP non-persistente si avrà una socket differente anche per ogni richiesta dello stesso client

![[demux-connessione.png|center|500]]
## controllo degli errori
L'affidabilità deve essere implementata a livello di trasporto, perché il livello di rete è inaffidabile. Per avere un servizio di trasporto affidabile, è necessario implementare un **controllo degli errori** sui pacchetti, che possa:
- rilevare e scartare pacchetti corrotti
- tenere traccia dei pacchetti persi e gestirne il rinvio
- riconoscere pacchetti duplicati e scartarli
- bufferizzare i pacchetti fuori sequenza finché arrivano i pacchetti mancanti

>[!tip] i messaggi scambiati tra livelli sono esenti da errori, quindi il controllo degli errori coinvolge solo i livelli trasporto mittente e destinatario

Il mittente deve quindi sapere quali pacchetti ritrasmettere, e il destinatario deve saper riconoscere pacchetti duplicati e fuori sequenza. Per riuscirci, si introducono:
- un **numero di sequenza** per ogni pacchetto (con numerazione sequenziale)
- un **numero di riscontro** (ACK), che permette di notificare al mittente la corretta ricezione di un pacchetto

### numeri di sequenza e ACK di TCP
- i **numeri di sequenza** (come visto sopra) rappresentano il "numero" del primo byte del segmento nel flusso di byte 
- l'**ACK** rappresenta invece il numero di sequenza del prossimo byte atteso
	- TCP usa un ack **cumulativo** (indica che *tutti* i pacchetti fino a $n-1$ sono stati ricevuti correttamente, e il pacchetto $n$ è mancante)

>[!example]- esempio 
>
>![[TCPcom-es.png|center|350]]

### affidabilità
Per il controllo degli errori, TCP utilizza tre tecniche:
- **checksum** (controllo sul singolo pacchetto) ⟶ se un segmento arriva corrotto, viene scartato dal destinatario
- **riscontri e timer di ritrasmissione** (RTO) ⟶ utilizza ACK cumulativi e un timer associato al più vecchio pacchetto non riscontrato
- **ritrasmissione** del segmento all'inizio della coda di spedizione

#### generazione di ack
| evento                                                                                                                                         | azione                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2. arrivo **ordinato** di un segmento con numero di sequenza atteso; tutti i dati fino al numero di sequenza atteso sono già stati riscontrati | `ACK` viene ritardato (delayed). il destinatario attende fino a 500ms l’arrivo del prossimo segmento. se il segmento non arriva, invia un `ACK` (posticipato)<br>- `ACK post` |
| 3. arrivo ordinato di un segmento con numero di sequenza atteso; un altro segmento è in attesa di trasmissione dell’`ACK`                      | invia immediatamente un singolo `ACK` cumulativo, riscontrando entrambi i segmenti ordinati<br>- `ACK cum`                                                                    |
| 4. arrivo non ordinato di un segmento con numero di sequenza superiore a quello atteso; **viene rilevato un buco**                             | invia immediatamente un `ACK` duplicato, indicando il numero di sequenza del prossimo byte atteso (per indurre a **ritrasmissione rapida**)<br>- `ACK dup`                    |
| 5. arrivo di un segmento mancante (uno o più dei successivi è stato ricevuto)                                                                  | invia immediatamente un `ACK` (cumulativo)<br>- `ACK cum`                                                                                                                     |
| 6. arrivo di un segmento duplicato                                                                                                             | invia immediatamente un riscontro con numero di sequenza atteso<br>- `ACK dup`                                                                                                |
## ritrasmissione dei segmenti
Quando un segmento viene inviato, in attesa del suo riscontro, ne viene **memorizzata una copia** in una coda di attesa.
Se il segmento non viene riscontrato, può accadere che:
- *scada il timer* (quindi è il primo segmento all'inizio della coda) ⟶ il segmento viene **ritrasmesso** e il timer viene riavviato
- vengano *ricevuti 3 ACK duplicati* ⟶ **ritrasmissione veloce** del segmento (senza attendere il timeout)

>[!info] FSM mittente
>
> ![[ritr-FMS-mit.png|center|450]]

>[!info] FSM destinatario
>
>![[ritr-FSM-dest.png|center|450]]


>[!example] esempi di funzionamento
> **normale operatività**:
> 
> ![[ritr-normale.png|center|450]]
> 
> **segmento smarrito**:
> 
> ![[segm-smarrito.png|center|450]]
> 
> **ritrasmissione rapida**:
> 
> ![[ritr-rapida.png|center|450]]
> 
>**riscontro smarrito senza ritrasmissione**:
>
>![[smar-no-tras.png|center|450]]
>
>**riscontro smarrito con ritrasmissione**:
>
>![[smar-tras.png|center|450]]

## riassunto meccanismi TCP
- **pipeline** ⟶ approcco ibrido tra go-back-n e ripetizione selettiva
- **numero di sequenza** ⟶ primo byte del segmento
- **ACK cumulativo** ⟶ conferma tutti i byte precedenti a quello indicato 
- **ACK delayed** ⟶ l'ACK è posticipato nel caso di arrivo di un pacchetto in sequenza con precedenti già riscontrati
- **timeout basato su RTT** ⟶ c'è un unico timer di ritrasmissione, associato al più vecchio segmento non riscontrato
	- quando arriva una notifica intermedia, si riavvia il timer sul più vecchio segmeno non riscontrato
- **ritrasmissione**:
	- **singla** ⟶ solo il segmento non riscontrato
	- **rapida** ⟶ al terzo ACK duplicato prima del timeout si ritrasmette

## controllo del flusso
Per evitare la perdita di dati, quando un'entità produce dati che un'altra entità deve consumare, deve esistere un *equilibrio* tra la velocità di produzione e la velocità di consumo.

- Le entità che partecipano al controllo del flusso sono: processi mittente e destinatario, e trasporti mittente e destinatario. 
- Ci sono due casi di controllo di flusso: quello tra livello applicazione e livello trasporto, e quello tra livello trasporto e livello trasporto (che interessa di più al protocollo TCP)

![[controllo-flusso.png|center|500]]

Il controllo del flusso viene realizzato tramite:
- un **buffer**
- **segnali** dal consumatore al produttore:
	- il livello trasporto del mittente segnala al livello applicazione di sospendere l'invio di messaggi quando il buffer è pieno, e segnala di riprendere quando si libera spazio
	- il livello trasporto del destinatario fa la stessa cosa con il livello trasporto del mittente

### implementazione
L'obiettivo è quindi bilanciare velocità di invio con velocità di ricezione. Viene implementato tramite **feedback esplicito** del destinatario, che comunica al mittente lo spazio disponibile includendo il valore `rwnd` nell'header dei segmenti.

![[finestra-invio.png|center|450]]

- l'apertura, chiusura e riduzione della finestra di invio sono controllate dal destinatario

>[!example] esempio
> 
>![[FTP-es.png|center|400]]

## integrazione di controllo di errori e controllo di flusso
Si combinano i buffer del controllo di flusso e il numero di sequenza e ACK del controllo degli errori. 

Quindi, il **mittente**:
- quando prepara un pacchetto, usa come numero di sequenza il numero $x$ della *prima locazione libera nel buffer*
- quando invia il pacchetto, ne memorizza una copia nella locazione $x$
- quando riceve un ACK, libera la posizione di memoria che era occupata da quel pacchetto

Il **destinatario**:
- quando riceve un pacchetto con numero di sequenza $y$, lo memorizza nella locazione $y$ fino a quando il livello applicazione non è pronto a riceverlo
- quando passa il pacchetto $y$ al livello applicazione, invia un ACK al mittente

I numeri di sequenza sono calcolati in modulo $2^m$, e possono essere rappresentati con un cerchio. Il buffer può essere rappresentato tramite un insieme di settori chiamati *sliding windows*, che occupano una parte del cerchio:

![[buffer-cerchio.png|center|500]]

Oppure, può essere rappresentato in maniera lineare:

![[sliding-window.png|center|500]]

## controllo della congestione
La congestione avviene se il **carico** della rete è superiore alla sua **capacità**. Quando la rete è congestionata, c'è il rischio di:
- pacchetti smarriti
- lunghi ritardi

>[!question] controllo del flusso vs controllo della congestione
>Con il controllo del flusso, la dimensione della finestra di invio è controllata dal destinatario tramite il valore `rwnd` (contenuto in ogni segmento trasmesso nella direzione opposta). In questo modo, la finestra del ricevnte non viene mai sovraccariccata.
>
>Ma i buffer intermedi (nei router) possono comunque congestionarsi: un router riceve infatti dati da più mittenti. Quindi, nonostante non ci sia congestione agli estremi, non vuol dire che non ce ne sia nei nodi intermedi.

Ci sono due principali approcci al controllo della congestione:
- **controllo di congestion end-to-end**:
	- non c'è nessun supporto esplicito dalla rete
	- la congestione è dedotta osservando le perdite e i ritardi nei sistemi terminali
	- è il metodo adottato da TCP
- **controllo di congestione assistito dalla rete**:
	- i router forniscono un feedback ai sistemi terminali (un singolo bit per indicare la congestione)
	- c'è quindi una comunicazione esplicita al mittente della frequenza trasmissiva
### rilevare la congestione
Per rilevare la congestione si possono utilizzare **ACK duplicati** e **timeout**, che possono essere interpretati come eventi di perdita, in quanto danno indicazioni sullo stato della rete.
In particolare:
- se gli ACK arrivano **in sequenza e con buona frequenza**, si può inviare e incrementare la quantità di segmenti inviati
- se ci sono ACK **duplicati o timeout**, è necesario ridurre la finestra dei pacchetti

>[!tip] TCP è **auto-temporizzante**: reagisce in base ai riscontri che ottiene
### controllare la finestra di congestione
Per controllare la congestione, si usa la variabile `cwnd` (congestion window) che, insieme a `rwnd`, definisce la dimensione della finestra di invio.
- `cwnd` è relativa alla congestione della rete
- `rwnd` è relativa alla congestione del ricevente

$$\text{dim. finestra = min(rwnd, cwnd)}$$

### controllo della congestione
L'idea alla base della congestione è quella di incrementare il rate di trasmissione se non c'è congestione, e diminuirlo se ce n'è.

L'algoritmo di controllo della congestione si basa su tre componenti:
1) **slow start**
2) **congestion avoidance**
3) **fast recovery**

#### slow start
Nello **slow start** (incremento esponenziale), la variablile `cwnd` è inizializzata a $\text{1MSS}$ (Maximum Segment Size). Poiché però la banda disponibile può essere molto maggiore, slow start *incrementa* di $\text{1MSS}$ la `cwnd` *per ogni segmento riscontrato*.

![[slowstart.png|center|400]]

>[!example] esempio
>Se arriva un riscontro, $cwnd=cwnd+1$.
>
>Si ha quindi:
>- inizio ⟶ $cwnd=1\to 2^0$
>- dopo 1 RTT ⟶ $cwnd=cwnd+1=1+1=2\to 2^1$
>	- (`cwnd` diventa 2, quindi ora si possono inviare due pacchetti)
>- dopo 2 RTT ⟶ $cwnd=cwnd+2=2+2=4\to 2^2$
>	- (^ i due pacchetti vengono riconosciuti, quindi si ricevono 2 ACK)
>- dopo 3 RTT ⟶ $cwnd=cwnd+4=4+4=8\to 2^3$

>[!tip] la dimensione della finestra di congestione viene aumentata esponenzialmente **fino al raggiungimento della soglia `ssthresh`** oppure **finché non viene perso un pacchetto** (in tal caso, si pone $\text{ssthreshold}=\frac{\text{cwnd}}{2}$).

#### congestion avoidance
Al termine di slow start, inizia **congestion avoidance**:
- l'incremento di `cwnd` è *lineare* ($+1$ ogni volta che viene riscontrata l'intera finestra di segmenti)

Congestion avoidance continua finché non si **rileva congestione** (ovvero finché non si va in *timeout* o si ricevono *3 ACK duplicati*).
- se si va in timeout, $\text{ssthreshold} =\frac{\text{cwnd}}{2}$ e $\text{cwnd}=1$

![[cong-avoid.png|center|400]]

>[!example] esempio
>Se arriva un riscontro, $\text{cwnd = cwnd}+\frac{1}{\text{cwnd}}$ quindi:
>- inizio ⟶ $\text{cwnd}=i$
>- dopo 1 RTT ⟶ $\text{cwnd}=i+1$
>- dopo 2 RTT ⟶ $\text{cwnd}=i+2$
>- dopo 3 RTT ⟶ $\text{cwnd}=i+3$

#### fast recovery
**Fast recovery** è usata solo da alcune versioni di TCP (vedi sotto), come TCP Reno.

Funziona così:
- quando il mittente riceve **3 ACK duplicati**, entra in **fast retransmit** e ritrasmette subito il pacchetto mancante (senza aspettare il timeout).
- entra quindi in **fast recovery**, e:
	- `cwnd` viene dimezzata
		- invece di tornare alla slow start, **incrementa gradualmente `cwnd`** per ogni ACK duplicato ricevuto
- quando arriva un **ACK "nuovo"**, esce da fast recovery.

## tempo di RTT e timeout
>[!question] come impostare il valore del timeout di TCP?
>Il timeout deve essere più grande dell’RTT (o finirà prima di dare il tempo ai pacchetti di arrivare), ma non deve essere né troppo piccolo (avverrebbero ritrasmissioni non necessarie) né troppo grande (la reazione alla perdita di segmenti sarebbe troppo lenta).

>[!question] come stimare l'RTT?
>Per stimare l'RTT, si può utilizzare il `SampleRTT`: il tempo misurato *dalla trasmissione del segmento alla ricezione dell'ACK*
>-  ignora le ritrasmissioni, ed è un valore unico per più segmenti trasmessi insieme
>
>`SampleRTT` varia a causa di congestione nei router e carico nei sitemi terminali, quindi occorre fare degli accorgimenti per livellare la stima:
>- invece di prendere il valore corrente, si fa una *media* delle misure più recenti 

Per stimare l'RTT, si utlizza la **media mobile esponenziale ponderata**:
$$\text{EstimatedRTT$_{t+1}$ = ($1 -\alpha$)\;$\cdot\;$EstmatedRTT$_t + \alpha \cdot\;$SampleRTT$_{t+1}$} $$

- l'influenza delle misure passate decresce esponenzialmente
- valore tipico: $\alpha=0.125$ (con questo valore si assegna minore peso alle misure recenti rispetto a quelle più vecchie)

Il **timeout** è quindi $\text{EstimatedRTT}$ più un "margine di sicurezza", che cresce al crescere della variazione di $\text{EstimatedRTT}$.

Bisogna innanzitutto stimare di quanto $\text{SampleRTT}$ si discosta da $\text{EstimatedRTT}$:

$$\text{DevRTT}=(1-\beta) \cdot\text{DevRTT}+\beta \;\cdot \mid\text{SampleRTT}-\text{EstimatedRTT}\mid$$

- tipicamente, $\beta=0,25$

Per **impostare l'intervallo di timeout**:
- si imposta un valore iniziale pari a 1 secondo
- se avviene un timeout, si raddoppia
- appena viene ricevuto un segmento ed aggiornato $\text{EstimatedRTT}$, si usa la formula:

$$\text{TimeoutInterval}= \text{EstimatedRTT}+4 \cdot \text{DevRTT}$$

>[!example] esempio 
>
>![[sample-rtt.png|center|500]]


# versioni di TCP
## TCP Tahoe

- TCP Tahoe considera timeout e 3 ACK duplicati come congestione e riparte da 1 con $\text{ssthresh}=\frac{\text{cwnd}}{2}$

>[!info] FSM
>![[TCP-tahoe.png|center|500]]

>[!example] esempio 
>
>![[tcptahoe-es.png|center|500]]

## TCP Reno
Il meccanismo di TCP Tahoe può essere però affinato: l'arrivo di 3 ACK duplicati non è strettamente negativo, in quanto indica la capacità della rete di consegnare qualche segmento (infatti sono arrivati 3 pacchetti oltre a quello perso). Invece, un timeout prima di 3 ACK duplicati è più allarmante, perché significa che non sono arrivati neanche i pacchetti seguenti.
- si può quindi distinguere tra i due tipi di congestione e reagire in maniera più appropriata: TCP Reno implementa la "fast recovery"

TCP Reno si comporta quindi così:
 - se avviene un **timeout**, la congestione è "importante" ⟶ riparte da $1$
 - se riceve **3 ACK duplicati**, la congestione è lieve ⟶ applica la **fast recovery** a partire da $\text{ssthreshold}+3$

>[!info] FSM
> 
> ![[FSM-Reno.png|center|450]]


>[!example] esempio
> 
>![[TCPreno-es.png|center|500]]

