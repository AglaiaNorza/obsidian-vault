(len() è $\Theta(1)$)

(in un dizionario, la ricerca al caso pessimo dà $O(n)$)

Raggiungibilità: $u$ è raggiungibile da $v$ se esiste un cammino che da $u$ arriva a $v$.

Connettività: comunque prendo due nodi, tra di essi c'è un cammino

Dato un grafo e un nodo, voglio sapere quali nodi posso raggiungere a partire da quel nodo.

DFS
- bisogna tenere traccia dei nodi già visitati (per non cadere in cicli)
