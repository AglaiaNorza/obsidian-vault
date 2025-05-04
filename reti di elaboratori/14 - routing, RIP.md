---
created: 2025-04-01
updated: 2025-05-04T09:52
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
>Un **albero a costo minimo** (minimum spanning tree) è una combinazione di percorsi a costo minimo dalla radice dell'albero verso tutte le destinazioni [ analogo al [[10 - minimo albero di copertura|minimo albero di copertura (prog. di algo)]] ]
>- il **vettore di distanza** è un array monodimensionale che rappresenta l'albero
>	- non fornisce il percorso da seguire per giungere alle destinazioni, ma solo i costi minimi
>
>>[!example] esempio
>>
>>![[alberominimoRETI.png|center|400]]

