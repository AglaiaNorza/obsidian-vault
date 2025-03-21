## concetti base

>[!info] raggiungibilità
>Un nodo $u$ è raggiungibile da un nodo $v$ se esiste almeno un cammino che da $u$ arriva a $v$.

>[!tip] connettività
>Il problema della connettività si occupa di determinare se, comunque prendo due nodi $u$ e $v$, tra essi c'è un cammino.

## Depth-First Search (DFS)
La strategia della visita depth-first consiste nel visitare il grafo sempre più "in profondità" <small>(unexpected)</small>, quando possibile. Partendo da un nodo, si prosegue lungo un sentiero finché non si arriva a un nodo che non ha più archi da seguire, quindi si torna indietro per esplorare eventuali altri archi dai nodi già visitati. Durante tutta la ricerca, **non si visitano mai** (all'"andata") **nodi già visitati**, per non cadere in cicli.

##### visita DFS su grafo rappresentato tramite matrice di adiacenza:
- usiamo un **vettore dei visitati** per tenere conto dei nodi già visitati: quando si trova un nodo $u$, lo si visita solo se $\text{visitati[u]==0}$ 
 
```python
def DFS(u, M)
	visitati[u] = 1 
	for i in range(len(M)): # si scorrono i vicini di u - θ(n)
		if M[u][i] and not visitati[i]:
			DFS(i, M, visitati) # O(n) (entro massimo n volte)
			
# ^ quindi questa funzione ha costo O(n)xΘ(n)

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
	for v in G[u]:
		if not visitati[v]:
			DFS(v, G, visitati)

# ^ questa funzione ha costo O(n+m)

n = len(G)
visitati = [0]*n
DFS(u, G, visitati)
return [x for x in range(n) if visitati(x)] # Θ(n)
```

Per ogni nodo $u$, l'algoritmo scorrerà la lista dei suoi adiacenti. Il ciclo for avrà quindi complessità $|\text{adj } 0|+|\text{adj } 1+\dots+ |\text{adj } n-1|$ (somma degli elementi nelle liste di tutti i nodi visitati), che, visto che non si visiterà mai un nodo due volte, corrisponde a $m$ <small>(numero di archi)</small> nel caso in cui il grafo è diretto, o $2m$ nel caso di un grafo indiretto.
- in entrambi i casi, la somma di tutte le iterazioni del ciclo for sarà quindi in $O(n)$

Il costo totale sarà quindi $O(n+m)$.
- se il grafo è sparso, $m\in O(n)$, quindi la complessità temporale totale sarà $O(n)$
###### versione iterativa
```python
def DFS_i(u, G):
	visitati = [0]*len(G)
	stack = [u]
	while stack:
		u = stack.pop()
		if not visitati[u]:
			visitati[u] = 1
			
			for v in G[u]:
				if not visitati[v]:
					stack.append(v)
					
	return [x for x in range(len(G)) if visitati[x]]
```

- anche qui, la complessità temporale è $O(n+m)$
### albero DFS
Visto che la ricerca visita solo nodi non precedentemente visitati, con una visita DFS, gli archi del grafo si dividono in attraversati e non attraversati.
I nodi visitati e gli archi attraversati formano un albero detto **albero DFS**.

> [!info] vettore dei padri
> L'albero DFS si può memorizzare tramite il **vettore dei padri** --> un vettore che contiene, per ogni entrata $i$, l'indice del suo nodo padre.
> - (per convenzione, il padre della radice è essa stessa - $P[r]==r$)
> - se $i$ non è un nodo dell'albero (in questo caso, se non è stato visitato), $P[i]==-1$

![[albero-DFS.png|center|500]]

(a sinistra un grafo, a destra i tre alberi DFS che si ottengono partendo dai nodi 9, 4 e 3 rispettivamente)

>[!example] esempio
>
>![[vettore-padre.png|center|200]]
>
>per esempio, questo albero sarà rappresentato dal seguente vettore dei padri:
>
>$P = \begin{array}{|c|c|c|c|c|c|c|c|c|c|} \hline 5 & 0 & 5 & 2 & 7 & 5 & 1 & 2 & 5 & 1 \\ \hline \end{array}$

La visita DFS può essere modificata in modo da memorizzare il vettore dei padri anziché quello dei visitati.

```python
def DFSp(x, G, P):
	for y in G[x]:
		if P[y] == -1:
			P[y] = x
			DFSp(y, G, P)

def padri(u, G):
	n = len(G)
	P = [-1]*n
	P[u] = u
	DFSr(u, G, P)
	return P
```

- al termine dell'algoritmo, $P[v] == -1$ se non è stato visitato. altrimenti, contiene il padre di $v$ 

### trovare un cammino
Molto spesso non basta sapere se un nodo $v$ sia raggiungibile da un nodo $u$, ma si vuole anche determinare un **cammino** che permetta di arrivare da $u$ a $v$.
- il vettore dei padri rende questa operazione molto semplice: basta controllare che il nodo $v$ sia nell'albero DFS, ed effettuare un reverse dei nodi incontrati

**versione iterativa**:
```python
def Cammino(u, P):
	if P[u] ==  -1: return [] # se non è nell'albero (non visitato)
	path = []
	while P[u] != u: # se P[u] = u, siamo arrivati al nodo che cerchiamo
		path.append(u)
		u = P[u] # seguiamo i padri
	path.append(u)
	path.reverse()
	return path
```

**versione ricorsiva**:
```python
def CamminoR(u, P):
	if P[u] == -1: return []
	if P[u] == u: return [u]
	return CamminoR(P[u], P) + [u]
```

- in entrambi i casi, disponendo del vettore dei padri, la complessità è $O(n)$

>[!warning] attenzione
>se esistono più cammini da $u$ a $v$, la procedura *non garantisce la restituzione del cammino minimo*

## colorazione di grafi

Dato un grafo connesso $G$, si vuole trovare il minimo numero $k$ di colori necessari per colorare i nodi dell'albero in modo che **nodi adiacenti** abbiano sempre **colori distinti**.

- un grafo può richiedere anche $\Theta(n)$ colori.

>[!summary] teorema dei quattro colori
>Un grafo planare richiede al più *quattro colori* per essere colorato.

>[!bug] non è noto nessun algoritmo polinomiale che determini la 3-colorabilità

### 2-colorabilità
È invece facile determinare se un grafo è 2-colorabile:

>[!tip] un grafo è 2-colorabile se e solo se non contiene **cicli di lunghezza dispari**

L'algoritmo di bi-colorazione che prova che un grafo senza cicli dispari può sempre essere 2-colorato funziona così:
- colora il nodo 0 con il colore 0
- effettua una visita in profondità del grafo a partire dal nodo 0 - nel corso della visita, assegna ad ogni nodo il colore (tra 0 e 1) opposto a quello assegnato al suo nodo padre

>[!note] prova di correttezza
>Siano $x$ e $y$ due nodi adiacenti in $G$. Consideriamo i due casi e verifichiamo che, in ogni caso, i due nodi avranno colori opposti.
>1) L'arco $(x,y)$ viene attraversato durante la visita --> banalmente i due nodi hanno colori diversi
>2) L'arco $(x,y)$ non viene attraversato durante la visita:
>	- sia $x$ il nodo visitato prima. Esiste un cammino che da $x$ porta a $y$ - questo cammino si chiuderà a formare un ciclo con l'arco $(y,x)$. Per ipotesi, il ciclo è di lunghezza pari, quindi il cammino è di lunghezza dispari. Poiché sul cammino i colori si alternano, il primo nodo ($x$) e il secondo ($y$) avranno colori diversi. 

**algoritmo di bi-colorazione** (sapendo che $G$ non ha cicli dispari):
- se $G$ contiene cicli dispari, produce una colorazione sbagliata
 
```python
def Colora(x, G, Colore, c):
	Colore[x] = c
	for y in G[x]:
		if Colore[y] == -1: # se non colorato
			Colora(y, G, Colore, 1-c)
			# 1-c alterna i colori (1-0 = 1, 1-1 = 0)

Colore = [-1]*len(G)
Colora(0, G, Colore, 0)
return Colore
```

**algoritmo che produce una bi-colorazione se $G$ è bicolorabile, altrimenti ritorna una lista vuota**:
```python
def Colora(x, G, Colore, c):
	Colore[x] = c
	for y in G[x]:
		if Colore[y]==-1:
			if not Colora(y, G, Colore, 1-c): 
				return False
		elif Colore[y] == Colore[x]:
			return False
	return True

def main()
	Colore = [-1]*len(G)
	if Colora(0, G, Colore, 0):
		return Colore
	return []
```

- la complessità è quella di una semplice visita di un grafo connesso: $O(n+m)=O(m)$ <small>(in un grafo connesso, $m\geq n-1$)</small>
## componente connessa
Una **componente connessa** (o semplicemente "componente") di un grafo <u>indiretto</u> è un sottografo composto da un *insieme massimale di nodi connessi da cammini*.

>[!tip] grafo connesso
>Un grafo indiretto si dice connesso se ha **una sola componente**.

esempio di grafo con 5 componenti: 
 
![[componenti-grafo.png|center|400]]

Si può calcolare il **vettore delle componenti connesse** di un grafo $G$.
Il vettore ($C$) ha tanti elementi quanti sono i nodi del grafo, e $C[u]=C[v]\iff$ $u$ e $v$ sono nella stessa componente connessa.

Per l'esempio sopra, il vettore sarebbe: 
 
$C = \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|} \hline 1 & 2 & 1 & 3 & 4 & 5 & 1 & 2 & 2 & 2 & 1 & 3 & 5 & 2 & 5 & 2 & 1 & 5  & 3 \\ \hline \end{array}$

**algoritmo per il vettore delle componenti connesse**:
```python
def Componenti(x, G, C, c):
	C[x] = c
	for y in G[x]:
		if C[y] == 0:
			Componenti(y, G, C, c)

def main(G):
	C = [0]*len(G)
	c = 0
	for x in range(len(G)):
		if C[x] == 0:
			c+=1
			Componenti(x, G, C, c)
	return C
```

- questo algoritmo ha complessità $O(n+m)$
## componente fortemente connessa
Una **componente fortemente connessa** di un grafo <u>diretto</u> è un sottografo composto da un insieme massimale di nodi connessi da cammini.

- come per i grafi indiretti, un grafo diretto si dice **fortemente connesso** se ha una sola componente.

esempio di grafo con 5 componenti:

![[comp-FC.png|center|300]]

$C = \begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|} \hline 1 & 1 & 2 & 1 & 1 & 3 & 1 & 1 & 4 & 5 & 4 & 4\\ \hline \end{array}$

>[!bug] attenzione
>l'algoritmo per le componenti connesse non funziona nel caso di componenti fortemente connesse: infatti, se c'è un cammino da $x$ a $y$, non è detto che ce ne sia anche uno da $y$ a $x$.

Per scrivere un algoritmo che, dato un grafo diretto $G$ ed un suo nodo $u$, calcola i nodi della componente fortemente connessa che contiene $u$, è utile creare il **grafo trasposto** $G^T$ di $G$.

>[!tip] grafo trasposto
>Dato un grafo diretto $G$, il suo grafo trasposto $G^T$ ha gli stessi nodi di $G$, ma **archi con direzione opposta**.
>
>(quindi, se facciamo una DFS a partire da un nodo $u$, otterremo tutti i nodi che, in $G$, portano a $u$)

#### algoritmo
Un possibile algoritmo per trovare il vettore delle componenti fortemente connesse funziona quindi così:
 
1) si calcola l'insieme $A$ dei nodi raggiungibili da $u$ 
	- semplice visita DFS 
	- $O(n+m)$
2) si costruisce il grafo trasposto $G^T$ 
	- $O(n+m)$
3) si calcola l'insieme $B$ dei nodi che portano a $u$
	- visita DFS su $G^T$
	- $O(n+m)$
4) si restituisce l'*intersezione* dei due insiemi $A$ e $B$ - $\Theta(n)$
	- a questo punto si hanno due vettori dei visitati (con la stessa cardinalità) - si scorrono semplicemente gli indici e si controlla per quali nodi entrambi hanno valore $1$ 
	- $O(n)$

**algoritmo per trovare la componente fortemente connessa di un nodo**:
```python
def ComponenteFC(x, G):
	visitati = DFS(x,G)
	GT = Trasposto(G)
	visitatiT = DFS(x, GT)
	
	componente = []
	for i in range(len(G)):
		if visitati[i] == visitatiT[i] == 1:
			componente.append(i)
	return componente
```

```python
def Trasposto(G):
	GT = [ [] for _ in G]
	for i in range(len(G)):
		for v in G[i]:
			GT[v].append(i) 
# (metto il nodo sorgente nella lista di adiacenza del n. destinazione)
	return GT
```

questo algoritmo può essere usato come subroutine per trovare le componenti fortemente connesse di tutti i nodi:

**algoritmo per trovare il vettore delle componenti FC**:
```python
def compFC(G):
	FC = [0]*len(G)
	c = 0
	for i in range(len(G)):
		if FC[i] == 0: 
			E = ComponenteFC(i, G) 
			# ^ ritorna un array con i numeri dei nodi nella comp.
			c+=1
			for x in E:
				FC[x] = c
	return FC
```

Al *caso pessimo*, la complessità sarà $O(n^3)$.
Consideriamo il caso di un grafo diretto $G$ avente un arco $(u,v)$ per ogni $u\leq v$.
- facciamo $n$ visite, di cui ognuna costa $O(n+m)$
- ma gli archi sono $\frac{n (n-1)}{2}=O(n^2)$, quindi:
- $O(n)\times O(n^2)=O(n^3)$

Esistono algoritmi che lavorano in tempo $O(n+m)$, come l'algoritmo di Tarjan e quello di Kosaraju (li aggiungerò for funsies prima o poi ma non fanno parte del programma).