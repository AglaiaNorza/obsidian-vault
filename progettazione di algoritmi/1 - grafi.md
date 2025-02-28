## grafi
Un grafo è formato da:
- nodi
- archi

Un grafo $G$ si indica come: $G(V,\,E)$ (con 
- $V$ insieme dei vertici, 
- $E$ insieme degli archi --> coppie di nodi

Un grafo si dice **diretto** se i suoi archi hanno una **direzione**.
Altrimenti, si dice **indiretto**.

Se il grafo è diretto, il numero $m$ degli archi è: $0\leq m \leq n(n-1)$.
Se invece il grafo è non diretto, $0\leq m\leq{\frac{n(n-1)}{2}}$.

In entrambi i casi quindi, il numero $m$ di archi è in $O(n^2)$ (con $n=|V|$).

Un grafo si dice **sparso** se $m=O(n)$ <small> (ha pochi archi). </small>
Un grafo si dice invece **denso** se $m=\Omega (n^2)$.

Esempi di grafi *densi*:
- un grafo si dice **completo** se ha tutti gli archi ($n=\Theta(n^2)$)
- un grafo diretto si dice **torneo** se tra ogni coppia di nodi c'è esattamente un arco

> [!warning] un grafo non sparso non è necessariamente denso!
> esistono anche grafi con $\Theta(n \log n)$ archi.
### albero 

> [!info] def
> Un **albero** è un grafo **connesso** (ogni nodo è connesso agli altri) **senza cicli**.

Un albero ha sempre $m=n-1$ archi.

Il **grado** di un nodo è il numero di archi in cui è coinvolto il nodo (= numero di figli)
