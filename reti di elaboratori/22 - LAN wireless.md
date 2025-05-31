---
created: 2025-04-01
updated: 2025-05-31T22:15
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
	- i [[19 - livello di collegamento#protocolli di accesso multiplo|protocolli di accesso multiplo]] regolano l'accesso ai link


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
Le caratteristiche dei link wireless causano errori. Il tasso di errore è misurato con il **Signal to Noise Ratio** (SNR o rapporto segnale-rumore), che misura il rapporto tra il segnale buono e il rumore esterno.
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
>- l'AP invia segnali periodici (*beacon*) che includono l'identificatore dell'AP (SSID) e il suo indirizzo MAC
>- la stazione wireless che vuole entrare in un BSS scandisce gli 11 canali trasmissivi alla ricerca di frame beacon (*passive scanning*)
>- alla fine della scansione, la stazione sceglie l'AP da cui ha ricevuto il beacon con la maggiore potenza di segnale e gli invia un frame con la *richiesta di associazione*
>- l'AP accetta la richiesta con un *frame di risposta associazione* che permetterà all'host entrante di inviare una richiesta DHCP per ottenere l'indirizzo IP
>- può essere prevista un'*autenticazione* per eseguire l'associazione

### protocollo MAC 802.11
Più stazioni possono voler comunicare nello stesso momento. Sono quindi state definite due tecniche di accesso al mezzo:
- **Distributed Coordination Function** (DCF) ⟶ i nodi si contendono l'accesso al canale
- **Point Coordination Function** (PCF) ⟶ non c'è contesa, l'AP coordina l'accesso ai nodi del canale

### CSMA/CA
Poiché la collision detection non è possibile, si fa affidamento sulla **collision avoidance** (protocollo CSMA/CA), e si cerca di evitare che due o più nodi trasmettano contemporaneamente.

> [!summary] caratteristiche
> Il protocollo CSMA/CA usa:
> - **ACK** come riscontro per capire se una trasmissione è andata a buon fine
> 	- ci possono essere collisioni anche sugli ACK
> - **doppio carrier sense** (ascolto del canale prima di trasmettere) per dati e ack
> - **IFS** (spazio interframe) ⟶ tempo che una stazione aspetta prima di iniziare a trasmettere dopo aver rilevato che il canale è libero (si vuole evitare che le stazioni che hanno già iniziato a trasmettere collidano con la stazione che vuole trasmettere); può essere:
> 	- **SIFS** ⟶ Short IFS: garantisce alta priorità alle trasmissioni (usato anche per ACK)
> 	- **DIFS** ⟶ Distributed IFS: garantisce bassa priorità (usato per le trasmissioni normali)
> 	- DIFS > SIFS, in modo da dare priorità alle comunicazioni già iniziate (agli ACK)

Quindi:
- il mittente **ascolta** il canale: se lo trova libero, aspetta un DIFS e poi **trasmette**
	- se durante l’intervallo DIFS, il canale diventa occupato, il nodo interrompe il conteggio del DIFS, **aspetta** che il canale torni libero, e **riavvia da zero** il conteggio del DIFS completo
- se il ricevente **riceve** correttamente un frame, aspetta un SIFS e invia un `ACK`

In realtà, dopo aver atteso un tempo IFS, se il canale è ancora inattivo, l’host attende un ulteriore tempo di tempo di contesa: la **contention window**, il lasso di tempo per cui deve sentire il canale libero prima di trasmettere
- il tempo è diviso in slot, e ad ogni slot si esegue il **sensing** del canale
- l’host sceglie `R` random in `[0, CW]`
- `while R > 0:`
	- ascolta il canale per uno slot
	- se il canale è libero per la durata dello slot: `R -= 1`; altrimenti, se il canale è occupato durante il sensing, interrompe il timer e aspetta che il canale si liberi (e riavvia il timer)

### RTS/CTS
Il problema dell'**hidden terminal** non viene risolto con IFS e finestra di contesa: è necessario un meccanismo di **prenotazione del canale**: Request-to-Send (RTS) Clear-To-Send (CTS). 

![[RTS-CTS.png|center|450]]

- quando una stazione invia un frame RTS, include la durata di tempo in cui occuperà il canale per trasmettere il frame e ricevere l’`ACK` - questo tempo viene incluso anche nel CTS
- in questo modo, le stazioni che sono influenzate da tale trasmissione avviano un timer chiamato **NAV**, che indica quanto tempo devono attendere prima di eseguire il sensing del canale

>[!error] se il mittente non riceve CTS, assume che c’è stata  una collisione e riprova dopo un tempo di backoff

>[!warning] problema della stazione esposta
>
>Il problema della stazione esposta si verifica  quando una stazione si astiene dall'usare il canale anche se potrebbe trasmettere
>
>![[stazione-esposta.png|center|450]]
>
>In questo esempio, C è la stazione esposta
### ACK e timer
È necessario utilizzare riscontri positivi e timer per capire se una trasmissione è andata a buon fine.

Il mittente non può aspettare un ACK all'infinito, quindi imposta un timer (**ACK timeout**) e, se esso scade prima che abbia ricevuto l'ACK, il nodo suppone che la trasmissione sia fallita e tenta una **ritrasmissione**.

### formato del frame

>[!info] formato del frame
>
>![[frame-LAN.png|center|500]]
>
>- `Frame Control` (FC) ⟶ tipo di frame e alcune informazioni di controllo
>- `D` ⟶ durata della trasmissione, usata per impostare il NAV
>- `Indirizzi` ⟶ indirizzi MAC
>- `SC` ⟶ informazioni sui frammenti (numero di frammento e numero di sequenza); il numero di sequenza serve per distinguere frame ritrasmessi 
>- `Frame Body` ⟶ payload
>- `FCS` ⟶ codice CRC a 32 bit

>[!tip] Frame Control
>
>![[frame-FC.png|center|500]]
>
> Una LAN wireless ha 3 categorie di frame: gestione, controllo e dati. Si distinguono in base ai bit del campo FC:
> - `00` ⟶ frame di **gestione** (usati per le comunicazioni iniziali tra stazioni e punti di accesso)
> - `01` ⟶ frame di **controllo** (usati per accedere al canale e dare riscontri) (`1011` = RTS, `1100` = CTS, `1101` = ACK)
> - `10` ⟶ frame di **dati** (usati per trasportare i dati)
>> [!summary] indirizzamento
>> 
> >In base ai campi `To DS` e `From DS` del campo FC, si ha un diverso formato per i campi degli indirizzi
> >
>> | Significato                    | To DS | From DS | Address 1    | Address 2   | Address 3    | Address 4 |
>> | ------------------------------ | ----- | ------- | ------------ | ----------- | ------------ | --------- |
>> | comunicazione diretta (ad-hoc) | 0     | 0       | destinazione | sorgente    | BSS ID       | N/A       |
>> | da AP a host                   | 0     | 1       | destinazione | AP mittente | sorgente     | N/A       |
> >| da host ad AP                  | 1     | 0       | AP ricevente | sorgente    | destinazione | N/A       |
>> | da AP ad AP                    | 1     | 1       | AP ricevente | AP mittente | destinazione | sorgente  |
>> 
>> Essenzialmente, in `address 1` viene memorizzato l’indirizzo del dispositivo successivo a cui viene trasmesso in frame, mentre in `address 2` l’indirizzo del dispositivo che il frame ha lasciato.

## mobillità all'interno della stessa sottorete IP
La mobilità all'interno della stessa sottorete IP è semplice, e l'IP rimane lo stesso.

![[mobilita-sottorete.png|center|400]]

- $H_{1}$ sente che il segnale da $AP_{1}$ si affievolisce, e avvia una scansione per un segnale più forte
- $H_{1}$ rileva $AP_{2}$, si disassocia da $AP_{1}$ e si associa a $AP_{2}$, mantenendo lo stesso IP e sessioni TC
- $AP_{2}$ si occupa di inviare un frame di broadcast allo switch con indirizzo mittente $H_{1}$, e lo switch capisce che $H_{1}$ ora è nel $BSS_{2}$