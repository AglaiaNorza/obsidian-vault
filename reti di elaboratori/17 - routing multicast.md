---
created: 2025-04-01
updated: 2025-05-26T15:54
---
# unicast

> [!info] unicast
> Il routing **unicast** prevede la comunicazione tra **una sorgente e una destinazione**.
> 
> ![[unicast-es.png|center|400]]
> 
# broadcast
>[!info] broadcast
>Il routing **broadcast** prevede l'invio di un pacchetto da un nodo sorgente **a tutti i nodi della rete** (IP sorgente ⟶ indirizzo broadcast).


Il broadcast può essere eseguito in due modi: attraverso *uncontrolled* o *controlled* flooding.
## uncontrolled flooding
Nell'uncontrolled flooding, quando un nodo riceve un pacchetto broadcast, lo duplica e lo **invia a tutti i nodi vicini** eccetto quello da cui lo ha ricevuto.
- se il grafo ha cicli, una o più copie del pacchetto cicleranno all'infinito nella rete

## sequence number controlled flooding
Nel sequence number controlled flooding, **non vengono forwardati pacchetti già ricevuti** ed inoltrati. Ogni nodo tiene una lista di `(IP, #sequenza)` dei pacchetti già ricevuti, duplicati e inoltrati. Quando riceve un pacchetto, controlla nella lista e: se è già stato inoltrato, lo scarta, altrimenti lo inoltra.

## reverse path forwarding
Nel reverse path forwarding, un pacchetto viene forwardato solo se è arrivato dal link che è **sul suo shortest path** (unicast)

>[!example] esempio
>
>![[controlled-flood-es.png|center|300]]
>

RPF elimina il problema dell'invio di troppi pacchetti sulla rete, ma non elimina completamente la ridondanza nella trasmissione
- per esempio, nel grafo sopra, $B,\,C,\,D ,\,E$ ed $F$ ricevono uno o due pacchetti ridondanti

La soluzione è costruire uno **spanning tree** prima di inviare i pacchetti broadcast.

>[!summary] costruzione dello spanning tree (center-based)
>- Si prende un nodo come centro (esempio: $E$)
>- ogni nodo invia un messaggio di join in unicast verso il centro
>- i messaggi vengono inoltrati finché arrivano alla radice o a un nodo che appartiene già all'albero
>
>![[spanning-tree-centerbased-reti.png|center|400]]

Quindi i pacchetti vengono inoltrati **solo sui link dell'albero**, e ogni nodo riceve solo una copia del pacchetto.

# multicast

> [!info] multicast
> Il routing **multicast** prevede la comunicazione tra **una sorgente** e **un gruppo di destinazioni**.
> 
> ![[multicast.png|center|450]]
> 
> Viene usato da applicazioni come streaming audio/video a gruppi di persone, trasferimenti di aggiornamenti software su un gruppo di macchine...

Si differenzia dall'**unicast multiplo** per i fatto che viene inviato un solo datagramma, che verrà poi duplicato dai router.
- il multicast, quindi, elimina i ritardi causati dall'invio di multipli pacchetti dell'unicast multiplo

Per poter comunicare con host che partecipano a un gruppo pur appartenendo a reti diverse, si assegna un unico **indirizzo multicast** a tutto il gruppo.
- esiste un blocco di indirizzi riservati per il multicast
	- in IPv4, è `224.0.0.0/4` (ovvero comprende gli indirizzi da `224.0.0.0` a `239.255.255.255`), per un totale di $2^{28}$ gruppi

>[!example]- esempio di gruppo multicast
>  
>![[gruppo-multicast.png|center|400]]

>[!warning] L’appartenenza ad un gruppo non ha alcuna relazione con il prefisso associato alla rete
>Un host che appartiene ad un gruppo ha un indirizzo multicast **separato** e aggiuntivo rispetto al primario (l’appartenenza non è un attributo fisso dell’host, in quanto il periodo di appartenenza può essere limitato).

Un router deve scoprire quali gruppi sono presenti in ciascuna delle sue interfacce, per poter propagare le informazioni agli altri router.

Per il multicast sono necessari *due protocolli*:
- uno per raccogliere le informazioni di appartenenza ai gruppi
- uno per diffonderle
### Internet Group Management Protocol (IGMP)
Il protocollo IGMP lavora **tra un host e il router** che gli è **direttamente connesso**. Esso offre agli host un modo di *informare i router* ad esso connessi del fatto che un'applicazione in esecuzione vuole aderire ad uno specifico gruppo multicast.

![[IGMP.png|center|400]]

#### messaggi IGMP
I messaggi IGMP sono incapsulati in datagrammi IP con `IP protocol number === 2`, e vengono mandati con `TTL == 1`.

I tipi di messaggio sono:
- `Membership query`: è un messaggio router $\to$ host, che permette di determinare **a quali gruppi hanno aderito gli host** su ogni interfaccia 
	- viene inviato periodicamente
- `Membership report`: è un messaggio host $\to$ router, che **informa** il router su un'**adesione**
	- eseguito, oltre che su query, anche al momento dell'adesione
- `Leave group`: è un messaggio host $\to$ router, inviato **quando si lascia un gruppo**
	- è opzionale: un router può capire che non ci sono più host associati a un gruppo quando non riceve più `Membership report`

>[!summary] liste di sottoreti
>Un router multicast tiene una **lista per ciascuna sottorete** dei gruppi multicast con un **timer** per membership. La membership deve essere aggiornata tramite report inviati prima della scadenza del timer, o tramite messaggi di leave espliciti.

### problema del routing multicast
Tra tutti i router, solo quelli collegati a host del gruppo multicast devono ricevere traffico multicast
- è quindi necessario un protocollo che coordini i router multicast in Internet, instradando i pacchetti multicast dalla sorgente alla destinazione

>[!example] esempio
>[ esempio ]

Ci sono diversi approcci per **determinare l'albero d'instradamento multicast**:
1) <u>**albero condiviso dal gruppo**</u>

Viene costruito un **singolo albero** di instradamento condiviso da tutto il gruppo multicast, e un router agisce da **rappresentante** del gruppo. 

Se il mittente del traffico multicast non è il centro, invierà il traffico in unicast al centro, che lo invierà al gruppo.

[ foto ]

2) <u>**albero basato sull'origine**</u>

Viene creato **un albero per ciascun'origine** nel gruppo multicast (con un algoritmo basato su reverse path forwarding con potatura). Ci sono quindi tanti alberi quanti mittenti del gruppo multicast.

### instradamento multicast in Internet
Per l'instradamento **intra-dominio** (interno a un sistema autonomo) si usano:
- **DVMRP** (Distance-Vector Multicast Routing Protocol)
- **MOSPF** (Multicast Open Shortest Path First)
- **PIF** (Protocol Independent Multicast)

Per l'instradamento **inter-dominio** (tra sistemi autonomi), si usa:
- **MBGP**: Multicast Border Gateway Protocol