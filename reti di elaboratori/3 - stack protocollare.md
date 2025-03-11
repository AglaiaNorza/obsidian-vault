> [!info] protocollo
> Un **protocollo** definisce le regole che il mittente, il destinatario e tutti i sistemi intermedi coinvolti devono rispettare per essere in grado di comunicare.

In alcune situazioni, è opportuno suddividere i compiti fra più livelli (layer) - questo permette di suddividere un compito complesso in più compiti semplici, e permette la **modularizzazione** (che rende i livelli indipendenti).

- ogni modulo/livello può essere considerato come un black box, senza preoccuparsi delle modalità con cui i dati vengono processati e prodotti
- si **separano i servizi dalla loro implementazione**: un livello usa servizi dal livello inferiore, e offre servizi al livello superiore
- se due macchine forniscono lo stesso output  dallo stesso input, possono essere considerati *equivalenti* 

Talvolta è richiesta una **comunicazione bidirezionale**: ciascun livello deve essere capace di effettuare i due compiti opposti, uno per ciascuna direzione (per esempio crittografare e decrittografare).

I livelli sono *direttamente collegati*, ovvero il protocollo implementato a ciascun livello specifica una comunicazione diretta tra pari livelli delle due parti



## organizzazione a più livelli

### principi
Quando è richiesta una comunicazione **bidirezionale**, ciascun livello deve essere in grado di effettuare i due compiti opposti, ognuno in ciascuna direzione.

Lo stack protocollare prende il nome di TCP/IP perché TCP e IP sono i due protocolli più importanti.
Si tratta di una **gerarchia** di protocolli che interagiscono tra di loro - 


**trasporto** - trasferisce i messaggi dal livello applicazione di un client a quello di un server
- TCP affidabile, UDP non affidabile (correttezza e ordine di arrivo)


**rete**: instradamento dei segmenti dall'origine alla destinazione (trova la rotta)
- i pacchetti trasmessi si chiamano *datagrammi*


L'ultimo livello è il livello fisico: trasferimento fisico dei bit lungo un canale di comunicazione

(switch sposta informazioni all'interno di una lan(rete), router collega reti)





visto che le porte dello switch sono omogenee, c'è solo un protocollo.


un protocollo non affidabile è più veloce


