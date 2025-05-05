---
created: 2025-05-05T20:03
updated: 2025-05-05T22:03
---
Il protocollo OSPF è un algoritmo di routing basato su **link state**.
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
Si utilizza l'**algoritmo di Dijkstra** <small>[ trattato anche [[9 - grafi pesati, algoritmo di Dijkstra|qui]] (progettazione di algoritmi) ]</small> per calcolare il cammino di costo minimo da un nodo a tutti gli altri 