(len() è $\Theta(1)$)

(in un dizionario, la ricerca al caso pessimo dà $O(n)$)

Raggiungibilità: $u$ è raggiungibile da $v$ se esiste un cammino che da $u$ arriva a $v$.

Connettività: comunque prendo due nodi, tra di essi c'è un cammino

Dato un grafo e un nodo, voglio sapere quali nodi posso raggiungere a partire da quel nodo.

DFS
- bisogna tenere traccia dei nodi già visitati (per non cadere in cicli)

Con una visita DFS, gli archi del grafo si dividono in attraversati (se portavano a nodi nuovi) e non attraversati.
I nodi visitati e gli archi attraversati formano un albero detto **albero DFS**.

> [!info] vettore dei padri
> L'albero DFS si può memorizzare tramite il **vettore dei padri** --> un vettore che contiene, per ogni entrata $i$, il suo nodo padre
> - (un nodo senza padre avrà se stesso)


L'obiettivo è modificare la visita DFS in modo da memorizzare anche il vettore dei padri.


- si sfrutta il vettore dei padri per controllare se un nodo sia stato visitato o meno

```python
def Padri(u, G):
	for y in G[x]:
		if P[y] == -1:
			P[y] = x
			DFSr(y, G, P)

n = len(G)
P = [-1]*n
P[u] = u
DFSr(u, G, P)
return P
```

### colorazione di grafi
Dato un grafo connesso $G$, si vuole trovare il minimo numero $k$ di colori necessari per colorare i nodi dell'albero in modo che **nodi adiacenti** abbiano sempre **colori distinti**.

- un grafo può richiedere anche $\Theta(n)$ colori.

>[!summary] teorema dei quattro colori
>Un grafo planare richiede al più *quattro colori* per essere colorato.

>[!bug] non è noto nessun algoritmo polinomiale che determini la 3-colorabilità

È invece facile determinare se un grafo è 2-colorabile:

>[!tip] un grafo è 2-colorabile se e solo se non contiene **cicli di lunghezza dispari**

### componente connessa
Una **componente connessa** di un grafo indiretto è un sottografo composto da un insieme *massimale* di nodi connessi da cammini.

### componente fortemente connessa
Una **componente fortemente connessa** di un grafo

- LEGGI TARJAN / KOSARAJU dai