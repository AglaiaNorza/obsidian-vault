Dato un grafo diretto e pesato $G$ in cui i pesi degli archi possono essere *anche negativi* e fissato un suo nodo $s$, vogliamo determinare il costo minimo dei cammini che conducono da $s$ a tutti gli altri nodi del grafo Se non esiste un cammino, il costo sarà considerato infinito.

>[!info] ciclo negativo
>Un **ciclo negativo** è un ciclo diretto in un grafo la cui somma dei pesi degli archi è negativa. 
>
>![[ciclo-negativo.png|center|300]]

>[!warning] se in un cammino tra i nodi $s$ e $t$ è presente un nodo che appartiene ad un ciclo negativo, allora **non esiste** un cammino di costo minimo tra $s$ e $t$.
>Infatti, ripassando più volte per il ciclo, si abbasserebbe arbitrariamente il costo del cammino.

>[!tip] proprietà
>Se il grafo $G$ non contiene cicli negativi, allora per ogni nodo $t$ raggiungibile dalla sorgente $s$ *esiste un cammino di costo minimo* che attraversa al più $n-1$ archi.

Per trovare cicli negativi: si calcola una riga in più (riga $n$) e, se la $n-1$-esima e la $n$-esima riga sono diverse, c'è un ciclo negativo.