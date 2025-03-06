## concetti base

>[!info] raggiungibilità
>Un nodo $u$ è raggiungibile da un nodo $v$ se esiste almeno un cammino che da $u$ arriva a $v$.

>[!tip] connettività
>Il problema della connettività si occupa di determinare se, comunque prendo due nodi $u$ e $v$, tra essi c'è un cammino.

## Depth-First Search (DFS)
La strategia della visita in profondità consiste nel visitare il grafo sempre più "in profondità" <small>(unexpected)</small>, quando possibile. Partendo da un nodo, si prosegue lungo un sentiero finché non si arriva a un punto che non ha più collegamenti da seguire, quindi si torna indietro per esplorare eventuali altri collegamenti dai nodi già visitati. Durante tutta la ricerca, **non si visitano mai** (all'"andata") **nodi già visitati**, per non cadere in cicli.

##### visita DFS su grafo rappresentato tramite matrice di adiacenza:
- usiamo un **vettore dei visitati** per tenere conto dei nodi già visitati: quando si trova un nodo $u$, lo si visita solo se $\text{visitati[u]==0}$ 
	- questo ci permette di non incorrere in cicli
 
```python
def DFS(u, M)
	visitati[u] = 1 
	for i in range(len(M)): # si scorrono i vicini di u - θ(n)
		if M[u][i] and not visitati[i]:
			DFS(i, M, visitati) # O(n) (entro massimo n volte)
			
# quindi questa funzione ha costo O(n)xΘ(n)

n = len(M)
visitati = [0]*n # Θ(n)
DFS(u, M, visitati)
return [x for x in range(n) if visitati[x]] # Θ(n)

# ^ prendo dai nodi (range della lunghezza delle liste) solo quelli che sono stati visitati
```

- al termine dell'esecuzione della funzione ricorsiva, si ha $\text{visitati[i]=1}$ se e solo se $i$ è raggiungibile da $u$.
- questo algoritmo ha costo $O(n)\times \Theta(n)=O(n^2)$

##### visita DFS su grafo rappresentato tramite liste di adiacenza:
```python
def DFS(u, G, visitati):
	visitati[u] = 1
	for v in G[u]: # O(n) (Θ(|vicini di u|))
		if not visitati[v]:
			DFS(v, G, visitati)

n = len(G)
visitati = [0]*n
DFS(u, G, visitati)
return [x for x in range(n) if visitati(x)]
```

Sappiamo che ogni lista di adiacenza 

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