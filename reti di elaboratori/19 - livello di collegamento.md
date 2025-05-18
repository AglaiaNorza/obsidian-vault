---
created: 2025-04-01
updated: 2025-05-18T18:44
---
La comunicazione a livello di collegamento è **hop-to-hop** o nodo-to-nodo.
- host e router sono chiamati **nodi** o **stazioni**
- i canali di comunicazione che collegano nodi adiacenti sono i **link**, e possono essere cablati o wireless
- le unita di dati scambiate dai protocolli a livello di link sono chimate **frame**

![[livello-collegamento.png|center|500]]

>[!tip] i **protocolli** a livello di collegamento si occupano del trasporto di datagrammi lungo un **singolo canale di comunicazione**

## link
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

### errori 
Gli errori sono dovuti a **interferenze** che possono cambiare la forma del segnale.
