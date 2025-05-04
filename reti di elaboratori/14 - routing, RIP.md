---
created: 2025-04-01
updated: 2025-05-04T11:21
---
>[!info] routing
>Il **routing** si occupa di trovare il **miglior percorso** per un pacchetto e di inserirlo nella tabella di routing (o tabella di forwarding).
>
>>[!question] routing vs forwarding
>>Quindi, il routing costruisce le tabelle che vengono poi usate dal [[13 - IP, IPv4, DHCP, NAT, forwarding, ICMP#forwarding di datagrammi IP|forwarding]] (che colloca fisicamente il datagramma sulla giusta porta di uscita del router)
 
Una rete di calcolatori si può rappresentare tramite **grafo pesato**.

![[reti-grafo.png|center|400]]

$G=(N,E)$
 
$N=\text{insieme dei nodi (router)}=\{u,v,w,x,y,z\}$
 
$E=\text{insieme di archi}=\{(u,v), (u,x), (v,x), (v,w), (x,w), (x,y), (w,y), (w,z), (y,z)\}$

- un **path** nel grafo $G$ è una sequenza di nodi $(x_{1},\,x_{2},\,\dots,\,x_{n})$ tale che ognuna delle coppie $(x_{1},\,x_{2}),\,(x_{2},\,x_{3}),\dots,(x_{n-1},x_{n})$ sono archi in $E$
- $c(x,\,x')$ è il **costo** del collegamento $(x,\,x')$
- il *costo di un cammino* è la somma di tutti gli archi che lo compongono

Il costo di un cammino può rappresentare:
- lunghezza fisica del collegamento
- velocità del collegamento
- costo monetario associato al collegamento

In un grafo di una rete di calcolatori, il **cammino a costo minimo** tra due nodi si calcola con un **algoritmo di instradamento**.

## algoritmo distance vector
È un algoritmo:
- *distribuito* ⟶ ogni nodo riceve informazioni dai vicini e opera su quelle
- *asincrono* ⟶ non richiede che tutti i nodi operino al passo con gli altri

L'algoritmo DV si basa sull'**equazione di Bellman-Ford** [ [[11 - algoritmo di Bellman-Ford|lezione di progettazione di algoritmi su Bellman-Ford]] ]. Essa definisce:

$$\begin{align*}
D_{x}(y) := \text{costo del percorso a costo minimo dal nodo $x$ al nodo $y$}
\end{align*}$$

in cui:

$$\begin{align*}
D_{x}(y)=min_{v}\{ c(x,v) + D_{v}(y) \}
\end{align*}$$

- (dove $min_{v}$ riguarda tutti i vicini di $x$) 
- ovvero: si considera quanto costano gli archi da $x$ a ciascun vicino $v$, e si sceglie il percorso che, passando per $v$, ha il costo totale (fino a $y$) che sia minimo

>[!example] esempio 
>
>![[DV-es.png|center|450]]
>
>Si ha: 
>
>$$\begin{align*}
>D_{xy} = min\{(c_{xa} + D_{ay}), (c_{xb} + D_{by}), (c_{xc} + D_{cy})\}
>\end{align*}$$
>
>- (in cui $a \to y$, $b \to y$, $c\to y$ sono percorsi a costo minimo precedentemente calcolati)

### vettore distanza, minimum spanning tree
 
>[!info] albero a costo minimo
>Un **albero a costo minimo** (minimum spanning tree) è una combinazione di percorsi a costo minimo dalla radice dell'albero verso tutte le destinazioni [ praticamente analogo al [[10 - minimo albero di copertura|minimo albero di copertura (prog. di algo)]] ]
>- il **vettore di distanza** è un array monodimensionale che rappresenta l'albero
>	- non fornisce il percorso da seguire per giungere alle destinazioni, ma solo i costi minimi
>
>>[!example] esempio
>>
>>![[alberominimoRETI.png|center|400]]

Quando viene inizializzato un nodo, si crea un vettore distanza iniziale con le informazioni che il nodo ottiene dai suoi vicini 
- per crearlo, il nodo invia messaggi di `hello` attraverso le sue interfacce (e i vicini fanno lo stesso), e scopre l'identità dei suoi vicini e la distanza da ognuno di essi
- dopo che ogni nodo ha creato il suo vettore, ne invia una copia ai suoi vicini
- quando un nodo riceve un vettore distanza da un suo vicino, *aggiorna* il suo vettore distanza applicando l'equazione di Bellman-Ford

>[!example]- esempio 
>
>![[DV-ese1.png|center|300]]
>
>1) $B$ riceve una copia del vettore di $A$
>
>![[DV-ese2.png|center|300]]
>
>2) $B$ riceve una copia del vettore di $E$
>
>![[DV-ese3.png|center|300]]

> [!summary] passi dell'algoritmo
> Quindi, l'idea di base dell'algoritmo è questa:
> - ogni nodo **invia una copia** del proprio vettore distanza a ciascuno dei suoi vicini
> - quando un nodo $x$ riceve un nuovo vettore di distanza da un suo vicino, lo salva e usa la formula di Bellman-Ford per **aggiornare** il proprio vettore distanza 
> - se il vettore distanza del nodo $x$ è cambiato, $x$ **manderà** il proprio vettore distanza aggiornato a ciascuno dei suoi vicini, che a loro volta aggiorneranno i propri
> 
> (è *asincrono* perché) ogni iterazione locale è causata da:
> - cambio del costo di uno dei collegamenti locali
> - ricezione da un vicino di un vettore di distanza aggiornato
> 
> (è *distribuito* perché):
> - ogni nodo aggiorna i suoi vicini soo quando il suo vettore della distanza cambia (i vicini sono avvisati solo se necessario)

### problema della modifica dei costi
con le modalità di aggiornamento definite nell’algoritmo, si può verificare il *problema del conteggio all’infinito* (le buone notizie viaggiano in fretta, e le notizie cattive si propagano lentamente <small>(life lesson)</small>).

>[!example] esempio 
>si guasta il collegamento tra $A$ e $X$
>
>![[conteggio-infinito.png|center|500]]
>
>il router $A$ si aggiorna male a causa del guasto di $X$, quindi invia l’aggiornamento a $B$, che incrementa il vettore delle distanze; la richiesta di aggiornamento continuerà a rimbalzare tra $A$ e $B$ (e di conseguenza il costo aumenterà) finché il costo non sarà $\infty$

Ci sono due possibili *soluzioni* a questo problema:
- **split horizon** ⟶ invece di inviare la tabella attraverso ogni interfaccia, ciascun nodo invia *solo una parte* della sua tabella tramite le interfacce: se per esempio il nodo $B$ ritiene che il percorso ottimale per arrivare a $X$ passi attraverso $A$, non fornisce questa informazione ad $A$ (in quanto gli è arrivata da $A$, che quindi la conosce già)
	- nell'esempio di sopra, $B$ elimina la riga di $X$ prima di inviarla ad $A$
- **poisoned reverse** ⟶ si pone a $\infty$ il valore del costo del percorso che passa attraverso il vicino a cui si sta inviando il vettore
	- nell'esempio di sopra, $B$ pone a $\infty$ il costo verso $X$ quando invia il vettore ad $A$

## protocollo RIP
Il **Routing Information Protocol** (RIP) è un protocollo a vettore distanza, <small>ed è incluso in UNIX BSD dal 1982 </small>.
- la *metrica di costo* è la distanza misurata in **hop**
	- 15 è il massimo di hop, e 16 indica $\infty$
	- ogni link ha un costo unitario

>[!example] esempio 
>
>![[RIP-es.png|center|450]]

Nel protocollo RIP, ogni router manda **periodicamente** la sua routing table agli altri router. Ogni router dello stesso network potrà quindi aggiornare le sue tabelle in base alle informazioni ricevute. 
- ogni router che riceve un messaggio da un altro router (nello stesso network) che dice di poter raggiungere il network $X$ a costo $N$ sa che potrà a sua volta raggiungerlo a costo $X+1$ (attraverso il router da cui ha ricevuto il messaggio)

>[!tip] invece di inviare solo i vettori di distanza, i router inviano l'intero contenuto della tabella di routing

### messaggi RIP
RIP si basa su una coppia di processi **client-server** e sul loro scambio di messaggi.
- **RIP request** ⟶ quando un nuovo router viene inserito nella rete, invia una RIP request per ricevere immediatamente informazioni di routing
- **RIP response** (o **advertisements**) ⟶ o in risposta a una Request (*solicited response*), o periodicamente ogni 30 secondi (*unsolicited response*)

Ogni messaggio contiene un elenco comprendente fino a 25 sottoreti di destinazione all’interno del sistema autonomo e la distanza del mittente rispetto a ciascuna di tali sottoreti.

