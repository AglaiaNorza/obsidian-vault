>[!info] grafo pesato
>Un grafo $G$ è detto **pesato** se ad ogni arco $e\in E$ è associato un valore numerico (detto *peso*) <small>(funzione $w:E\to R$ associa ad ogni arco un peso)</small>.
>- il *peso di un cammino* $P$ è dato dalla somma dei pesi degli archi che lo costituiscono

>[!example]- analogia dei contenitori d'acqua
>Abbiamo tre contenitori d'acqua con capienza 4, 7 e 10 litri. Inizialmente, i contenitori da 4 e 7 litri sono pieni, mentre quello da 10 è vuoto. Possiamo fare un solo tipo di operazione: versare acqua da un contenitore ad un altro, fermandoci quando il contenitore sorgente è vuoto o quello destinazione pieno.
>
>Vogliamo sapere se esiste una sequenza di operazioni di versamento che termina lasciando esattamente 2L di acqua nel contenitore da 4 o nel contenitore da 7.
>
>Il problema si può modellare con un grafo $G$:
>- i *nodi* di $G$ rappresentano i possibili stati di riempimento dei contenitori (tramite una configurazione $(a,b,c)$ dove le tre lettere rappresentano il numero di litri nei tre contenitori)
>- c'è un *arco* tra un nodo $(a,b,c)$ a un nodo $(a',b',c')$ se dallo stato $(a,b,c)$ è possibile passare allo stato $(a',b',c')$ con un versamento lecito
>
>![[grafo-acqua.png|center|300]]
>
> Per risolvere il problema, basta chiedersi se nel grafo diretto $G$ almeno uno dei nodi $(2,*,*)$ o $(*,2,*)$ è raggiungibile a partire dal nodo $(4,7,0)$.
> - per facilitare la ricerca, possiamo aggiungere un nodo pozzo $(-1,-1,-1)$ con archi entranti solo dai nodi $(2,*,*)$ e $(*,2,*)$, e chiederci se questo sia raggiungibile da $(4,7,0)$ 
> - per raggiungere uno dei due target con il minimo numero di travasi ci basta effettuare una visita BFS per la ricerca dei cammini minimi, calcolando le distanze minime a partire da $(4,7,0)$ ($O(n+m)$)
>
> Consideriamo però questa variante del problema: consideriamo una sequenza di operazioni di versamento come *buona* se termina lasciando esattamente 2 litri in uno dei due contenitori. Inoltre, una sequenza buona è *parsimoniosa* se il totale dei litri versati in tutti i versamenti della sequenza è *minimo* rispetto a tutte le sequenze buone. Cerchiamo una sequenza buona e parsimoniosa.
> 
> Ci conviene aggiungere un costo ad ogni arco per rappresentare il numero di litri che vengono versati nella mossa corrispondente.
> 
> ![[grafo-acqua2.png|center|400]]
> 
> Trovare un cammino dal nodo $(4.7,0)$ al pozzo $(-1,-1,-1)$ che minimizzi la somma dei costi degli archi attraversati diventa una generalizzazione del problema dei cammini di lunghezza minima.
> 
> Possiamo infatti sostituire un arco da $x$ a $y$ di costo $C$ con un cammino con $C-1$ nuovi nodi - in questo modo, ogni arco corrisponde al versamento di 1L d'acqua, e contando gli archi di un cammino tra due nodi contiamo esattamente il numero di litri versati. Basta quindi eseguire una BFS nel nuovo grafo. Essa avrà complessità $O(n'+m')$ con $n'$ e $m'$ nodi e archi del nuovo grafo.
> 
> Abbiamo ricondotto un problema di cammini minimi su grafi pesati ad uno di cammini minimi in un grafo non pesato. Ma questo approccio è possibile solo quando gli archi hanno pesi interi e relativamente piccoli.
> 
> Esiste quindi un algoritmo che ci permette di risolvere il problema dei cammini minimi lavorando direttamente su grafi pesati.

## algoritmo di Dijkstra
>[!bug] problema:
>Dato un grafo pesato, vogliamo trovare i **cammini minimi**, e quindi anche le distanze da un nodo $s$ (sorgente) a tutti gli altri nodi del grafo.

![[cammini-minimi.png|center|500]]

(^ cammini minimi dalla sorgente $0$ a tutti gli altri nodi)

L'algoritmo di Dijkstra costruisce l'albero dei cammini minimi un arco per volta partendo dal nodo sorgente, e segue questa logica:
- ad ogni passo, aggiunge all'albero l'arco che produce il nuovo cammino **più economico**
- assegna ad ogni nodo come distanza il **costo del cammino** (che dalla radice porta ad esso)

L'algoritmo rientra nel paradigma della **tecnica greedy**. Opera infatti secondo una sequenza di *decisioni irrevocabili*: 
- il cammino dal nodo sorgente ad un nuovo nodo viene deicso ad ogni passo, senza più tornare sulla decisione
- le decisioni vengono prese in base ad un *criterio locale*: tra tutti i cammini percorribili, si sceglie quello che costa meno

**pseudocodice**:
- `P[0...n-1]` vettore dei padri inizializzato a `-1`
- `D[0...n-1]` vettore delle distanze inizializzato a `+inf` (perché si utilizzerà la funzione `min()`)
- `D[s], P[s] = 0, s` (la sorgente ha distanza zero da se stessa ed è padre di se stessa)
- `while esistono archi (x,y) con P[x]!=-1 e P[y]==-1`: 
	- sia `(x,y)` quello per cui è minimo `D[x] + peso(x,y)`
	- `D[y], P[y] = D[x] + peso(x,y), x` (si sceglie il cammino, quindi la distanza del nuovo nodo sarà data dalla distanza del padre + il peso dell'arco, e il padre del nuovo nodo sarà il nodo corrente)

>[!warning] attenzione: l'algoritmo non è corretto nel caso di grafi con pesi anche negativi
>Infatti, poiché sceglie il cammino meno costoso ad ogni passo, non considera il caso in cui si percorrerà prima un arco con peso maggiore per poi incontrare archi con pesi negativi (che abbasseranno quindi il costo totale).

### prova di correttezza
Si dimostra per induzione sul numero di iterazioni del `while` (che assegna una nuova distanza ad un nodo).

Dobbiamo dimostrare che **la distanza assegnata è quella minima**.

- *caso base*: al passo zero viene assegnata distanza zero alla sorgente (e, poiché non consideriamo il caso di pesi negativi, non c'è una distanza minore)
- *ipotesi induttiva*: assumiamo che i cammini costruiti fino al passo $i>0$ siano minimi

Sia $T_{i}$ l'albero dei cammini minimi costruito fino al passo $i>0$ e $(u,v)$ l'arco aggiunto al passo $i+1$. Per dimostrare che $D[v]$ è la distanza minima, basta mostrare che il costo di un eventuale cammino alternativo è sempre superiore o uguale a $D[v]$.

Sia $C$ un qualsiasi cammino alternativo $s\to v$ e $(x,y)$ il primo arco che incontriamo percorrendolo all'indietro, tale ceh (ovvero l'ultimo arco del cammino).