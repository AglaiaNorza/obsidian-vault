Dato un grafo $G$ (diretto o indiretto) e un suo nodo $u$, vogliamo sapere se, partendo da $u$, si raggiunge un ciclo.

- un'idea (errata) di partenza potrebbe essere quella di visitare un grafo e, se si incontra un nodo già visitato, interrompere la visita e restituire True (e, altrimenti, restituire False)
	- non funziona con i grafi indiretti perché in un grafo indiretto, se $(u,v)\in E$, anche $(v,u)\in E$, quindi nella lista di adiacenza di $u$ ci sarà $v$ e viceversa --> ogni arco verrebbe considerato un ciclo e farebbe ritornare True
	- non funziona neanche con alcuni grafi diretti: prendiamo come esempio il grafo $[[1, 2], [], [1] ]$: partendo dal nodo $0$, si visita prima il nodo $1$ (che non ha archi uscenti), e poi il nodo $2$. Ma il nodo $2$ ha un arco uscente verso $1$ (già visitato) --> l'algoritmo ritornerebbe quindi $\text{True}$, nonostante non ci siano cicli.
	-  es:
		- ![[graph-es1.png|150]]
