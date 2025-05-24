---
created: 2025-04-01
updated: 2025-05-24T22:05
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

## switch
Uno switch è un dispositivo di livello collegamento che (al contrario dell'hub) svolge un **ruolo attivo**. Opera direttamente a livello di collegamento, filtrando e inoltrando i pacchetti Ethernet: esamina l'indirizzo di destinazione e lo invia all'interfaccia corrispondente.
- gli switch sono **trasparenti** agli host (questi non sono consapevoli della loro presenza)

![[switch.png|center|400]]

Gli switch consentono **più trasmissioni simultanee**: gli host hanno collegamenti dedicati e diretti con lo switch, che bufferizza i pacchetti.
- il protocollo Ethernet è usato su ciascun collegamento in entrata, ma non si verificano collisioni
- è una connessione full duplex

>[!summary] proprietà degli switch
>- sono dispositivi **plug-and-play**: non richiedono intervento dell'amministratore di rete o dell'utente
>- **elminano le collisioni**: bufferizzano i frame e non trasmettono più di un frame alla volta su ogni segmento di rete
>- **interconnettono link eterogenei**: collegamenti che operano a diverse velocità possono essere collegati ad uno switch
>- aumentano la **sicurezza** della rete e migliorano il **network management**: 
>	- (inviano ogni pacchetto solo alla porta corrispondente al dispositivo destinatario, quindi non è possibile utilizzare un packet sniffer per intercettare il traffico degli altri dispositivi in modo passivo <small>(perché lo switch non inoltra i pacchetti a tutte le porte)</small>)
>	- forniscono informazioni su uso di banda, collisioni, tipi di traffico ecc.
### apprendimento
Inizialmente gli switch venivano configurati staticamente, ma ora c'è un meccanismo dinamico di **auto-apprendimento**, basato su una tabella dinamica associa automaticamente gli indirizzi MAC alle porte.

Lo switch apprende quali nodi possono essere raggiunti attraverso determinate interfacce
- quando riceve un pacchetto, "impara" l'indirizzo del mittente e registra la coppia mittente/interfaccia nella sua tabella di commutazione
-  quando deve inoltrare un frame, se la destinazione è ignota si usa il *flooding*, mentre se è nota il *selective send*


# ethernet standard
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
3) **collision detection**
	- verifica, durante la trasmissione, la presenza di eventuali segnali provenienti da altre NIC; se non ne rileva, considera il pacchetto spedito
4) **jamming**
	- se rileva segnali da altre NIC, interrompe immediatamente la trasmissione del pacchetto e invia un segnale di disturbo (jam) di 48 bit per avvisare della collisione tutte le altre NIC che sono in fase trasmissiva 
5) **backoff esponenziale**
	- la NIC rimane in attesa; quando rileva la $n$-esima collisione consecutiva, stabilisce un valore $k \in \{ 0,\,1,\,\dots,\,2^m-1 \}$ con $m=min(n,\,10)$, aspetta un tempo pari a $k$ volte 512 bit e ritorna al passo 2
	- la NIC prova a stimare quanti sono gli adattatori coinvolti (se sono numerosi, il tempo di attsa potrebbe essere lungo) (ad ogni collisione, il range da cui scegliere $k$ cresce)

# fast ethernet
Ethernet standard si è evoluta a **fast ethernet** (100Mbps), mantenendo la retrocompatibilità e mantenendo invariato il sottolivello MAC (compresi formato e dimensione dei frame).

>[!question] CSMA/CD e fast ethernet
> Il funzionamento corretto di CSMA/CD dipende dalla *velocità di trasmissione*, dalla *dimensione minima del frame* e dalla *lunghezza massima della rete*. Visto che con il fast ethernet la trasmissione è 10 volte più veloce mentre il frame rimane lungo 512 bit, le collisioni devono essere rilevate 10 volte più velocemente, quindi la rete deve essere **10 volte più corta**.
> 
> 1) <u>**prima soluzione**</u>
> 
> Una prima soluzione per integrare CSMA/CD e fast ethernet è quella di utilizzare un hub passivo con topologia a stella (tutti i dispositivi sono collegati a un punto centrale), ma con dimensione massima della rete fissata a 250 metri invece che 2500 della versione standard.
> 
> L'hub è un dispositivo che opera a livello fisico sui **singoli bit**.
> - all'arrivo di un bit, l'hub lo riproduce incrementandone l'energia e lo trasmette attraverso tutte le sue altre interfacce
> - ripete il bit entrante su tutte le interfacce uscenti anche se se c'è già un segnale
> - trasmette in broadcast, quindi ciascuna NIC può sondare il canale per verificare se è libero e rilevare una collisione mentre trasmette
> 
> ![[csma-ethernet-hub.png|center|350]]
> 
> 2) <u>**seconda soluzione**</u>
> 
> Si utilizza uno **switch di collegamento dotato di buffer** per memorizzare i frame e **connessione full duplex** (permette la comunicazione simultanea in entrambe le direzioni) per ciascun host.
> - il mezzo trasmissivo è privato per ciascun host e non c'è bisogno di usare CSMA/CD visto che *gli host non sono più in competizione*
> - lo switch riceve un frame da un host, lo memorizza nel buffer, verifica l'indirizzo di destinazione e invia il frame attraverso l'interfaccia corrispondente
> - il singolo mezzo condiviso diventa molti mezzi punto-punto
> 

# gigabit ethernet
Il gigabit ethernet è la versione successiva al fast Ethernet. Ha una topologia a stella con switch (quindi non ci sono collisioni), e permette di arrivare fino a 10Gbps

# VLAN
Le LAN virtuali sono **reti locali** configurate per mezzo del **software** invece che del cablaggio fisico.
- una LAN viene suddivisa in **segmenti logici** anziché fisici, e può essere suddivisa in più VLAN
- il gruppo di appartenenza è definito dal software

![[VLAN.png|center|450]]

Il management software dello switch permette all’amministratore di rete di dichiarare quali porte appartengono a una data LAN (lo switch mantiene una tabella di associazioni porta-VLAN).

### VLAN trunking
Esiste una porta speciale su ogni switch che viene configurata come **porta trunk**, una porta che può interconnettere due switch (anche in due edifici diversi). La porta trunk appartiene ad **entrambe le VLAN** e riceve i frame indirizzati ad entrambe.

![[VLAN-trunking.png|center|450]]