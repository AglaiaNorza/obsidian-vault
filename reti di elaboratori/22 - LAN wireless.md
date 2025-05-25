---
created: 2025-04-01
updated: 2025-05-25T16:03
---
Le reti wireless si dividono in:
- LAN wireless, disponibili in campus, uffici, bar, aree pubbliche
- reti cellulari
- bluetooth
- reti di sensori, RFID, smart objects

>[!example] alcuni standard
>
>![[wireless-standard.png|center|450]]
>
>Quello più usato è lo standard IEEE, con le sue diverse versioni:
>
> | Protocol | Release date | Freq.     | Rate (typical) | Rate (max) | Range (indoor) |
> | -------- | ------------ | --------- | -------------- | ---------- | -------------- |
> | Legacy   | 1997         | 2.4 GHz   | 1 Mbps         | 2 Mbps     | ?              |
> | 802.11a  | 1999         | 5 GHz     | 25 Mbps        | 54 Mbps    | ~30 m          |
> | 802.11b  | 1999         | 2.4 GHz   | 6.5 Mbps       | 11 Mbps    | ~30 m          |
> | 802.11g  | 2003         | 2.4 GHz   | 25 Mbps        | 54 Mbps    | ~30 m          |
> | 802.11n  | 2008         | 2.4/5 GHz | 200 Mbps       | 540 Mbps   | ~50 m          |

# LAN wireless
## elementi 

![[network-infrastructure.png|center|350]]

Una LAN wireless è composta da:
- **wireless hosts** ⟶ usati per eseguire applicazioni; possono essere fissi o mobili
- **base stations** ⟶ sono dei *relay* (ripetitori) tipicamente connessi a reti cablate, che si occupano di mandare pacchetti tra reti cablate e host wireless nella loro area
- **wireless links** ⟶ tipicamente usati per connettere gli host alle base station, ma possono anche essere usati come collegamenti per il backbone; variano in data rate e distanza di trasmissione
	- i [[19 - livello di collegamento#protocolli di accesso multiplo|protocolli di accesso multiplo]] regolano l'accesso ai lnink


> [!summary] caratteristiche
> - Il mezzo trasmissivo delle LAN wireless è l'**aria** (mezzo condiviso dagli host della rete), e il segnale è **broadcast**. 
> - Un **host wireless** non è fisicamente connesso alla rete e può muoversi liberamente.
> - La **connessione ad altre reti** avviene mediante una stazione base detta **Access Point** (AP), che collega l'ambiente wireless a quello cablato.


> [!error] migrazione da ambiente cablato a wireless
> Il funzionamento di una rete cablata o wireless dipende dai livelli di collegamento e fisico. Per migrare da rete cablata a wireless basta *cambiare le schede di rete* e *sostituire lo switch di collegamento con un AP* (gli indirizzi MAC cambieranno, ma gli IP resteranno gli stessi).

## reti ad hoc
Le reti ad hoc sono insieme di host che si **auto-organizzano** per formare una rete e **comunicano liberamente** tra di loro.
- Ogni host deve eseguire le funzionalità di rete (network setup, routing, forwarding ecc)

##  link wireless
### caratteristiche
Alcune delle caratteristiche più importanti dei link wireless sono:
- **attenuazione del segnale** ⟶ la forza dei segnali elettromagnetici diminuisce rapidamente all'aumentare della distanza dal trasmettitore (il segnale si disperde in tutte le direzioni)
- **propagazione multi-path** ⟶ quando un'onda radio trova un ostacolo, viene riflessa (completamente o in parte) con una perdita di potenza - un segnale può quindi arrivare ad una stazione, tramite riflessi successivi, attraverso percorsi multipli 
- **interferenze** ⟶ le interferenze possono arrivare:
	- dalla **stessa sorgente**: un destinatario può ricevere più segnali dal mittente desiderato a causa del multipath
	- da **altre sorgenti**: se altri trasmettitori stanno usando la stessa banda di frequenza per comunicare con altri destinatari

### errori 
Le caratteristiche dei link wireless causano errori. Il tasso di errore è misurato con il **Signal to Noise Radio** (SNR o rapporto segnale-rumore), che misura il rapporto tra il segnale buono e il rumore esterno.
- se è alto, il segnale è più forte del rumore e può quindi essere convertito in dati reali
- se è basso, il segnale è stato danneggiato dal rumore e i dati non possono essere recuperati

Per **evitare collisioni**, è necessario controllare l'accesso al mezzo (che è condiviso). 

>[!question] per le reti wireless, non si può usare CSMA/CD
>- **no collision detection**
>
>Per rilevare una collisione, un host deve poter trasmettere e ricevere (ascoltare il canale) contemporaneamente. Ma, poiché la potenza del segnale ricevuto è molto inferiore a quella del segnale trasmesso, sarebbe *troppo costoso* usare un adattatore di rete in grado di rilevare le collisioni (i dispositivi wireless  hanno un'energia limitata fornita dalla batteria che non consente loro di usare un dispositivo del genere).
>
>- **hidden terminal problem**
>
> Un host potrebbe non accorgersi che un altro host sta trasmettendo e non sarebbe in grado di rilevare la collisione.
> 
> ![[hidden-terminal.png|center|450]]
> 

## IEEE 802.11
IEEE ha definito le **specifiche per le LAN wireless**, chiamate `802.11`, che coprono i livelli fisico e collegamento.

### architettura BSS
**Basic Service Set** (BSS) è costituita da uno o più host wireless e un access point.

![[BSS.png|center|500]]

### architettura ESS
**Extended Service Set** è costituito da due o più BSS con infrastruttura.
- i BSS sono collegati da una rete cablata o wireless
- quando i BSS sono collegati, le stazioni in visibilità comunicano direttamente, mentre le altre comunicano tramite l'AP

![[ESS.png|center|500]]

### architettura generale
Le architetture BSS corrispondono alle celle delle **reti cellulari**, mentre ESS è molto  comune nelle reti WiFi moderne, soprattutto in aree dove è necessario coprire aree estese con accesso continuo alla rete wireless.

![[architettura-E-BSS.png|center|350]]

### canali e associazione
Lo spettro 2.4GHz-2.485GHz è diviso in **11 canali** parzialmente sovrapposti. L'amministratore dell'AP sceglie una frequenza, ma sono possibili interferenze (per esempio se viene usato lo stesso canale per AP vicini). Il numero massimo di frequenze utilizzabili da diversi AP per evitare interferenze è 3 (canali 1, 6, 11).

L'architettura IEEE 802.11 prevede che una stazione wireless si **associ ad un AP** per accedere a Internet.

>[!info] associazione di una stazione ad un AP
>
>Per associare una stazione (host) ad un AP è necessario conoscere gli AP disponibili in un BSS, e avere un protocollo di associazione.
>- l'AP invia segnali periodici (beacon) che includono l'identificatore dell'AP (SSID) e il suo indirizzo MAC
>- la stazione wireless che vuole entrare in un BSS scandisce gli 11 canali trasmissivi alla ricerca di frame beacon (*passive scanning*)
>- alla fine della scansione
