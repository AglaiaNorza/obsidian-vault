Consideriamo un grafo non pesato connesso non diretto - l'obiettivo è eliminare il massimo numero di archi possibile, mantenendolo connesso. Il grafo così ottenuto si chiama **albero di copertura**.
- si cerca l'albero che costa meno

### algoritmo di Kruskal



Si ha che $m \log m\in O(m\log n)$. Infatti, $m\log m\leq m\log n^2=2 \,m\log n\in O(m\log n)$.