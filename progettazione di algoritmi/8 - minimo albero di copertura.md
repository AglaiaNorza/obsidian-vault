>[!info] spanning tree
>Dato un grafo $G$, un **albero di copertura** (o ricoprente/di connessione/di supporto) è un qualsiasi sottografo $G'=(V',E')$ con $V'=V$, $E'\subseteq E$ che sia un albero (quindi che sia connesso e aciclico).
>- <small>(un albero di copertura  di un grafo connesso indiretto è un albero che contiene tutti i nodi del grafo e contiene soltanto un sottoinsieme degli archi: quelli necessari per connettere tra loro tutti i vertici con uno e un solo cammino)</small>

>[!tip] minimum spanning tree
Sia $G$ un grafo indiretto connesso pesato. Un **albero di copertura minimale** è un suo albero di copertura $T\subseteq G$ tale che la somma di tutti i pesi degli archi
di $T$ è minima rispetto a quella di tutti gli altri alberi di copertura.
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




Si ha che $m \log m\in O(m\log n)$. Infatti, $m\log m\leq m\log n^2=2 \,m\log n\in O(m\log n)$.