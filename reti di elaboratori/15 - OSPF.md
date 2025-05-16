---
created: 2025-05-05T20:03
updated: 2025-05-16T12:23
---
## link state
Lo stato di un link indica il **costo** associato al link. 
- quando un collegamento non esiste o è stato interrotto, il costo viene settato a $\infty$
 
Ogni nodo deve conoscere i costi di tutti i collegamenti della rete, e la mappa completa di tutti i link della rete viene mantenuta dal **link state database** (LSDB).

### link state database
Il **link state database** è unico per tutta la rete, e ogni nodo ne possiede una copia. Esso viene rappresentato con una **matrice** <small>(come una [[1 - introduzione ai grafi#rappresentare i grafi|matrice di adiacenza]] ma con i costi al posto di 0/1)</small>.

>[!example] esempio 
>
>![[LSDB-es.png|center|300]]

>[!summary] costruire il link state database
> Per costruire il link state database, ogni nodo della rete deve innanzitutto conoscere i propri vicini e i costi dei collegamenti verso di loro
> - ogni nodo invia quindi un messaggio di `hello` a tutti i suoi vicini
> - ogni nodo riceve gli `hello` dei vicini e crea una lista, chiamata **LS packet** (LSP), con vicini e costi dei collegamenti 
> - ogni nodo esegue un **flooding** degli LSP, ovvero invia a tutti i vicini il proprio LSP
> 	- quando riceve l'LSP di un vicino, se è nuovo lo inoltra a tutti i suoi vicini eccetto quello da cui lo ha ricevuto
> 
> ![[LSP-LSDB.png|center|450]]


## algoritmo di instradamento a link state
Si utilizza l'**algoritmo di Dijkstra** <small>[ trattato anche [[9 - grafi pesati, algoritmo di Dijkstra|qui]] (progettazione di algoritmi) ]</small> per calcolare il cammino di costo minimo da un nodo a tutti gli altri, creando una *tabella di inoltro* per quel nodo.
- è iterativo: dopo la $k$-esima iterazione, i cammini a costo minimo sono noti a $k$ nodi di destinazione
- ogni nodo applica l'algoritmo indipendentemente

>[!summary] notazione
>- $N$ ⟶ insieme dei nodi della rete
>- $c(x,\,y)$ ⟶ costo del collegamento dal nodo $x$ al nodo $y$
>- $D(y)$ ⟶ costo del cammino minimo dal nodo origine alla destinazione $v$ (all'iterazione corrente)
>- $p(v)$ ⟶ immediato predecessore di $v$ lungo il cammino
>- $N'$ ⟶ sottoinsieme di nodi per cui il cammino a costo minimo dall'origine è defnitivamente noto

**implementazione**:

inizializzazione:
- $N' = {r}$ (il nodo che esegue l'algoritmo)
- per tutti i nodi $n$:
	- se $n$ è adiacente a $r$, allora $D(n) = c(r, n)$
	- altrimenti $D(n) = \infty$

ciclo (while $N'\neq N$):
- determina un $n$ non in $N'$ tale che $D(n)$ sia minimo
- aggiungi $n$ a $N'$
- per ogni nodo $a$ adiacente a $n$ e non in $N'$, aggiorna $D(a)$:
	- $D(a) = min(D(a), D(n) + c(n,a))$

>[!example]- esempio 
>Dato il seguente grafo:
>
>![[D0.png|center|300]]
>
>l'algoritmo si comporta così:
>
>![[D1.png|center|400]]
>![[D2.png|center|400]]
>![[D3.png|center|400]]
>![[D4.png|center|400]]
>![[D5.png|center|400]]
>![[D6.png|center|400]]
>![[D7.png|center|400]]
>![[D8.png|center|400]]
>![[D9.png|center|400]]
>![[D10.png|center|400]]
>
>e produce quindi questo grafo a costo minimo:
>
>![[D11.png|center|400]]
>
>La tabella di inoltro (che contiene, per ogni destinazione, la coppia $(\text{dest, predecessore})$) di $u$ è:
>
> | destinazione | collegamento |
> | ------------ | ------------ |
> | $v$          | $(u,v)$      |
> | $x$          | $(u,x)$      |
> | $y$          | $(u,x)$      |
> | $w$          | $(u,x)$      |
> | $z$          | $(u,y)$      |
> 

## confronto tra link state e distance vector


|                              | **link state**                                                                                                                                                                                                                     | **distance vector**                                                                                                                                                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **complessità dei messaggi** | con $n$ nodi, $E$ collegamenti, implica l’invio di $O(nE)$ messaggi (ogni nodo deve conoscere il costo degli $E$ link)                                                                                                             | richiede scambi tra nodi adiacenti (il tempo di convergenza può variare)                                                                                                                                                    |
| **velocità di convergenza**  | l’algoritmo ha complessità $O(n^2)$ <small>(prima $n$ nodi, poi $n-1$, poi $n-2$... (gauss))</small>                                                                                                                               | può convergere lentamente; può presentare cicli di instradamento e il problema del conteggio infinito                                                                                                                       |
| **robustezza**               | OSPF è *più robusto* di RIP:<br>se un router funziona male, può comunicare via broadcast un costo sbagliato per uno dei suoi collegamenti connessi (ma non per altri); i nodi si occupano di calcolare soltanto le proprie tabelle | RIP è *meno robusto* di OSPF:<br>un nodo può comunicare cammini a costo minimo errati a tutte le destinazioni; la tabella di ciascun nodo può essere usata da altri (un calcolo errato si può diffondere per l’intera rete) |
## protocollo OSPF
 **Open Shortest Path First** è un protocollo di routing basato sull'algoritmo link state.
 - è *open* perché le specifiche del protocollo sono pubblicamente disponibili
 - utilizza il *flooding* e l'algoritmo di *Dijkstra* per determinare il percorso a costo minimo
	 - ogni volta che si verifica un **cambiamento nello stato** di un collegamento, il router manda informazioni d’instradamento a **tutti** gli altri router
	 - invia periodicamente (ogni 30 minuti) messaggi OSPF all’intero sistema autonomo, utilizzando il flooding

>[!tip] I messaggi OSPF vengono trasportati direttamente in datagrammi IP usando il numero di protocollo `89` nel campo `IP protocol`

### messaggi OSPF
- `hello`: usato da un router per annunciare la propria esistenza ai i vicini che conosce
- `database description`: risposta ad `hello`, consente a chi si è appena connessodi ottenere il LSDB 
- `link-state request`: usato per richiedere specifiche informazioni su un collegamento
- `link-state update`: messsaggio principale, usato da OSPF per la costruzione del LSDB
- `link-state ack`: riscontro ai link-state update (per fornire affidabilità)