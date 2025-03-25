>[!info] spanning tree
>Dato un grafo $G$, un **albero di copertura** (o ricoprente/di connessione/di supporto) è un qualsiasi sottografo $G'=(V',E')$ con $V'=V$, $E'\subseteq E$ che sia un albero (quindi che sia connesso e aciclico).
>- <small>(un albero di copertura  di un grafo connesso indiretto è un albero che contiene tutti i nodi del grafo e contiene soltanto un sottoinsieme degli archi: quelli necessari per connettere tra loro tutti i vertici con uno e un solo cammino)</small>

>[!tip] minimum spanning tree
>Sia $G$ un grafo indiretto connesso pesato. Un **albero di copertura minimale** è un suo albero di copertura $T\subseteq G$ tale che la somma di tutti i pesi degli archi di $T$ è minima rispetto a quella di tutti gli altri alberi di copertura.
> - un MST non è unico

>[!bug] se si ha un sottografo $G'=(V',E')$ connesso tale che $V'=V$ e tale che la somma dei pesi dei suoi archi sia minima, allora $G'$ è necessariamente un albero (e quindi un MST)
>- (sappiamo che albero = grafo connesso indiretto aciclico)
>- supponiamo che ci sia un ciclo in $G'$: vorrebbe dire che esiste almeno un arco che può essere eliminato senza che il grafo perda la sua connessione: questo contraddirebbe l'ipotesi per cui la somma dei pesi degli archi di $G'$ è minima. È perciò impossibile che ci siano cicli, e $G'$ (poiché $V'=V$ e $G'$ connesso) è quindi un albero.

Il problema è quindi trovare un sottoinsieme di archi che colleghi tutti i vertici e che abbia il minimo peso totale.
### algoritmo di Kruskal
L'algoritmo di Kruskal fornisce una soluzione al problema del minimo albero di copertura.

La logica che segue è questa:
- parte con il grafo $T$ che contiene tutti i nodi di $G$ e nessun arco di $G$
- considera uno alla volta gli archi del grafo $G$ in ordine di costo crescente
- se un arco non forma un ciclo in $T$ con archi già considerati, lo inserisce in $T$
- al termine restituisce $T$

Anche questo algoritmo rientra nel paradigma della **programmazione greedy**:
- (*decisioni irrevocabili*) una volta deciso se inserire o meno un arco in $T$, non ritorna più sulla decisione
- (*decisioni prese in base ad un criterio locale*) se un arco crea un ciclo, non lo si aggiunge; altrimenti, lo si sceglie in quanto è il meno costoso a non creare cicli 

**pseudocodice**:
```
kruskal(G):
	T = set()
	inizializza E con gli archi di G
	while E != []:
		estrai da E un arco (x,y) di peso minimo
		if l'inserimento di (x,y) non crea ciclo con gli archi in T:
			inserisci arco (x,y) in T
	return T
```

### dimostrazione di correttezza

>[!note] correttezza
>Dobbiamo mostrare che, al termine dell'algoritmo, $T$ è un albero di copertura e che non c'è un altro albero che costa meno.
>
>1) **produce un albero di copertura**
>
>Supponiamo, per assurdo, che al termine dell'algoritmo il sottoinsieme $T$ di archi non sia connesso. In tal caso, $T$ avrebbe più di una componente connessa. Poiché il grafo iniziale $G$ è connesso, esiste almeno un arco $(x,y)$ che connette due nodi $x$ e $y$ di due componenti diverse di $T$. 
>
>Se $(x,y)$ non è stato inserito in $T$, significa che è stato scartato perché avrebbe creato un ciclo. Tuttavia, dato che $(x,y)$ connette due componenti disconnesse, non potrebbe formare un ciclo, poiché non esiste un percorso precedente in $T$ che collega $x$ a $y$. Questo porta a una contraddizione, in quanto l'algoritmo scarta solo gli archi che causano cicli. Pertanto, il grafo $T$ deve essere connesso e aciclico (ovvero un albero).
>
>2) **non c'è un albero di copertura per $G$ che costa meno dell'albero $T$ ottenuto**
>
>Sia $T$ l'albero di copertura prodotto dall'algoritmo di Kruskal, e sia $T^*$ un altro albero di copertura con lo stesso costo minimo. Assumiamo che $T$ e $T^*$ differiscano: supponiamo che $T^*$ sia l'albero di copertura con lo stesso costo che differisce nel *minor numero* di archi da $T$. <small>(il numero di archi dei due rimane lo stesso, ma hanno x archi diversi con x minimo)</small> 
>
>Consideriamo l'ordine $e_{1},e_{2},\dots$ con cui gli archi sono stati presi in considerazione nel corso dell'algoritmo. Sia $e$ il primo arco che compare in $T$ e non in $T^*$. Se $e$ fosse inserito in $T^*$, creerebbe un ciclo $C$ <small>(perché $T^*$ è un albero di copertura, quindi l'aggiunta di un altro arco genererebbe necessariamente un ciclo)</small>. Il ciclo $C$ contiene almeno un arco $e'$ che non appartiene a $T$ (se tutti gli archi di $C$ fossero in $T$, allora l'algoritmo non avrebbe aggiunto $e$). 
>
>Consideriamo ora l'albero $T'$, ottenuto da $T^*$ inserendo $e$ ed eliminando $e'$. Il costo del nuovo albero $T'$ è $costo(T^*)-costo(e')+costo(e)$. Questo non può aumentare rispetto a quello di $T^*$, perché $costo(e)\leq costo(e')$ (perché tra $e$ ed $e'$, Kruskal ha considerato prima $e$).
>
>Quindi, $T'$ è un altro albero di copertura ottimo che differisce da $T$ in meno archi di quanto faccia $T^*$ (perché, rispetto a $T^*$, al posto dell'arco $e'$ ha l'arco $e$, che appartiene a $T$), il che contraddice l'ipotesi per cui $T^*$ differisce da $T$ nel minor numero di archi.
>
>![[kruskal-dim.png|center|400]]


### implementazione
- con un pre-processing, ordino gli archi nella lista $E$ così che, scorrendola, ottengo di volta in volta l'arco di costo minimo in tempo $O(1)$
- verifico che l'arco $(x,y)$ non formi ciclo in $T$ controllando se $y$ è raggiungibile da $x$ in $T$

```python
def kruskal(G):
	E = [(c,u,v) for un in range(len(G)) for v,c in G[u] if u < v].sort()
	T = [[] for _ in G]
	
	for c,u,v in E:
		if not connessi(u,v,T):
			T[u].append(v)
			T[v].append(u)
	return T
```

```python
def DFSr(a, b, T, visitati):
	visitati[a] = 1
	for z in T[a]:
		if z == b:
			return True
		if not visitati[z]:
			if DFSr(z, b, T, visitati):
				return True
	return false

def connessi(u,v,T):
	visitati = [0]*len(T)
	return DFSr(u, v, T, visitati)
```

- l'ordinamento esterno al `for` costa $O(m \log m)=O(m\log n)$ 
	- ($m\log m\leq m\log n^2=2 \,m\log n\in O(m\log n)$)
- il `for` fa $m$ iterazioni, e controllare che l'arco $(a,b)$ non crei un ciclo in $T$ costa quanto la visita di un grafo aciclico, ovvero $O(n)$
	- il `for` richiede quindi $O(m\cdot n)$

La complessità totale è $O(m\cdot n)$.

### implementazione con union-find
Union-Find (o Disjoint Set Union) è una struttura dati per gestire insiemi disgiunti che permette operazioni di unione e ricerca efficienti.

Le tre operazioni fondamentali sono:
- `Crea(C)`: restituisce una struttura dati Union-Find sull'insieme S di elementi dove ciascun elemento è in un insieme separato
- `Find(x,C)`: restituisce il nome dell'insieme nella struttura dati C a cui appartiene l'elemento x
- `Union(A,B,C)`: modifica la struttura dati C fondendo la componente A con la componente B e restituisce il nome della nuova componente




Ogni albero di altezza $k$ avrà al suo interno almeno $2^k$ elementi.
- *caso base*: $k=0$ --> c'è un nodo solo ($2^0$)
- *ipotesi induttiva*: gli alberi con altezza $k-1$ hanno almeno $2^{k-1}$ elementi

altezza diversa: uno $h$ e l'altro $k<h$.
Il primo ha $2^h$ nodi, il secondo $2^k$.
Si avrà un nuovo albero con altezza $h$, che avrà quindi almeno $2^h$ nodi.

