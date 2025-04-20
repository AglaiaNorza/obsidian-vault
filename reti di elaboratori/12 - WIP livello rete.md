---
created: 2025-04-10T14:17
updated: 2025-04-20T11:56
---
Come visto nell'[[3 - stack protocollare|introduzione allo stack protocollare]], il livello di rete si occupa dell'instradamento dei segmenti dall'origine alla destinazione.
Nello specifico, svolge due compiti:
- **routing** (instradamento) ⟶ determina il percorso seguito dai pacchetti dall'origine alla destinazione
- **forwarding** (inoltro) ⟶ trasferisce i pacchetti dall'input di un router all'output del router appropriato (utilizzando il percorso definito dal routing)

>[!info] routing e forwarding
>
>![[routing-algo.png|center|400]]
>
>Un **routing algorithm** crea la **forwarding table**, che specifica quale collegamento di uscita bisogna prendere per raggiungere la destinazione.
> - ogni router ha la sua forwarding table

## switch e router
![[hostrouterlinkswitch.png|center|450]]

Il **packet switch** è il dispositivo che si occupa del trasferimento dall'interfaccia d'ingresso a quella di uscita, in base al valore del campo di intestazione a pacchetto. 

Il **link-layer switch** instrada pacchetti a livello di collegamento, ed è utilizzato per collegare singoli computer all'interno di una rete LAN. 

Il **router** instrada pacchetti a livello rete, inoltrandolo ad un altro dei suoi collegamenti di comunicazione (*next hop*).

>[!info] architettura del router
>
>![[router-arch.png|center|450]]

Esistono due approcci per lo switching: a *circuito virtuale*, e a *datagamma*.
### reti a circuito virtuale
L'approccio a circuito virtuale è orientato alla connessione: prima che i datagrammi fluiscano, i due sistemi terminali e i router intermedi stabiliscono una connessione virtuale.

Un circuito virtuale consiste in:
1. un percorso tra gli host di origine e destinazione
2. **numeri VC**, uno per ciascun collegamento
3. righe nella tabella d’inoltro in ciascun router

Ogni pacchetto di un circuito virtuale ha un **numero VC** (etichetta di circuito) nella propria intestazione, che cambia su tutti i collegamenti lungo un percorso. Ogni router sostituisce il numero VC con un nuovo numero (rilevato dalla tabella di inoltro).

>[!summary] tabella di inoltro
>
>![[tab-inoltro.png|center|450]]
>
>I router mantengono le informazioni sullo stato delle connessioni: aggiungono alla tabella di inoltro una nuova riga ogni volta che stabiliscono una nuova connessione, e la cancellano quando la connessione viene rilasciata.

>[!example] esempio: ATM
>La rete ATM (Asynchronous Transfer Mode) è una rete orientata alla connessione progettata nei primi anni 90, con lo scopo di unificare voce, dati, televisione via cavo ecc.
>
>Attualmente, è usata nella rete telefonica per trasportare internamente pacchetti IP.
>- le connessioni vengono chiamate circuiti virtuali
>- quando una connessione è stabilita, ciascuna parte può inviare dati

### reti a datagramma
Le reti a datagramma sono connectionless, e ogni datagramma viaggia indipendentemente dagli altri. In queste reti, l'impostazione della chiamata non avviene a livello di rete e i router della rete non conservano informazioni sullo stato dei circuiti virtuali (non c'è il concetto di "connessione") a livello di rete.

I pacchetti vengono inoltrati usando l'indirizzo dell'host destinatario. Essi passano attraverso una serie di router e possono intraprendere percorsi diversi.

![[rete-packet.png|center|500]]

>[!summary] processo di inoltro
>
>![[proc-inoltro1.png|center|400]]
>
>La tabella di inoltro è gestita creando dei bucket per gli indirizzi (che hanno dimensione 4 byte), con questa logica:
>
>![[proc-inoltro2.png|center|400]]
>
>e gli indirizzi vengono suddivisi in modo più efficiente, ovvero confrontando il prefisso dell’indirizzo:
>
>![[proc-inoltro3.png|center|400]]
> `11001000 00010111 00010110 10100001` ⟶ $0$
>  
>  `11001000 00010111 00011000 10101010` ⟶ $1$
>
>- se si verificano corrispondenze multiple, si prende la corrispondenza a prefisso più lungo

2