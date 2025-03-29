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
