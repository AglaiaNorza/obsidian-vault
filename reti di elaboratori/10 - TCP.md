---
created: 2025-04-01
updated: 2025-04-10T10:06
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
>- in questo caso, il client richiede la chiusura della connessione in uscita, e il server risponde solo con un `ACK` ⟶ potrà continuare a mandare dati al client
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
| 2. arrivo **ordinato** di un segmento con numero di sequenza atteso; tutti i dati fino al numero di sequenza atteso sono già stati riscontrati | `ACK` viene ritardato (delayed). il destinatario attende fino a 500ms l’arrivo del prossimo segmento. se il segmento non arriva, invia un `ACK` (posticipato)<br>- `ACK` post |
| 3. arrivo ordinato di un segmento con numero di sequenza atteso; un altro segmento è in attesa di trasmissione dell’`ACK`                      | invia immediatamente un singolo `ACK` cumulativo, riscontrando entrambi i segmenti ordinati<br>- `ACK cum`                                                                    |
| 4. arrivo non ordinato di un segmento con numero di sequenza superiore a quello atteso; **viene rilevato un buco**                             | invia immediatamente un `ACK` duplicato, indicando il numero di sequenza del prossimo byte atteso (per indurre a **ritrasmissione rapida**)<br>- `ACK dup`                    |
| 5. arrivo di un segmento mancante (uno o più dei successivi è stato ricevuto)                                                                  | invia immediatamente un `ACK` (cumulativo)<br>- `ACK cum`                                                                                                                     |
| 6. arrivo di un segmento duplicato                                                                                                             | invia immediatamente un riscontro con numero di sequenza atteso<br>- `ACK dup`                                                                                                |

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
La congestione avviene se il **carico** della rete è superiore alla sua **capacità**. Il controllo della congestione fa sì che questo non avvenga.