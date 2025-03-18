> [!info] protocollo
> Un **protocollo** definisce le regole che il mittente, il destinatario e tutti i sistemi intermedi coinvolti devono rispettare per essere in grado di comunicare.

In alcune situazioni, è opportuno suddividere i compiti fra più livelli (layer) - questo permette di suddividere un compito complesso in più compiti semplici, e permette la **modularizzazione** (indipendenza dei livelli).

- ogni modulo/livello può essere considerato come un black box, senza preoccuparsi delle modalità con cui i dati vengono processati e prodotti
- si **separano i servizi dalla loro implementazione**: un livello usa servizi dal livello inferiore, e offre servizi al livello superiore
- se due macchine forniscono lo stesso output  dallo stesso input, possono essere considerati *equivalenti* 

Talvolta è richiesta una **comunicazione bidirezionale**: ciascun livello deve essere capace di effettuare i due compiti opposti, uno per ciascuna direzione (per esempio crittografare e decrittografare).

I livelli sono *direttamente collegati*, ovvero il protocollo implementato a ciascun livello specifica una comunicazione diretta tra i **pari livelli** delle due parti.

## stack protocollare TCP/IP
(Lo stack protocollare prende il nome di TCP/IP perché TCP e IP sono i due protocolli più importanti).

La rete è organizzata come una pila di **strati** (layer) o **livelli**, costruiti l'uno sull'altro. Ogni livello offre servizi agli strati di livello superiore, nascondendo i dettagli di implementazione.

- strati dello stesso livello di computer diversi sono in comunicazione tra di loro, attraverso i **protocolli**
- le entità che formano gli strati sono chiamati **pari** (peer)



La pila TCP/IP era originariamente definita in termini di quattro livelli software + un livello hardware, ma è oggi intesa come composta di cinque livelli.

![[TCPIP-liv.png|center|500]]

### livello applicazione

**Applicazione** --> sede delle applicazioni di rete
- usa i protocolli: HTTP, SMTP, FTP, DNS
- i pacchetti sono chiamati *messaggi*

**Trasporto** --> trasferimento dei messaggi dal livello applicazione di un client a quello di un server
- protocolli: TCP affidabile, UDP non affidabile (l'affidabilità fa riferimento a correttezza e ordine di arrivo)
- i pacchetti sono chiamati *segmenti*

**Rete** --> instradamento dei segmenti dall'origine alla destinazione
- IP, protocolli di instradamento
- pacchetti: *datagrammi*

**Link** (hardware) --> trasmissione di datagrammi da un nodo a quello successivo sul percorso
- Ethernet, Wi-Fi, PPP (lungo un percorso sorgente-destinazione, un datagramma può essere gestito da protocolli diversi)
- pacchetti: *frame*

**Fisico** --> trasferimento dei singoli bit

>[!tip] comunicazione in una internet
>
>![[internet-comm.png|center|400]]
>
>- grazie al layering, i sistemi implementano solo i livelli necessari, riducendo la complessità
>- nel router, ci possono essere fino a $n$ livelli fisico-collegamento, con $n$ numero di link a cui il router è collegato
>- invece, poiché le porte dello switch sono omogenee, c'è un solo protocollo




**rete**: instradamento dei segmenti dall'origine alla destinazione (trova la rotta)
- i pacchetti trasmessi si chiamano *datagrammi*


L'ultimo livello è il livello fisico: trasferimento fisico dei bit lungo un canale di comunicazione

(switch sposta informazioni all'interno di una lan(rete), router collega reti)





visto che le porte dello switch sono omogenee, c'è solo un protocollo.


un protocollo non affidabile è più veloce


