---
created: 2025-03-31T14:43
updated: 2025-04-14T09:56
---
Un problema di ottimizzazione è un tipo di problema in cui l'obiettivo è trovare la **migliore soluzione possibile** tra un insieme di soluzioni ammissibili.
- ogni soluzione ammissibile (ovvero che soddisfa tutte le condizioni imposte dal problema) ha un valore associato chiamato *costo* o *beneficio*.
- l'obiettivo può essere minimizzarlo o massimizzarlo: ci sono quindi problemi di minimizzazione e problemi di massimizzazione

### problema di copertura tramite nodi
Dato un grafo indiretto $G$, una sua **copertura tramite nodi** è un sottoinsieme $S\subseteq V$ dei suoi nodi tale che tutti gli archi di $G$ hanno almeno un estremo in $S$.

> [!bug] ipotesi greedy (errata)
> Una strategia greedy potrebbe essere questa:
> - finché ci sono archi non coperti, inserisci in $S$ il nodo che copre il massimo numero di archi ancora scoperti
> 
> Questa soluzione non trova la copertura ottimale.
> Per esempio, dato questo grafo $G$:
> 
> ![[greedy-copertura.png|center|300]]
> 
> L'algoritmo sceglie come primo nodo $e$ (che copre 4 archi). Dopodiché, tutti i nodi restanti coprono lo stesso numero di archi (2) e l'algoritmo dovrà quindi sceglierne uno per coppia. Il sottoinsieme $S$ avrà quindi 5 nodi.
> 
> ![[greedy-copertura2.png|center|200]]
> 
> La soluzione ottimale ha però solo 4 nodi:
>  
> ![[greedy-copertura3.png|center|200]]
> 
> Si può dimostrare che questo algoritmo sbaglia di massimo $\log n$ nodi.
> (non ottimale, si vuole trovare un'euristica che sbagli massimo di una costante)
> 
