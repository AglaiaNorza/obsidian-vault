Un **ordinamento topologico** è una permutazione dei nodi di un grafo tale che, se $(u,v)\in E$, allora $u$ compare prima di $v$ nell'ordinamento (ovvero tutte le frecce puntano in una sola direzione).

- non è sempre possibile trovarne uno

> Un grafo diretto può avere da $0$ a $n!$ ordinamenti topologici <small>(ha il massimo numero di ordinamenti topologici quando non ha archi - tendenzialmente, più archi ci sono, meno sono gli ordinamenti topologici)</small>

>[!tip] esiste un sort topologico $\iff$ il grafo è un DAG (grafo diretto aciclico)

Un DAG ha infatti sempre un **nodo sorgente**, ovvero un nodo in cui non entrano archi. Questa proprietà ci permette di costruire un ordinamento topologico in questo modo:
- inizio la sequenza dei nodi con una sorgente
- cancello dal DAG quel nodo sorgente e gli archi che partono da esso - otterrò un nuovo DAG
- ripeto fino ad aver sistemato in ordine lineare tutti i nodi

> <small>fatto anche [[19 - il meccanismo di lock, lock binario#lock binario|qui]] (basi di dati 1, serializzabilità)</small>

#### algoritmo per il sort topologico (basato sulle sorgenti)
- restituisce un sort topologico di $G$ se esiste - altrimenti, una lista vuota
 
```python
def sortTop(G):
	n = len(G)
	gradoEnt = [0]*n
	for i in range(n):
		for j in G[i]:
			gradoEnt(j) += 1 
			# se j compare in una qualsiasi lista di adiacenza, 
			# vuol dire che ha archi entranti

	sorgenti = [ i for i in range(len(G)) if gradoEnt[i]==0 ]
	ST = []

	while sorgenti:
		u = sorgenti.pop()
		ST.append(u)
		for v in G[u]:
			gradoEnt[v] -= 1
			if gradoEnt[v] == 0:
				sorgenti.append(v)

	if len(ST) == len(G): return ST
	return []
```

- creare il vettore dei gradi entranti costa $O(n+m)$
- inizializzare l'insieme delle sorgenti costa $O(n)$
- il while viene eseguito $O(n)$ volte e il costo totale del for al termine del while è $O(m)$

il costo totale è quindi $O(n+m)$.
#### algoritmo per il sort topologico basato su DFS
- effettua una visita DFS 
- man mano che termina la visita dei vari nodi


la somma del costo delle visite è la somma dei nodi e degli archi.


