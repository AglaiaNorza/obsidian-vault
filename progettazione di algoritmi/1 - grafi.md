## grafi
Un grafo è formato da:
- nodi
- archi

Un grafo $G$ si indica come: $G(V,\,E)$ (con 
- $V$ insieme dei vertici, 
- $E$ insieme degli archi --> coppie di nodi

Un grafo si dice **diretto** se i suoi archi hanno una **direzione**.
Altrimenti, si dice **indiretto**.

>[!info] pozzo
>In un grafo diretto, un **pozzo** è un nodo senza archi uscenti.
>- un *pozzo universale* è un pozzo verso cui tutti gli altri nodi hanno un arco.

Se il grafo è diretto, il numero $m$ degli archi è: $0\leq m \leq n(n-1)$.
Se invece il grafo è non diretto, $0\leq m\leq{\frac{n(n-1)}{2}}$.

In entrambi i casi quindi, il numero $m$ di archi è in $O(n^2)$ (con $n=|V|$).

Un grafo si dice **sparso** se $m=O(n)$ <small> (ha pochi archi). </small>
Un grafo si dice invece **denso** se $m=\Omega (n^2)$.

Esempi di grafi *densi*:
- un grafo si dice **completo** se ha tutti gli archi ($n=\Theta(n^2)$)
- un grafo diretto si dice **torneo** se tra ogni coppia di nodi c'è esattamente un arco

Esempio di grafo *sparso*:
Un **grafo planare** è un grafo che si può disegnare sul piano senza che gli archi si intersechino.

>[!example] grafo planare
>![[grafo-planare.png|center|350]]

>[!example] più piccolo grafo non planare
>![[grafo-non-planare.png|center|200]]

> [!warning] un grafo non sparso non è necessariamente denso!
> esistono anche grafi con $\Theta(n \log n)$ archi.
### albero 

> [!info] def
> Un **albero** è un grafo **connesso** (ogni nodo è connesso agli altri) **senza cicli**.

Un albero ha sempre $m=n-1$ archi.

Tutti gi alberi sono **grafi planari**.

>[!note]- si dimostra per induzione
>induzione sul numero $n$ di nodi.
>- $n=0$ ci sono $0$ archi
>- ipotesi induttiva: assumiamo che sia vero per alberi con fino a $n-1$ nodi
>
>per un albero da $n$ nodi, mettendo da parte una foglia e l'arco

Il **grado** di un nodo è il numero di archi che incidono su un nodo (= numero di figli).

[ slide 7 ]

## rappresentare i grafi

### rappresentazione tramite matrice
Uno dei modi più semplici per rappresentare un grafo è quello della **matrice di adiacenza**.

Dato un grafo di $n$ nodi, si costruisce una matrice $n\times n$ con:
- $M[i][j]=1\iff$ c'è un arco diretto da $i$ a $j$

[ immagine slide sbagliata, manca un 1 seconda posizione ultima riga ]

Uno dei problemi principali di questa matrice è lo *spreco di spazio*: se per esempio il grafo è sparso, si occuperanno solo fino a $n$ delle $n^2$ posizioni.

Se il grafo è non diretto, la matrice sarà simmetrica con diagonale nulla.

### rappresentazione tramite lista di adiacenza
Si utilizza una lista di liste $G$, con tanti elementi quanti sono i nodi del grafo $G$. Ogni $G[x]$ è una lista che contiene i nodi adiacenti al nodo $x$ (quelli raggiunti da archi che partono da $x$).