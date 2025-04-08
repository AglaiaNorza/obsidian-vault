---
created: 2025-04-01
updated: 2025-04-08T11:33
---
# introduzione
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

## controllo degli errori
L'affidabilità deve essere implementata a livello di trasporto, perché il livello di rete è inaffidabile. 
Per avere un servizio di trasporto affidabile, è necessario implementare un **controllo degli errori** sui pacchetti, che possa:
- rilevare e scartare pacchetti corrotti
- tenere traccia dei pacchetti persi e gestirne il rinvio
- riconoscere pacchetti duplicati e scartarli
- bufferizzare i pacchetti fuori sequenza finché arrivano i pacchetti mancanti

>[!tip] i messaggi scambiati tra livelli sono esenti da errori, quindi il controllo degli errori coinvolge solo i livelli trasporto mittente e destinatario

Il mittente deve quindi sapere quali pacchetti ritrasmettere, e il destinatario deve saper riconoscere pacchetti duplicati e fuori sequenza. Per riuscirci, si introducono:
- un **numero di sequenza** per ogni pacchetto (con numerazione sequenziale)
- un **numero di riscontro** (ack), che permette di notificare al mittente la corretta ricezione di un pacchetto

## integrazione di controllo di errori e controllo di flusso
Si combinano i buffer del controllo di flusso e il numero di sequenza e ack del controllo degli errori. 

Quindi, il **mittente**:
- quando prepara un pacchetto, usa come numero di sequenza il numero $x$ della *prima locazione libera nel buffer*
- quando invia il pacchetto, ne memorizza una copia nella locazione $x$
- quando riceve un ack, libera la posizione di memoria che era occupata da quel pacchetto

Il **destinatario**:
- quando riceve un pacchetto con numero di sequenza $y$, lo memorizza nella locazione $y$ fino a quando il livello applicazione non è pronto a riceverlo
- quando passa il pacchetto $y$ al livello applicazione, invia un ack al mittente

I numeri di sequenza sono calcolati in modulo $2^m$, e possono essere rappresentati con un cerchio. Il buffer può essere rappresentato tramite un insieme di settori chiamati *sliding windows*, che occupano una parte del cerchio:

![[buffer-cerchio.png|center|500]]

Oppure, può essere rappresentato in maniera lineare:

![[sliding-window.png|center|500]]

## controllo della congestione
La congestione avviene se il **carico** della rete è superiore alla sua **capacità**. Il controllo della congestione fa sì che questo non avvenga.

# meccanismi per il trasferimento dati affidabile
## stop-and-wait
Lo stop-and-wait è un meccanismo orientato alla connessione, che implementa controllo del flusso e controllo degli errori.
- mittente e destinatario usano una **finestra di scorrimento di dimensione 1**
- il mittente invia un pacchetto alla volta e ne **attende** l'ack prima di spedire il successivo
- quando il pacchetto arriva al destinatario, viene calcolato il checksum 
	- se il pacchetto è corrotto, viene scartato *senza informare il mittente*
- per capire se un pacchetto è andato perso, il mittente usa un **timer** (in quanto non può aspettare all'infinito di ricevere un ack)
	- se il timer scade e non ha ricevuto un ack, il pacchetto viene rinviato
	- il mittente deve quindi tenere una *copia* del pacchetto spedito fino a quando non riceve il riscontro

Il **controllo degli errori** viene implementato quindi tramite il numero di sequenza e l'utilizzo di ack e timer. Il **controllo del flusso** è intrinseco, in quanto non si spedisce più di un pacchetto alla volta.

### numeri di sequenza e riscontro
Per gestire pacchetti duplicati, stop-and-wait utilizza i numeri di sequenza $0$ e $1$. Il numero di riscontro indica quindi, in aritmetica modulo 2, il numero di sequenza del prossimo pacchetto atteso dal destinatario.

> [!example] situazioni possibili
> Supponiamo che il mittente abbia inviato il pacchetto con numero di sequenza
> $x$. Si possono verificare 3 casi:
> 1. Il pacchetto arriva correttamente al destinatario che invia un riscontro ⟶ il riscontro arriva al mittente, che invia il pacchetto successivo numerato $x+1$
> 2. Il pacchetto risulta corrotto o non arriva al destinatario ⟶ il mittente, allo scadere del timer, invia nuovamente il pacchetto $x$
> 3. Il pacchetto arriva correttamente al destinatario, ma il riscontro viene perso o corrotto ⟶ scade il timer e il mittente rispedisce $x$. 
>	- Il destinatario riceve un duplicato, se ne accorge?