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

#### implementazione naïf
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

- un nodo finisce in coda al più una volta, quindi il `while` viene eseguito $O(n)$ volte
- le liste di adiacenza dei nodi verranno scorse al più una volta, quindi il costo totale dei `for y in G[u]` è $O(m)$
- però, l'estrazione in testa da una lista (`pop()`) ha costo proporzionale al numero di elementi presenti nella lista, ovvero anche $O(n)$

quindi, il *costo* totale dell'algoritmo è $O(n^2)$.

>[!bug]- caso pessimo
>
>![[bfs-worst.png|center|300]]
>
>Un esempio di caso pessimo per questo algoritmo è quello di un grafo in cui un nodo fa da sorgente e tutti gli altri sono pozzi.
>In questo caso, tutti i nodi verranno inseriti nella coda (in quanto adiacenti alla sorgente), e verranno poi eseguite una serie di estrazioni dalla coda con costo decrescente da $n$. Il costo complessivo sarà quindi $\Theta(n^2)$ <small>($O(n)$ del while $\times O(n)$ dei `pop()`)</small>

>[!note]- dimostrazione della correttezza
>alla fine dell'algoritmo, $\text{visitati}[u] = 1\iff\text{il nodo } u \text{ è raggiungibile da } x$
>
>- se $u$ è raggiungibile da $x$, allora $\text{visitati}[u]=1$
>
>Se $u$ è raggiungibile, c'è un cammino $P$ da $x$ a $u$. Supponiamo per assurdo che al termine, $\text{visitati}[u]=0$. Sia $b$ il primo nodo che si incontra nel cammino $P$ con $v[b]=0$ e $a$ il suo predecessore
>TODO finisci

#### implementazione in $O(n+m)$
Se si potesse eseguire un `pop()` in $O(1)$, l'algoritmo costerebbe $O(n+m)$ - basta non eseguire effettivamente le cancellazioni, ma semplicemente utilizzare un puntatore per indicare l'inizio della coda all'interno della lista (incrementandolo ogni volta che si "cancella" dalla coda).

```python 
def BFS(x, G):
	visitati = [0]*len(G)
	visitati[x] = 1
	coda = [x]
	i = 0
	while len(coda) > i:
		u = coda[i]
		i += 1
		for y in G[u]:
			if visitati[y] == 0:
				visitati[y] = 1
				coda.append(y)
	return visitati
```

>[!info] implementazione con `deque`