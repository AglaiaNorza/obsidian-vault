---
created: 2025-04-10T14:17
updated: 2025-04-24T21:06
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
>
>La **ricerca nella tabella di inoltro** deve essere veloce per evitare accodamenti. 
>La tabella è quindi implementata con una *struttura ad albero*, in cui ogni livello dell'albero corrisponde a un bit dell'indirizzo di destinazione.
>- per cercare un indirizzo si comincia dalla radice (se il primo bit è `0`, si trova nel sottoalbero sinistro, altrimenti in quello destro)
>- la ricerca richiede quindi $N$ passi (dove $N$ è il numero di bit dell'indirizzo)

>[!info] porte di ingresso e di uscita
>##### porte d'ingresso
>
>![[porte-ingresso.png|center|400]]
>
>La **commutazione decentralizzata** determina la porta d’uscita dei pacchetti utilizzando le informazioni della tabella d’inoltro (ogni porta d’ingresso ha una copia della tabella)
>- l’obiettivo è quello di completare l’elaborazione allo stesso tasso della linea (evitando bottlenecks). 
>	- c'è accodamento di pacchetti se il tasso di arrivo dei datagrammi è superiore a quello di inoltro
>- una volta determinata la porta di uscita, il pacchetto verrà inoltrato alla struttura di commutazione
>
>##### porte d'uscita
>
>![[porte-uscita.png|center|450]]
>
>Le porte di uscita gestiscono:
>- **funzionalità di accodamento** ⟶ necessarie quando la struttura di commutazione consegna pacchetti alla porta d'uscita ad una frequenza che supera quella del collegamento uscente
>- **schedulatore di pacchetti** ⟶ stabilisce in quale ordine trasmettere i pacchetti accodati

### tecniche di commutazione
Ci sono tre modi per far passare un pacchetto dalla porta di ingresso alla porta di uscita:
- commutazione in memoria
- commutazione tramite bus
- commutazione tramite rete di interconnessione

![[tecniche-commutaz.png|center|400]]


#### commutazione in memoria
Era utilizzata dalla prima generazione di router. Questi erano tradizionali calcolatori e la commutazione era effettuata sotto il *controllo diretto della CPU*.
- il pacchetto veniva copiato nella memoria del processore e veniva trasferito dalle porte di ingresso a quelle di uscita

![[comm-memoria.png|center|450]]


#### commutazione tramite bus
Le porte d'ingresso trasferiscono un pacchetto direttamente alle porte d'uscita su un *bus condiviso*, senza l'intervento del processore di instradamento.
- si può trasferire *un solo pacchetto alla volta*
- i pacchetti che arrivano e trovano il bus occupato vengono accodati alla porta d'ingresso - la larghezza di banda della commutazione è quindi limitata da quella del bus

![[comm-bus.png|center|350]]
#### commutazione tramite rete di interconnessione
La commutazione tramite rete di interconnessione risolve il problema del limite di banda di un singolo bus condiviso.
Usa un **crossbar switch**: una rete di interconnessione che formata da $2n$ bus che collegano $n$ porte d'ingresso a $n$ porte di uscita.

(Attualmente, si tende a frammentare i pacchetti IP a lunghezza variabile in celle di lunghezza fissa).

### accodamento
L'accodamento si verifica sia nelle porte di ingresso che in quelle di uscita.

>[!info] velocità di commutazione
>La **velocità di commutazione** è la frequenza alla quale una struttura può trasferire i pacchetti dalle porte di ingresso a quelle di uscita.

>[!question] capacità dei buffer
>Per quanto riguarda la **capacità dei buffer**, per diversi anni si è seguita la regola definita in RFC 3439:  la quantità di buffering dovrebbe essere uguale a una media del tempo di andata e ritorno (RTT) per la capacità del collegamento $C$.
>
>Le attuali raccomandazioni dicono invece che la quantità di buffering necessaria per $N$ flussi TCP è:
>
>$$\frac{RTT \cdot C}{\sqrt{ N }}$$
#### accodamento nelle porte di ingresso
Si verifica:
- quando la *velocità di commutazione è inferiore* a quella delle porte di ingresso
	- per non avere accodamento, la velocità di commutazione dovrebbe essere $n \times\text{velocità della linea di ingresso}$
- quando c'è un **blocco in testa alla fila** (HOL: Head-Of-the-Line blocking) ⟶ un pacchetto nella coda di ingresso deve attendere il trasferimento perché viene bloccato da un altro pacchetto in testa alla fila

Se le code diventano troppo lunghe, i buffer si possono saturare e causare **perdita di pacchetti**.

![[accod-ingr.png|center|450]]

#### accodamento sulle porte di uscita
Avviene:
- quando la struttura di commutazione ha un *rate superiore* alla porta di uscita
- quando troppi pacchetti vanno sulla stessa porta di usicita

Anche in questo caso, se le code diventano troppo lunghe, i buffer si possono saturare e causare **perdita di pacchetti**.

![[accod-usc.png|center|450]]