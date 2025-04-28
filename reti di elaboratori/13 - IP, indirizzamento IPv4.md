---
created: 2025-04-01
updated: 2025-04-28T12:23
---
Il protocollo IP (Internet Protocol) è responsabile della **suddivisione in pacchetti**, del **forwarding** e della **consegna** dei datagrammi a livello rete (host to host).
- è un protocollo *inaffidabile* e *connectionless*
- offre un servizio di consegna best effort

>[!summary] formato dei datagrammi
> 
>![[darifare.png|center|500]]
>
>- **numero di versione** ⟶ consente la corretta interpretazione del datagramma (può essere 4 per IPv4 o 6 per IPv6)
>- **lunghezza dell'intestazione** ⟶ indica dove inizia il campo dati (un datagramma IP può contenere un numero variabile di opzioni) (la lunghezza di un'intestazione senza opzioni è di 20 byte)
>- **tipo di servizio** ⟶ permette di distinguere diversi datagrammi con requisiti di qualità del servizio diverse (per esempio alcuni pacchetti potrebbero richiedere una consegna rapida, mentre altri potrebbero essere meno sensibili al ritardo)
>- **lunghezza del datagramma** ⟶ rappresenta la lunghezza totale del datagramma in byte (inclusa l'intestazione) - serve per capire se il pacchetto è arrivato per intero
>- **identificatore, flag, offset di frammentazione** ⟶ servono per gestire la frammentazione dei pacchetti [vedi [[13 - IP, indirizzamento IPv4#frammentazione|sotto]]] (IPv6 non prevede frammentazione)
>- **tempo di vita** (Time To Live) ⟶ incluso per assicurare che i datagrammi non resitno in circolazione per sempre nella rete; viene decrementaton ad oni hop e il datagramma viene eliminato se TTL=0
>- **protocollo** ⟶ indica il protocollo a livello di trasporto a cui va passato il datagramma (es: `6: TCP`, `17: UDP`)
>	- utilizzato solo quando il datagramma raggiunge la destinazione finale
>- **checksum dell'intestazione** ⟶ consente ai router di rilevare errori sui datagrammi ricevuti (al contrario di TCP/UDP, viene fatta solo sull'intestazione)
>	- viene ricalcolata nei router intermedi
>- **indirizzi IP di origine e destinazione** ⟶ sono inseriti dall'host che crea il datagramma
>- **opzioni** ⟶ consentono di estendere l'intestazione IP (per test o debug della rete)
>- **dati** ⟶ contiene il segmento di trasporto da consegnare alla destinazione

## frammentazione
Un datagramma IP può dover viaggiare attraverso reti con caratteristiche diverse - ogni router estrarrrà il datagramma, lo elaborerà e lo incapsulerà in un nuovo frame.

>[!info] Maximum Transfer Unit
>La **Maximum Transfer Unit** è la massima quantità di dati che un frame a livello di collegamento può trasportare.
>- la MTU varia in base alla tecnologia

Diverse reti hanno diversi MTU, quindi i datagrammi IP troppo grandi vengono suddivisi in datagrammi più piccoli (frammentazione). I frammenti saranno riassemblati solo una volta raggiunta la destinazione, prima di raggiungere il livello di trasporto.

### bit dell'intestazione
Alcuni bit dell'intestazione sono usati per identificare e riordinare i frammenti. Quando un host di destinazione ricefve una serie di datagrammi dalla stessa origine deve individuare i frammenti, determinare quando ha ricevuto l'ultimo e stabilire come debbano essere riassemblati.

Per farlo, usa:
- **identificazione** (16 bit) ⟶ identificativo associato a ciascun datagramma al momento della creazione (tutti i frammenti di uno stesso datagramma avranno la stessa identificazione)
	- IP + identificazione identificano in modo unico un datagramma
- **flag** (3 bit):
	- riservato
	- do not fragment: `1` se il datagramma non va frammentato
	- more fragments: `1` se il frammento è intermedio, `0` se è l'ultimo
- **offset** ⟶ secifica l'ordine del frammento all'interno del datagramma originario


>[!example] esempio di frammentazione
> 
>![[frammentazione-es.png|center|400]]
>
>![[frammentazione-es2.png]]
>
>- Il primo frammento ha un valore del campo offset pari a 0
>- l'offset del secondo si ottiene dividendo per 8 la lunghezza del primo frammento (esclusa l'intestazione)
>- l'offset del terzo si ottiene dividendo per 8 la somma della lunghezza del primo e del secondo (esclusa l'intestazione)
>- ...
>- l'ultimo frammento ha il bit `M` impostato a 0

## indirizzamento IPv4
Un indirizzo IP è formato da 32 bit (4 byte) in notazione decimale puntata.

>[!info] interfaccia
>l'**interfaccia** è il confine tra host e collegamento fisico
>- ogni interfaccia di host e router internet ha un indirizzo IP *globalmente univoco*
>- i router devono necessariamente essere connessi ad almeno due collegamenti
>- un host, in genere, ha una sola interfaccia

- gli indirizzi IPv4 sono in totale $2^{32}$ (più di 4 miliardi), e possono essere scritti in notazione binaria, decimale puntata, o esadecimale

### gerarchia nell'indirizzamento
Un indirizzo IPv4 si divide in **prefisso** e **suffisso**.
- il prefisso individua la rete
	- può avere lunghezza fissa (nel caso di indirizzamento con classi) o variabile (indirizzamento senza classi)
- il suffisso individua il collegamento al nodo

#### indiri