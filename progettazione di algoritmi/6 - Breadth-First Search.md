> [!info] distanza minima
> Dati due nodi $a$ e $b$ di un grafo $G$, definiamo **distanza minima** in $G$ di $a$ da $b$ il *numero minimo di archi* che bisogna attraversare per raggiungere $b$ a partire da $a$.
> - la distanza è posta a $+\infty$ se $b$ non è raggiungibile partendo da $a$

### visita in ampiezza
La visita in ampiezza esplora i nodi partendo da quelli a distanza $1$ dalla sorgente $s$. Poi visita quelli a distanza $2$ e così via.
- l'algoritmo visita quindi tutti i nodi a livello $k$ prima di passare a quelli a livello $k+1$.

![[BFS.png|center|450]]

L'algoritmo genera un albero detto **albero BFS**.

Per effettuare questa visita, si mettono in una *coda* i nodi visitati i cui adiacenti non sono ancora stati esaminati.
Ad ogni passo, si prende il primo nodo dalla coda, si esaminano i suoi adiacenti e, se si scopre un nuovo nodo, si visita e si aggiunge alla coda.

![[BFS-es.png|center|450]]

^ sulla destra i tre alberi BFS risultanti da tre visite BFS di $G$ a partire da $0$, $5$, $2$ rispettivamente

**processo**:
- si comincia con una coda contenente solo il nodo di partenza $x$.
- finché la coda non risulta vuota, ad ogni passo:
	- un nodo viene estratto dalla coda
	- tutti i suoi adiacenti vengono visitati e messi in coda

```python
def BFS(x, G):
	visitati = [0]*len(G)
	visitati[x] = 1
	coda = [x]

	while coda:
		u = coda.pop()
		for y in G[u]:
			if visitati[y] == 0:
				visitati[y] = 1
				coda.append(y) # va in coda solo se non visitato
	return visitati
```

