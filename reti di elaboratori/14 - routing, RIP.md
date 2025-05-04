---
created: 2025-04-01
updated: 2025-05-04T09:20
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

In un grafo di una rete di calcolatori, il **cammino a costo minimo** tra due nodi si calcola con un **algoritmo di instradamento**
