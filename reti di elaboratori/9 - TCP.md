---
created: 2025-04-01
updated: 2025-04-07T17:25
---
>[!info] overview
>- è un protocollo **orientato alla connessione**: è richiesto un *setup* tra i processi client e server.
>- il trasferimento dei dati è **affidabile**
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

## servizio connection-oriented
Viene stabilita una **connessione logica** prima dello scambio dei dati.

![[connection-oriented.png|center|400]]

>[!info] rappresentazione FSM
>
>![[FSM-conn-oriented.png|center|400]]

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

