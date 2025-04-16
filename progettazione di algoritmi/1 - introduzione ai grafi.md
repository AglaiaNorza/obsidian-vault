---
created: 2025-03-22T10:30
updated: 2025-04-16T17:12
---
## grafi
Un grafo è formato da:
- **nodi**
- **archi**

Un grafo $G$ si indica come: $G(V,\,E)$, con:
- $V$ insieme dei vertici, 
- $E$ insieme degli archi ⟶ coppie di nodi

Si ha:
- $|V|=n$ <small>(numero di vertici)</small>
- $|E|=m$ <small>(numero di archi)</small>

> [!info] grado di un nodo 
> Il **grado** di un nodo è il numero di archi che incidono su un nodo.

>[!tip] somma dei gradi dei vertici, handshaking lemma
>Dato un grafo $G=(V,\,E)$, si ha che
>
>$$\sum_{v\in V}deg(v)=2m$$
>
><small>(la somma dei gradi di tutti i nodi è pari a $2m$).</small>
> 
>(si vede chiaramente che, per ogni arco $e\in E$, esistono esattamente due nodi ad esso incidenti, e di cui quindi esso aumenta il grado di 1)
>
>**corollario (handshaking lemma)**: Dato un grafo $G=(V,E)$, il numero dei nodi di $G$ che hanno grado dispari è pari.

>[!example] Se $G$ ha almeno due nodi, allora in $G$ ci sono due nodi con lo stesso grado.
>Prendiamo un grafo $G$ con $n=|V|\geq 2$. Ogni nodo può avere un grado che va da $0$ a $n-1$ <small>(ci sono quindi $n$ possibili gradi)</small>. 
>
>Se tutti gli $n$ nodi avessero grado diverso, allora vorrebbe dire necessariamente che un nodo dovrebbe avere grado $n-1$, e un altro $0$. 
>Ma la coesistenza di un nodo con grado $n-1$ e uno con grado $0$ è impossibile (se un nodo è connesso a tutti gli altri, non ce ne può essere un altro completamente isolato). Si ha quindi necessariamente che almeno due nodi hanno lo stesso grado.


>[!info] nodi adiacenti
>Due nodi $u,v$ si dicono **adiacenti** se l'arco $(u,v) \in E$ <small>(se sono connessi da un arco)</small>.


### grafi diretti e indiretti
Un grafo si dice **diretto** se i suoi archi hanno una **direzione**.
Altrimenti, si dice **indiretto**.

![[grafi-es.png|center|500]]

(a sinistra un grafo indiretto, a destra un grafo diretto)

>[!note] numero di archi
>- Se il grafo è *diretto*, il numero $m$ degli archi è: $0\leq m \leq n(n-1)$.
>- Se invece il grafo è *non diretto*, $0\leq m\leq{\frac{n(n-1)}{2}}$.
> 
>In entrambi i casi quindi, il numero $m$ di archi è in $O(n^2)$ (con $n=|V|$).

>[!info] pozzo
>In un grafo diretto, un **pozzo** è un nodo senza archi uscenti.
>- un *pozzo universale* è un pozzo verso cui tutti gli altri nodi hanno un arco.
>
>![[pozzi.png|center|450]]
>
>(a sinistra un pozzo, a destra un pozzo universale)

### grafi sparsi e densi
Un grafo si dice **sparso** se $m=O(n)$ <small> ("ha pochi archi"). </small>
Un grafo si dice invece **denso** se $m=\Omega (n^2)$.

Esempi di grafi *densi*:
- un grafo si dice **completo** se ha tutti gli archi ($n=\Theta(n^2)$)
- un grafo diretto si dice **torneo** se tra ogni coppia di nodi c'è esattamente un arco

Esempio di grafo *sparso*:
- un **grafo planare** è un grafo che si può disegnare sul piano senza che gli archi si intersechino.

>[!example] grafo planare
>![[grafo-planare.png|center|350]]

>[!example] più piccolo grafo non planare
>![[grafo-non-planare.png|center|200]]

> [!warning] un grafo non sparso non è necessariamente denso!
> esistono anche grafi con $\Theta(n \log n)$ archi.
### alberi

> [!info] def
> Un **albero** è un grafo sparso **connesso** (ogni nodo è connesso agli altri) **senza cicli**.

Un albero ha sempre $m=n-1$ archi.

>[!note]- si dimostra per induzione
>induzione sul numero $n$ di nodi.
>- $n=0$ ⟶ ci sono $0$ archi
>- ipotesi induttiva ⟶ assumiamo che sia vero per alberi con fino a $n-1$ nodi
>
>Per un albero da $n$ nodi, mettendo da parte una foglia e l'arco che incide su di essa, rimane un albero di $n-1$ nodi. Per ipotesi induttiva, questo avrà esattamente $n-2$ archi. Aggiungendo quindi l'ultimo nodo e il suo arco, si otterranno $n-1$ archi totali

Tutti gi alberi sono **grafi planari**.
## rappresentare i grafi

### rappresentazione tramite matrice
Uno dei modi più semplici per rappresentare un grafo è quello della **matrice di adiacenza**.

Dato un grafo di $n$ nodi, si costruisce una matrice binaria $n\times n$ con:
- $M[i][j]=1\iff$ c'è un arco diretto da $i$ a $j$

> [!example]- grafo indiretto
> Questo grafo:
> 
> ![[graph-1.png|center|200]]
> 
> Si rappresenta così:
>  
> $$ \begin{bmatrix}  0 & 0 & 1 & 0 & 0 & 1  \\ 0 & 0 & 0 & 0 & 0 & 1  \\ 1 & 0 & 0 & 0 & 1 & 1  \\ 0 & 0 & 0 & 0 & 1 & 0  \\ 0 & 0 & 1 & 1 & 0 & 1 \\ 1 & 1 & 1 & 0 & 1 & 0  \end{bmatrix} $$
> 
> (si nota che, poiché è un grafo indiretto <small>(quindi ogni arco entrante è anche uscente)</small>, la rappresentazione è **simmetrica rispetto alla diagonale** della matrice)

>[!example]- grafo diretto
> Questo grafo:
> 
>![[graph-2.png|center|200]]
> 
> Si rappresenta così:
>  
> $$ \begin{bmatrix}  0 & 0 & 1 & 0 & 0 & 1  \\ 0 & 0 & 0 & 0 & 0 & 0  \\ 0 & 0 & 0 & 0 & 0 & 0  \\ 0 & 0 & 0 & 0 & 1 & 0  \\ 0 & 0 & 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 0 & 0 & 0  \end{bmatrix} $$

- Uno dei **problemi** principali di questa matrice è lo *spreco di spazio*: se per esempio il grafo è sparso, si occuperanno solo fino a $n$ delle $n^2$ posizioni.
- Uno dei **vantaggi** principali è invece la *velocità* con cui si può controllare la presenza di un arco: basta accedere all'elemento in posizione $(u,v)$ - costa $O(1)$.

>[!summary]- costi
>I costi sono quindi:
>- presenza di un **arco**: $O(1)$
>- ricerca dei **nodi adiacenti**: $\Theta(n)$ (bisogna scorrere tutta la lista $M[i]$)
### rappresentazione tramite lista di adiacenza
Si utilizza una **lista di liste** $G$, con tanti elementi quanti sono i nodi del grafo $G$. 
- ogni elemento $G[x]$ è una lista che contiene i *nodi adiacenti* al nodo $x$.

>[!example]- grafo indiretto
>Il primo grafo:
> 
>![[graph-1.png|center|200]]
>
>Si rappresenta così:
>```python
>G = [
>	[2, 5],
>	[5],
>	[0, 4, 5],
>	[4],
>	[2, 3, 5],
>	[0, 1, 2, 4]
>]
>```

>[!example]- grafo indiretto
>Il secondo grafo:
> 
>![[graph-2.png|center|200]]
>
>Si rappresenta così:
>```python
>G = [
>	[2, 5],
>	[],
>	[],
>	[4],
>	[2, 3, 5],
>	[0, 1]
>]
>```

- Rispetto alla rappresentazione tramite matrice, il *risparmio di spazio* è notevole.
- Però, vedere se due archi sono connessi o meno può arrivare a costare $O(n)$ (bisogna scorrere la lista dei nodi adiacenti al nodo $u$ per verificare se $v$ sia presente).

>[!summary]- costi
>I costi sono quindi:
>- presenza di un **arco**: worst case: $O(n)$
>- ricerca dei **nodi adiacenti**: worst case: $O(n)$ 
## esercizio: verificare se un grafo diretto ha un pozzo universale
In questo caso, è più comodo utilizzare la rappresentazione tramite matrice - essa ci permette infatti di risolvere il problema in $\Theta(n)$. 

Osserviamo un esempio di un pozzo universale in questa rappresentazione:
$$\begin{bmatrix} 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \end{bmatrix}$$

C'è un semplice test che ci permette di eliminare uno dei due nodi rappresentati da ogni posizione della matrice:
$$
M[i][j] = \begin{cases} 1 & i \ \text{ non è pozzo } \\ 0 & j \ \text{ non è pozzo universale} \end{cases}
$$

- se $M[i][j]==1$, sicuramente so che $i$ (la riga, ovvero il nodo da cui l'arco parte) non è un pozzo ⟶ infatti, c'è un arco che parte da esso
- se $M[i][j]==0$, so che $j$ non è pozzo universale ⟶ non c'è un arco entrante in $j$ (ma potremmo trovarci nella situazione $(2,2)$ dell'esempio, quindi non escludiamo $i$)

Quindi, una soluzione sarebbe:
```python
def pozzo(M):
n = len(M)
L = [x for x in range(n)]; # creo una lista con tutti i nodi

# prendo due nodi per controllare
while len(L)>1:
	a = L.pop() # uso pop perché è O(1)
	b = L.pop()
	if M[a][b]: # se è 1
		L.append(b) # a non è pozzo, quindi teniamo b
	else:
		L.append(a) # b non è pozzo universale, quindi teniamo a

L.pop()
for j in range(n): # controllo la riga 
	if M[x][j]: 
		return False # se non sono tutti zeri, non è pozzo univ.

for i in range(n):
	if i != x and M[i][x] == 0:
		return False # se ci sono zeri oltre a quello in (x,x), ""

return True
```