---
created: 2025-04-01
updated: 2025-05-24T12:09
---
>[!info]- standard IEEE 802
>IEEE ha prodotto diversi standard per le LAN (collettivamente noti come IEEE 802), che includono:
> - specifiche generali del progetto (802.1)
> - logical link control (LLC, 802.2)
> - CSMA/CD (802.3)
> - token bust (802.4, destinato a LAN per automazione industriale)
> - token ring (802.5)
> - DQDB (802.6, destinato alle MAN)
> - WLAN (802.11)
> 
> I vari standard differiscono a livello fisico e nel sottolivello MAC, ma sono **compatibili a livello data link**.

Ethernet è la tecnologia di rete che consente la comunicazione tra dispositivi in una LAN, e detiene una posizione dominante nel mercato delle LAN cablate (è stata la prima LAN cablata ad alta velocità con vasta diffusione).

![[ethernet-standard.png|center|450]]

L'ethernet standard è **connectionless** (non è prevista nessuna forma di handshaking preventiva prima di inviare un pacchetto) e **non affidabile**: la NIC (scheda di rete) ricevente non invia un riscontro.

### formato dei frame

>[!info] frame
>![[frame-ethernet.png|center|550]]
> - `Preambolo` ⟶ 7 byte con valore `10101010`: servono per **attivare le NIC** dei riceventi e **sincronizzare** i loro orologi con quello del trasmittente (fa parte dell'header a livello fisico)
> - `SFD` (Start Frame Delimiter) ⟶ 1 byte con valore `10101011`: definisce l'**inizio del frame** (è l'ultima possibilità di sincronizzazione); gli ultimi due bit (`11`) indicano che inizia l'header MAC
> - `Indirizzi sorgente e destinazione` ⟶ 6 byte; quando una NIC riceve un pacchetto contenente il proprio indirizzo di destinazione o l'indiriizo broadcast, **trasferisce il contenuto** del campo dati del pacchetto a **livello di rete** (i pacchetti con altri indirizzi MAC vengono ignorati)
> - `Tipo` ⟶ 2 byte usati per **multiplexing e demultiplexing**: indicano il protocollo di livello superiore del pacchetto incapsulato nel frame
> - `Dati`  ⟶ da 46 a 1500 byte; contiene il **datagramma di rete**; se è inferiore alla dimensione minima, viene riempito di zeri fino a raggiungere 46 byte
> - `CRC` ⟶ consente alla NIC ricevente di **rilevare la presenza di un errore** nei bit sui campi indirizzo, tipo e dati
> 
> compresi i 18 byte di intestazione e trailer, la lunghezza minima del frame è di 64 byte (necessaria per il corretto funzionamento del CSMA/CD), mentre la lunghezza massima del frame è di 1518 byte (necessaria per evitare che una stazione possa monopolizzare il mezzo e per ragioni storiche <small>(la memoria era molto costosa e permetteva di ridurre la memoria necessaria nei buffer dei dispositivi)</small>)

### indirizzi
Tutte le stazioni che fanno parte di una ethernet sono dotate di una **Network Interface Card** (NIC, scheda di rete), che fornisce un **indirizzo di rete livello collegamento**. Gli indirizzi vengono trasmessi byte per byte da sinistra verso destra, ma per ciascun byte il LSB viene inviato per primo e il MSB per ultimo.

### fasi operative del protocollo CSMA/CD
[ [[19 - livello di collegamento#CSMA|CSMA/CD]] ]

1) **framing**
	- la NIC riceve un datagramma di rete dal nodo a cui è collegato e prepara un frame ethernet
2) **carrier sense e trasmissione**
	- misura il livello di energia sul mezzo trasmissivo per un periodo di tempo e, se il canale è inattivo, inizia la trasmissione; se il canale risulta occupato, resta in attesa fino a quando non rileva più il segnale (e trasmette)
3) **collision detection**'
4) **jamming**
5) **backoff esponenziale**