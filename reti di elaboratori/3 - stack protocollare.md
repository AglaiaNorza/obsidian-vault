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