---
created: 2025-04-01
updated: 2025-06-21T10:10
---
La comunicazione a livello di collegamento è **hop-to-hop** o nodo-to-nodo.
- host e router sono chiamati **nodi** o **stazioni**
- i canali di comunicazione che collegano nodi adiacenti sono i **link**, e possono essere cablati o wireless
- le unita di dati scambiate dai protocolli a livello di link sono chimate **frame**

![[livello-collegamento.png|center|500]]

>[!tip] i **protocolli** a livello di collegamento si occupano del trasporto di datagrammi lungo un **singolo canale di comunicazione**

# link
I nodi all'interno di una rete sono fisicamente collegati da un mezzo trasmissivo come un cavo o l'aria.

È possibile utilizzare:
- l'intera capacità del mezzo ⟶ **collegamento punto-punto**, dedicato a due soli dispositivi
	- usato da connessioni telefoniche o ethernet-host
	- si usa il **point-to-point protocol** (PPP) <small>(Pier Paolo Pasolini)</small>
- solo una parte del mezzo ⟶ **collegamento broadcast**, condiviso tra varie coppie di dispositivi

Un datagramma può essere gestito da diversi protocolli quando si trova su collegamenti diversi (es. da Ethernet su un collegamento, poi da PPP su un altro). Anche i servizi erogati dai protocolli del livello di link possono essere diversi (ad esempio, non tutti i protocolli forniscono un servizio di consegna affidabile).

>[!question] dove è implementato il livello di collegamento
>
>Il livello di collegamento è implementato in tutti gli host, ed è realizzato in un adattatore chiamato **Network Interface Card** (NIC), che implementa il livello di collegamento e il livello fisico
>- un esempio è la scheda Ethernet
>
>È una combinazione di hardware, software e firmware.

## servizi offerti dal livello di collegamento
- **framing** ⟶ i protocolli **incapsulano** i datagrammi del livello di rete all'interno di un frame a livello link per separare i vari messaggi durante la trasmissione
	- per identificare origine e destinatario vengono usati MAC addresses
- **consegna affidabile** ⟶ è basata su **ACK** 
	- non viene utilizzata se un collegamento presenta un basso numero di errori sui bit (es. fibra ottica, cavo coassiale), mentre è usata nei collegamenti soggetti ad elevati tassi di errore (es. wireless)
- **controllo del flusso** ⟶ evita che il nodo trasmittente saturi quello ricevente
- **rilevazione degli errori** ⟶ il nodo ricevente individua la presenza di errori (causati dalle interferenze) grazie all'inserimento da parte del nodo trasmittente di **bit di controllo** di errore 
- **correzione degli errori** ⟶ il nodo ricevente determina il punto in cui si è verificato un errore e lo corregge

>[!summary] adattatori
>
>![[adattatori-link.png|center|350]]
>
>durante la comunicazione:
>- il lato mittente:
>	- incapsula un datagramma in un frame
>	- imposta i bit rilevazione degli errori, trasferimento dati affidabile, controllo di flusso, etc.
>- il lato ricevente:
>	- individua errori, trasferimento dati affidabile, controllo di flusso, etc.
>	- estrae i datagrammi e li passa al nodo ricevente

>[!info] sottolivelli
>Il livello di collegamento ha due ulteriori sottolivelli:
>- **Data-Link Control** (DLC)
>
>Si occupa delle questioni *comuni* ai collegamenti punto-punto e a quelli broadcast:
>- framing
>- controllo di errori e di flusso
>- rilevamento e correzione degli errori
>
>e delle procedure di comunicazione nodo-a-nodo (indipendentemente dal fatto che il collegamento sia dedicato o broadcast).
>
>- **Media Access Control** (MAC)
>
>Si occupa degli aspetti specifici dei *canali broadcast*, come il controllo dell'accesso al mezzo condiviso

# errori 
Gli errori sono dovuti a **interferenze** (o "rumori") che possono cambiare la forma del segnale, e si dividono in due categorie:
- **errori sul singolo bit**
- **errori a burst** (raffica)

La durata di un'interferenza è tipicamente più lunga di quella di un singolo bit, quindi la probabilità che avvenga un errore di tipo burst è più elevata.
- Il numero di bit coinvolti dipende dalla *velocità di trasferimento* dati e dalla *durata* del rumore

>[!example]- esempi
>
>![[errore-bit.png|center|400]]
>
>![[errore-burst.png|center|400]]

### tecniche di rilevazioni degli errori
La rilevazione degli errori si basa sull'aggiunta di alcuni **bit EDC** (Error Detection and Correction), e non è attendibile al 100%. Per questo, le tecniche più sofisticate prevedono un'elevata ridondanza.

![[EDC.png|center|400]]

#### controllo di parità
Viene utilizzato anche un controllo sulla **parità**: si inserisce un bit aggiuntivo, il cui valore viene selezionato in modo da rendere pari il numero totale di $1$ all'interno ella codeword.
- con un unico bit di parità si può solo controllare se si è verificato almeno un errore in un bit
- tramite la **parità bidimensionale**, si può individuare e correggere il bit alterato

>[!example] parità bidimensionale
>
>![[parita-bidimensionale.png|center|400]]

# protocolli di accesso multiplo
Quando si utilizza un canale broadcast condiviso, centinaia o migliaia di nodi possono comunicare direttamente su un canale broadcast. Non è quindi raro che i nodi ricevano *due o più frame contemporaneamente*, generando una **collisione**.

I **protocolli di accesso multiplo** permettono di limitare il caos e realizzare una condivisione di canale, fissando le modalità con cui i nodi regolano le loro trasmissioni sul canale condiviso. 
- la comunicazione relativa al canale condiviso avviene sul canale stesso (non ce n'è un altro "out of band")

>[!info] protocolli di accesso multiplo ideali
>
>A livello ideale, se si ha un canale broadcast con velocità di $R$ bps, si vuole che:
>- se solo un nodo deve inviare dati, esso disponga di un tasso trasmissivo pari a $R$bps
>- se $M$ nodi devono inviare dati, il canale sia *diviso equamente* tra questi (quindi che ognuno abbia un tasso trasmissivo di $\frac{R}{M}$bps)
>
>Un protocollo di accesso multiplo ideale è *decentralizzato*: non ci sono nodi master e non c'è sincronizzazione dei clock.
>

I protocolli di accesso multiplo si possono classificare in una di queste tre categorie:
- **protocolli a suddivisione del canale** (channel partitioning)  ⟶ si suddivide un canale in parti più piccole (slot di tempo, frequenza ecc), che vengono allocate ad un nodo per utilizzo esclusivo
	- si evitano sicuramente le collisioni
- **protocolli ad accesso casuale** (random access)
	- i canali non vengono divisi, quindi si può verificare una collisione ⟶ i nodi coinvolti ritrasmettono ripetutamente i pacchetti
- **protocolli a rotazione** (taking-turn) ⟶ ciascun nodo ha il suo turno di trasmissione; i nodi che hanno molto da trasmettere possono avere turni più lunghi

![[prot-acc-mul.png|center|450]]

## protocolli a suddivisione del canale
### TDMA
Il protocollo TDMA (Time Division Multiple Access) [vedi anche [[1 - introduzione alle reti#suddivisione della rete|TDM]]] permette l'accesso multiplo a **divisione di tempo**.

Ogni nodo ha un *turno* assegnato per accedere al canale, che è diviso in intervalli di tempo.
- gli slot non usati *rimangono inattivi*

Il difetto principale del TDMA è il fatto che **non è flessibile** rispetto a variazioni nel numero di nodi (quindi la banda non viene utilizzata appieno).
### FDMA
Il protocollo FDMA (Frequency Division Multiple Access) [vedi anche [[1 - introduzione alle reti#suddivisione della rete|FDM]]] suddivide il canale in **bande di frequenza**.

A ciascuna stazione è assegnata una banda di frequenza prefissata.
- il tasso trasmissivo per ognuno degli $N$ nodi è $\frac{R}{N}$bps

## protocolli ad accesso casuale
Quando si utilizzano protocolli ad accesso casuale, **nessuna stazione ha il controllo** sulle altre. Ogni volta che una stazione ha dei dati da inviare, usa una procedura definita dal protocollo per decidere se spedire o meno. 
- non c'è un tempo programmato nel quale la stazione deve trasmettere
- non c'è una regola specifica che permette di sapere quale sarà la prossima stazione che trasmetterà

Le stazioni si **contendono il canale**, ovvero competono l'una con l'altra per accedere al mezzo trasmissivo. 

Poiché le collisioni sono possibili, un protocollo ad accesso casuale deve definire **come rilevarle** e **come ritrasmettere** nel caso si sia verificata una collisione.

### ALOHA
Il protocollo **ALOHA** è il primo metodo di accesso casuale ad essere stato proposto in letteratura. È stato ideato <small> all'università delle Hawaii nei primi anni '70</small> per mettere in comunicazione diversi atolli mediante una LAN radio.

Ogni stazione può inviare un frame tutte le volte che ha dati da inviare. Il ricevente invia un `ACK` per notificare la corretta ricezione del frame ⟶ se il mittente non riceve `ACK` entro un **timeout**, deve *ritrasmettere*.

Se due stazioni ritrasmettono di nuovo contemporaneamente e avviene un'altra collisione, si **attende un tempo random** (*back-off*) (la casualità aiuta ad evitare altre collisioni) prima di effettuare la ritrasmissione. Dopo un numero massimo di tentativi $K_{\text{max}}$, una stazione interrompe i suoi tentativi e riprova più tardi.

>[!example] esempio 
>
>![[ALOHA-es.png|center|450]]

>[!summary] timeout e backoff
>Il periodo di **timeout** equivale al **massimo ritardo di propagazione di round-trip tra le due stazioni più lontane**.
>
>$$
>\text{timeout}=2 \times T_p
>$$
>
>Il **tempo di back-off** è un valore scelto casualmente che **dipende dal numero $K$ di trasmissioni fallite**.
>
>$$
>\text{backoff}=R\cdot T_{\text{fr}}
>$$
>
>dove:
>- $R\in[0,\,2^k-1]$, 
>- $T_{\text{fr}}=\text{tempo x inviare un frame}$
> 
> e con massimo di tentativi $K_{max}=15$

>[!example] esempio: calcolo di backoff
>
>Le stazioni in una rete wireless ALOHA sono a una distanza massima di 600km. Supponendo che i segnali si propaghino a $3 \times 10^8\text{m/s}$, troviamo che
>$$
>T_{\text{fr}} = \frac{600 \times 10^3}{3 \times 10^8} = 2ms
>$$
>
>per $K=2$, l'intervallo di $R$ è $\{ 0,\,1,\,2,\,3 \}$ - ciò significa che $T_{B}=R \times T_{\text{fr}}$ può essere 0, 2, 4 o 6 ms sulla base del risultato della variabile casuale $R$.

#### ALOHA puro
Il protocollo ALOHA puro ha elevate probabilità di collisione, in quanto il **tempo di vulnerabilità** (l'intervallo di tempo nel quale il frame è a rischio di collisioni) è $2T_{\text{fr}}$ (il frame trasmesso a tempo $t$ si sovrappone con la trasmissione di qualsiasi frame inviato in $[t-1,t+1]$)

![[alohapuro-vul.png|center|450]]

>[!example] efficienza
>Assumendo che tutti i frame abbiano la stessa dimensione e ogni nodo abbia sempre un frame da trasmettere:
>- in ogni istante di tempo, $p$ è la probabilità che un nodo trasmetta un frame (e $(1-p)$ che non trasmetta)
>- supponendo che un nodo inizi a trasmettere al tempo $t_{0}$, perché la trasmissione vada a buon fine, nessun altro nodo deve aver iniziato la trasmissione nel tempo $[t_{0}-1,\,t_{0}]$ (probabilità data da $(1-p)^{N-1}$), e allo stesso modo nessun nodo deve iniziare a trasmettere nel tempo $[t_{0},\,t_{0}+1]$ (evento che ha la stessa probabilità)
>- la probabilità che trasmetta con successo è quindi $p(1-p)^{2(N-1)}$
>
>Studiando il valore di $p$ per $N$ che tende ad infinito, si ottiene che l'efficienza massima è $\frac{1}{2e}\approx 0,18$ (bassa)

#### slotted ALOHA
Un modo per aumentare l'efficienza di ALOHA consiste nel  **dividere il tempo in intervalli discreti**, ciascuno corrispondente ad un frame time ($T_{\text{fr}}$).

I nodi si mettono d'accordo nei confini tra gli intervalli facendo emettere da una attrezzatura speciale un breve segnale all'inizio di ogni intervallo.

>[!tip] assunzioni
>Si assume che:
>- tutti i pacchetti abbiano la stessa dimensione
>- il tempo sia diviso in **slot**, in cui ogni slot equivale al **tempo di trasmissione di un pacchetto**
>- i nodi inizino la trasmissione dei pacchetti solo all'inizio degli slot
>- i nodi siano **sincronizzati**
>- se in uno slot due o più pacchetti collidono, i nodi coinvolti rilevino l'evento prima del termine dello slot

Quando ad un nodo arriva un nuovo pacchetto da spedire, questo attende quindi l'inizio del prossimo slot. 
- **Se non si verifica una collisione** ⟶ il nodo può trasmettere un nuovo pacchetto nello slot successivo
- **Se si verifica una collisione** ⟶ il nodo ritrasmette con *probabilità p* il suo pacchetto durante gli slot successivi

| **pros**                                                                                            | **cons**                                                         |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| consente a un singolo nodo di trasmettere continuammente pacchetti alla massima velocità del canale | una frazione degli slot presenterà collisioni e andrà "sprecata" |
| il tempo di vulnerabilità si riduce ad un solo slot ($T_{\text{fr}}$)                               | un'altra frazione degli slot rimarrà vuota e quindi inattiva     |

>[!example] efficienza
>Supponiamo ci siano $N$ nodi e che ognuno trasmetta i pacchetti in uno slot con probabilità $p$.
>- la probabilità di successo di un dato nodo è $p(1-p)^{N-1}$
>- poiché ci sono $N$ nodi, la probabilità che ogni nodo abbia successo è $Np(1-p)^{N-1}$
>
>L'efficienza chhe si ottiene per un elevato numero di nodi è data dal limite di $\lim_{ N \to \infty }Np^*(1-p^*)^{N-1}=\frac{1}{e}\approx 0,37$.
>
>Quindi, nel caso migliore, solo il 37% degli slot compie lavoro utile.

### CSMA
Nel protocollo CSMA (Carrier Sense Multiple Access, accesso multiplo a rilevazione della portante), un  nodo **si pone in ascolto prima di trasmettere** (listen before talk/sense before transmit); se rileva che il canale è libero, trasmette l'intero pacchetto. Se invece sta già trasmettendo, **aspetta** un altro intervallo di tempo.

Ma le collisioni possono ancora verificarsi: il **ritardo di propagazione** può far sì che due nodi non rilevino la reciproca trasmissione: esiste quindi un **tempo di vulnerabilità**, che corrisponde al tempo di propagazione.

#### CSMA/CD
CSMA/Collision Detection permette di **rilevare le collisioni** ascoltando il canale anche *durante la trasmissione*. Le collisioni vengono rilevate in poco tempo, e la trasmissione viene annullata non appena si accorge di un'altra trasmissione in corso.

>[!tip] La rilevazione di collisioni è facile nelle LAN cablate e difficile nelle LAN wireless.

>[!example]- esempio
>
>![[csma-cd.png|center|500]]

>[!info] dimensione minima del frame
> Perché il Collision Detection funzioni, il mittente deve poter rilevare la trasmissione *prima di trasmettere l'ultimo bit del frame* (una volta inviato un frame, una stazione non ne tiene una copia né controlla il mezzo trasmissivo per rilevare collisioni). 
> 
> Il tempo di trasmissione di un frame deve quindi essere almeno due volte il tempo di propagazione $T_{p}$ (quindi la prima stazione deve essere ancora in trasmissione dopo $2T_{p}$).

>[!example] esempio 
>Una rete che utilizza CSMA/CD ha un rate di $10\text{mbps}$. Se il tempo di propagazione massimo è $25,6\mu s$, qual è la dimensione minima del frame?
>
>Il tempo di trasmissione minimo del frame è:
>
>$$
>T_{\text{fr}}=2 \times T_{p} = 51.2\mu s
>$$
>
>quindi, nel peggiore dei casi, una stazione deve trasmettere per $51,2\mu s$ per poter rilevare la collisione.
>
>La dimensione minima del frame è quindi:
>
>$$
>10\text{Mbps} \times 51,2\mu s = 512\text{bit} = 64 \text{byte}
>$$

#### metodi di persistenza
Ci sono diversi metodi di persistenza per i nodi.


|                                              | **non persistente**                                                   | **1-persistente**                                    | **p-persistente**                                             |
| -------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------- |
| cosa fa un nodo se trova il canale libero?   | trasmette subito                                                      | trasmette subito                                     | trasmette con probabilità p                                   |
| cosa fa un nodo se trova il canale occupato? | desiste e riascolta dopo un tempo random (carrier sense a intervalli) | rimane in ascolto finché il canale non si è liberato | backoff: attesa di un tempo random e nuovo ascolto del canale |
| se c'è collisione                            | backoff                                                               | backoff                                              | backoff                                                       |

![[non-pers.png|center|450]]

![[1-pers.png|center|450]]


![[p-pers.png|center|550]]


>[!example]  efficienza CSMA/CD
>Quando un solo nodo trasmette, può trasmettere al massimo rate; quando più nodi trasmettono, il throughput è minore.
>
>Il throughput del CSMA/CD è maggiore di quello dell'ALOHA (sia puro che slotted).
>
>Per il metodo 1-persistente, il throughput massimo è del 50%.

## protocolli MAC a rotazione
I protocolli a rotazione cercano un **compromesso** tra quelli a suddivisione del canale e quelli ad accesso casuale.
#### polling
Nel protocollo **polling**, un nodo principale (master) sonda **a turno** gli altri (slave) per eliminare le collisioni e gli slot vuoti, e decidere chi può trasmettere in quale momento
- in particolare interroga uno alla volta ogni nodo: se il nodo ha dati da inviare, li invia, e il master passa al nodo successivo
- può interrogare i nodi in modo equo (round robin) o rispettando delle prorità

>[!warning] se il nodo principale si guasta, l'intero canale resta inattivo

- il protocollo di polling genera overhead perché si interrogano anche stazioni che non hanno dati da inviare


#### token-passing
Nel protocollo **token-passing**, un **messaggio di controllo** (token) circola fra i nodi seguendo un ordine prefissato.
- una stazione che riceve il token può inviare dati e passerà poi il token alla stazione successiva

È un protocollo decentralizzato e altamente efficiente, ma il guasto di un nodo può mettere fuori uso l'intero canale.