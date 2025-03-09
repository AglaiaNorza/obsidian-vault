Un **ordinamento topologico** è una permutazione dei nodi di un grafo tale che, se $(u,v)\in E$, allora $u$ compare prima di $v$ nell'ordinamento (ovvero tutte le frecce puntano in una sola direzione).

- non è sempre possibile trovarne uno

> Un grafo diretto può avere da $0$ a $n!$ ordinamenti topologici <small>(ha il massimo numero di ordinamenti topologici quando non ha archi - tendenzialmente, più archi ci sono, meno sono gli ordinamenti topologici)</small>

>[!tip] esiste un sort topologico $\iff$ il grafo è un DAG (grafo diretto aciclico)

Un DAG ha infatti sempre un **nodo sorgente**, ovvero un nodo in cui non entrano archi. Questa proprietà ci permette di costruire un ordinamento topologico in questo modo:
- inizio la sequenza dei nodi con una sorgente
- cancello dal DAG quel nodo sorgente e gli archi che partono da esso - otterrò un nuovo DAG
- ripeto fino ad aver sistemato in ordine lineare tutti i nodi

> <small>fatto anche [[19 - il meccanismo di lock, lock binario#lock binario|qui]] (basi di dati 1, serializzabilità)<small>



- A[i] = numero di archi che entrano in i
- trovo sorgente in $O(n)$

