---
created: 2025-04-01
updated: 2025-05-04T10:21
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
> - ogni nodo aggiorna i suoi vicini soo quando il suo vettore della distanza cambia (quindi i vicini sono avvisati solo se necessario)

**implementazione** (per ciascun nodo $x$):
```

```