> [!info] distanza minima
> Dati due nodi $a$ e $b$ di un grafo $G$, definiamo **distanza minima** in $G$ di $a$ da $b$ il *numero minimo di archi* che bisogna attraversare per raggiungere $b$ a partire da $a$.
> - la distanza è posta a $+\infty$ se $b$ non è raggiungibile partendo da $a$

## visita in ampiezza
La visita in ampiezza esplora i nodi partendo da quelli a distanza $1$ dalla sorgente $s$. Poi visita quelli a distanza $2$ e così via.
- l'algoritmo visita quindi tutti i nodi a livello $k$ prima di passare a quelli a livello $k+1$.

![[BFS.png|center|450]]

L'algoritmo genera un albero detto **albero BFS**.

Per effettuare questa visita, si mettono in una *coda* i nodi visitati i cui adiacenti non sono ancora stati esaminati.
Ad ogni passo, si prende il primo nodo dalla coda, si esaminano i suoi adiacenti e, se si scopre un nuovo nodo, si visita e si aggiunge alla coda.

![[BFS-es.png|center|450]]

^ sulla destra i tre alberi BFS risultanti da tre visite BFS di $G$ a partire da $0$, $5$, $2$ rispettivamente

### implementazione naïf
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

>[!note]- dimostrazione della correttezza TODO
>alla fine dell'algoritmo, $\text{visitati}[u] = 1\iff\text{il nodo } u \text{ è raggiungibile da } x$
>
>- se $u$ è raggiungibile da $x$, allora $\text{visitati}[u]=1$
>
>Se $u$ è raggiungibile, c'è un cammino $P$ da $x$ a $u$. Supponiamo per assurdo che al termine, $\text{visitati}[u]=0$. Sia $b$ il primo nodo che si incontra nel cammino $P$ con $v[b]=0$ e $a$ il suo predecessore
>TODO finisci

### implementazione in $O(n+m)$
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

> [!info]- implementazione con `deque`
> Il modulo `Collections` di python contiene la struttura dati `deque` (double-ended queue) (è implementata tramite una doubly linked list)
> 
> ![[deque.png|center|300]]
>  
> ```python
> def BFS(x, G):
> 	visitati=[0]*len(G)
> 	visitati[x] = 1
> 	from collections import deque
> 	coda = deque([x])
> 	while coda:
> 		u = coda.popleft()
> 		for y i G[u]:
> 			if visitati[y] == 0:
> 				visitati[y] = 1
> 				coda.append(y)
> 	return visitati
> ```

### albero BFS
La procedura può essere modificata in modo da restituire in $O(n+m)$ l'albero di visita BFS rappresentato tramite vettore dei padri.

> [!example] albero BFS
> ![[BFS-tree.png|center|400]]

```python
def BFSpadri(x, G):
	P = [-1]*len(G)
	P[x] = [x]
	coda = [x]
	i = 0
	while len(coda) > i:
		u = coda[i]
		i += 1
		for y in G[u]:
			if P[y] == -1:
				P[y] = u
				coda.append(y)
```

>[!info] cammino
>grazie al vettore dei padri $P$, come già visto per la visita DFS, con la [[1 - visita DFS, colorabilità, componenti connesse#trovare un cammino|procedura]] $\text{Cammini(x, P)}$, si può ottenere in $O(n)$ un cammino dalla radice dell'albero al nodo $x$.

Però, in più, vale anche:
>[!tip] la distanza minima di un vertice $x$ da $s$ (radice) nel grafo $G$ equivale alla **profondità** di $x$ nell'albero BFS.
>>[!note] dimostrazione
>>Si dimostra per induzione sulla distanza $d$ di $x$ da $s$. 
>>- *caso base*: è banalmente vero per $d=0$, in quanto $s$ è l'unico vertice a distanza $0$ da se stesso, ed ha profondità $0$ nell'albero.
>>- *ipotesi induttiva*: supponiamo sia vero per tutti i vertici a distanza al più $d-1$.
>>
>>Consideriamo un vertice $x$ a distanza $d$. Sia $P$ un **cammino minimo** da $s$ a $x$, e sia $v$ il predecessore di $x$ in questo cammino. Per ipotesi induttiva sappiamo che $v$ è a profondità $d-1$.
>>- se $x$ è stato inserito nell'albero grazie a $v$ (è stato esplorato partendo da $v$), allora sappiamo che si troverà a distanza $d$.
>>
>>Supponiamo quindi che sia stato inserito grazie ad un nodo $u\neq v$.
>> 
>>La profondità di $u$ non può essere inferiore a $d-1$, o avremmo trovato un cammino $s\to u\to x$ di lunghezza inferiore a $d$ (il che contraddirebbe l'ipotesi iniziale). Ma la profondità di $u$ non può essere maggiore di $d-1$, perché il nodo $v$ sarebbe stato visitato prima di $u$ e $x$ sarebbe stato inserito grazie a $v$. Quindi, si ha necessariamente che la profondità di $u$ è $d-1$, e che la profondità di $v$ è $d$.

### vettore delle distanze
La procedura può anche essere modificata in modo da restituire in $O(n+m)$ il **vettore delle distanze** $D$.
- al nodo $x$ viene assegnata distanza zero, e a tutti gli altri $-1$ - a ciascun nodo via via visitato viene assegnata la distanza del padre incrementata di $1$.
- al termine della procedura, $D[u]$ conterrà $-1$ se il nodo $u$ non è raggiungibile da $x$, e la distanza minima di $u$ da $x$ altrimenti.

```python
def BFSdistanze(x, G):
	D = [-1]*len(G)
	D[x] = 0
	coda = [x]
	i = 0
	while len(coda) > i:
		u = coda[i]
		i += 1
		for y in G[u]:
			if D[y] == -1:
				D[y] = D[u] + 1
				coda.append(y)
	return D
```