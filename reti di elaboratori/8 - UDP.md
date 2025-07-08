---
created: 2025-04-07T11:35
updated: 2025-07-08T16:24
---
>[!info] overview
>- è un protocollo **senza connessione**: non è richiesto alcun setup fra processi client e server
>- il trasferimento dei dati è **inaffidabile** (è possibile che due messaggi mandati alla stessa destinazione arrivino in tempi diversi, ed è possibile la perdita di messaggi)
>- **non offre**: setup della connessione, affidabilità, controllo del flusso, controllo di errori (eccetto checksum), controllo della congestione, temporizzazione, ampiezza di banda minima, sicurezza
>- fornisce invece i **servizi** di:
>	- comunicazione tra processi attraverso socket
>	- multiplexing/demultiplexing dei pacchetti
>	- incapsulamento e decapsulamento
>- viene utilizzato quando non è necessaria l'affidabilità, perché è *più veloce* di TCP (la sua controparte affidabile)

Nella comunicazione attraverso UDP, il mittente invia pacchetti uno dopo l'altro senza pensare al destinatario.
- può inviare dati a raffica perché non c'è controllo di flusso o congestione

![[UDP-comms.png|center|450]]

UDP è un servizio **connectionless**: non c’è coordinazione tra livello di trasporto del mittente e del destinatario, e **ogni pacchetto è indipendente** dagli altri.
- il mittente deve solo dividere i suoi messaggi in porzioni di dimensioni accettabili dal livello trasporto, e consegnarli ad esso uno ad uno

![[UDP-es2.png|center|450]]

>[!info] rappresentazione mediante FSM
>
>![[UDP-FSM.png|center|500]]
>
>- UDP è un protocollo molto semplice (infatti le FSM hanno un solo stato)

>[!tip]- DNS usa UDP
>Quando effettua query, DNS utilizza UDP.
>- sceglie UDP invece di TCP perché deve effettuare query molto semplici e molto brevi, e UDP risulta più veloce
## datagrammi UDP
Nel procollo UDP, i messaggi devono avere dimensione inferiore a 65507 byte (65535 - 8 byte di intestazione UDP e 20 byte di intestazione IP). 

>[!summary] struttura dei datagrammi
>
>![[datagrammi-UDP.png|center|350]]

Il valore del campo **checksum** viene calcolato tamite **somma in complemento a uno** (CA1) in questo modo:
1) Il messaggio (compresa l'intestazione) viene diviso in "parole" da 16 bit
2) Tutte le parole del messaggio vengono sommate usando l'addizione in complemento a uno
	- l’eventuale riporto finale del bit più significativo viene sommato al bit meno significativo 
3) Il risultato è inserito nel campo checksum del segmento e questo viene inviato,
4) Il messaggio arriva al destinatario, e viene nuovamente diviso in parole da 16 bit.
5) Il destinatario esegue di nuovo l'addizione in complemento a uno di tutte le parole (compresa la checksum)
6) Se il valore della somma è 0, allora il messaggio viene accettato. Altrimenti, viene scartato.

>[!example] esempio
> 
>![[checksum.png|center|500]]
