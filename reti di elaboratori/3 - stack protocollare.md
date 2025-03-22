> [!info] protocollo
> Un **protocollo** definisce le regole che il mittente, il destinatario e tutti i sistemi intermedi coinvolti devono rispettare per essere in grado di comunicare.

In alcune situazioni, è opportuno suddividere i compiti fra più livelli (layer) - questo permette di suddividere un compito complesso in più compiti semplici, e permette la **modularizzazione** (indipendenza dei livelli).

- ogni modulo/livello può essere considerato come un black box, senza preoccuparsi delle modalità con cui i dati vengono processati e prodotti
- si **separano i servizi dalla loro implementazione**: un livello usa servizi dal livello inferiore, e offre servizi al livello superiore
- se due macchine forniscono lo stesso output  dallo stesso input, possono essere considerati *equivalenti* 

Talvolta è richiesta una **comunicazione bidirezionale**: ciascun livello deve essere capace di effettuare i due compiti opposti, uno per ciascuna direzione (per esempio crittografare e decrittografare).

I livelli sono *direttamente collegati*, ovvero il protocollo implementato a ciascun livello specifica una comunicazione diretta tra i **pari livelli** delle due parti.

## stack protocollare TCP/IP
(Lo stack protocollare prende il nome di TCP/IP perché TCP e IP sono i due protocolli più importanti).

La rete è organizzata come una pila di **strati** (layer) o **livelli**, costruiti l'uno sull'altro. Ogni livello offre servizi agli strati di livello superiore, nascondendo i dettagli di implementazione.

- strati dello stesso livello di computer diversi sono in comunicazione tra di loro, attraverso i **protocolli**
- le entità che formano gli strati sono chiamati **pari** (peer)

La pila TCP/IP era originariamente definita in termini di quattro livelli software + un livello hardware, ma è oggi intesa come composta di cinque livelli.

![[TCPIP-liv.png|center|500]]

### livello applicazione

- sede delle applicazioni di rete
- usa i protocolli: HTTP, SMTP, FTP, DNS
- i pacchetti sono chiamati *messaggi*

Il livello applicazione fornisce **servizi** all'utente.
La comunicazione è fornita per mezzo di una **connessione logica**: i livelli applicazione ai due lati della comunicazione agiscono come se esistesse un collegamento diretto bidirezionale attraverso il quale poter inviare e ricevere messaggi.

![[app-lvl.png|center|400]]

- la comunicazione reale avviene attraverso più livelli e dispositivi, e vari canali fisici

Il livello applicazione è molto flessibile, e consente di aggiungere nuovi protocolli con estrema facilità senza modificare gli altri livelli. Ogni protocollo aggiunto ad un dato livello deve essere progettato in modo da usare servizi del livello inferiore.
#### protocolli standard
A livello applicazione esistono diversi protocolli standardizzati e documentati dagli enti responsabili della gestione di Internet. Ogni protocollo standard è costituito da una coppia di programmi che interagiscono con l'utente e con il livello di trasporto per fornire uno specifico servizio.
- per esempio, un'applicazione web è specificata dal protocollo HTTP
#### protocolli non standard
È possibile creare un'applicazione non standard scrivendo due programmi che forniscono servizi agli utenti (facendo uso dei servizi di trasporto) senza dover chiedere autorizzazioni.

#### creare un'applicazione di rete
>[!example]- alcune applicazioni di rete
>- posta elettronica
>- web
>- messaggistica istantanea
>- condivisione di file P2P
>- SSH
>- giochi multiutente via rete
>- streaming
>- telefono via internet
>- videochiamate

Per creare un'applicazione di rete è necessario scrivere programmi che 
- girino su sistemi terminali diversi
- comunichino attraverso la rete
- funzionino su più macchine e siano indipendenti dalla tecnologia che c'è sotto

#### architettura dell'applicazione
Esistono tre diversi paradigmi per la gestione dei servizi:
- i due programmi devono essere entrambi in grado di richiedere e offrire servizi (**peer-to-peer**)
- ciascuno dei due programmi deve occuparsi di uno dei due compiti(**client-server**)
- architetture ibride (**client-server E p2p**)

##### paradigma client-server
Il ruolo delle due entità è totalmente differente: non è possibile eseguire un client come programma server e viceversa. Infatti

- il **client** --> *richiede* i servizi, e va in esecuzione solo quando il servizio è necessario (di solito ci sono numerosi client che richiedono i servizi)
- il **server** --> è il *fornitore* dei servizi, ed è sempre in esecuzione, in attesa di richieste dal client (c'è un numero limitato di processi server pronti ad offrire uno specifico servizio)

[ da finire ]
### altri livelli

**Trasporto** --> trasferimento dei messaggi dal livello applicazione di un client a quello di un server
- protocolli: TCP affidabile, UDP non affidabile (l'affidabilità fa riferimento a correttezza e ordine di arrivo)
- i pacchetti sono chiamati *segmenti*

**Rete** --> instradamento dei segmenti dall'origine alla destinazione
- IP, protocolli di instradamento
- pacchetti: *datagrammi*

**Link** (hardware) --> trasmissione di datagrammi da un nodo a quello successivo sul percorso
- Ethernet, Wi-Fi, PPP (lungo un percorso sorgente-destinazione, un datagramma può essere gestito da protocolli diversi)
- pacchetti: *frame*

**Fisico** --> trasferimento dei singoli bit

>[!tip] comunicazione in una internet
>
>![[internet-comm.png|center|400]]
>
>- grazie al layering, i sistemi implementano solo i livelli necessari, riducendo la complessità
>- nel router, ci possono essere fino a $n$ livelli fisico-collegamento, con $n$ numero di link a cui il router è collegato
>- invece, poiché le porte dello switch sono omogenee, c'è un solo protocollo




**rete**: instradamento dei segmenti dall'origine alla destinazione (trova la rotta)
- i pacchetti trasmessi si chiamano *datagrammi*


L'ultimo livello è il livello fisico: trasferimento fisico dei bit lungo un canale di comunicazione

(switch sposta informazioni all'interno di una lan(rete), router collega reti)





visto che le porte dello switch sono omogenee, c'è solo un protocollo.


un protocollo non affidabile è più veloce


