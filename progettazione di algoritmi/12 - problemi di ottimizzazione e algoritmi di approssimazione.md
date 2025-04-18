---
created: 2025-03-31T14:43
updated: 2025-04-18T17:28
---
Un problema di ottimizzazione è un tipo di problema in cui l'obiettivo è trovare la **migliore soluzione possibile** tra un insieme di soluzioni ammissibili.
- ogni soluzione ammissibile (ovvero che soddisfa tutte le condizioni imposte dal problema) ha un valore associato chiamato *costo* o *beneficio*.
- l'obiettivo può essere minimizzarlo o massimizzarlo: ci sono quindi problemi di minimizzazione e problemi di massimizzazione

Gli **algoritmi di approssimazione** sono algoritmi per cui si può dimostrare che la soluzione ammissibile (ovvero che rispetti le condizioni richieste) approssima entro un certo grado una soluzione ottima.

Le **euristiche** sono invece algoritmi per cui non si riesce a dimostrare che la soluzione ammissibile si avvicini a quella ottima, ma che sembrano comportarsi bene sperimentalmente. <small>(sono un'"ultima spiaggia" quando non ci sono né algoritmi corretti né algoritmi di approssimazione efficienti).</small>

### problemi di minimizzazione
Nel caso dei problemi di minimizzazione, ad ogni soluzione ammissibile è associato un **costo**, e si cerca la soluzione di *costo minimo*.

>[!info] formalmente
>Si dice che $A$ approssima il problema di minimizzazione entro un fattore di approssimazione $\rho$ se, **per ogni istanza** $I$ del problema, vale:
>
>$$\frac{A(I)}{OPT(I)}\leq \rho$$
>
>dove $OPT(I)$ è il costo di una soluzione ottima per $I$, e $A(I)$ è il costo della soluzione prodotta dall'algoritmo $A$ per $I$.
>
>Trattandosi di un problema di minimizzazione, si ha sempre $A(I)\geq OTT(I)$, perciò il rapporto di approssimazione $\rho$ è sempre un numero $\geq 1$.
>- se $A$ approssima $P$ con fattore $1$, allora $A$ è **corretto** per $P$ perché trova sempre una soluzione ottima
>- se $A$ approssima $P$ entro un fattore di $2$, allora $A$ trova sempre una soluzione di costo al più doppio di quello della soluzione ottima, ecc.
>
>>[!tip] problemi di massimizzazione
>>Per i problemi di massimizzazione vale il rapporto inverso, ovvero:
>>
>>$$\frac{OTT(I)}{A(I)}$$
#### problema di copertura tramite nodi
Dato un grafo indiretto $G$, una sua **copertura tramite nodi** è un sottoinsieme $S\subseteq V$ dei suoi nodi tale che tutti gli archi di $G$ hanno almeno un estremo in $S$.

> [!bug] prima ipotesi greedy (errata)
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
> Si può dimostrare che questo algoritmo ha un rapporto di approssimazione di almeno $\frac{\Omega (l\cdot \log l)}{O(l)}=\Omega(\log l)$.

>[!tip] seconda ipotesi greedy
>Consideriamo invece questa strategia greedy: si considerano i vari archi del grafo uno dopo l'altro e, ogni volta che se ne trova uno non coperto (ovvero che non ha estremi in $S$) si aggiungono entrambi gi estremi dell'arco ad $S$.
>
>```
> def copertura(G):
> 	inizializza la lista E con gli archi di G
> 	S = []
> 	while E != []:
> 		estrai un arco (x,y) da E
> 		se né x né y sono in S:
> 			S.append(x)
> 			S.append(y)
> 	return S
>```
>- l'algoritmo è sicuramente *ammissibile*: ogni arco verrà esaminato e, se risulterà non coperto, verrà coperto da entrambi i lati
>
>Si può dimostrare che il rapporto di approssimazione è limitato a 2 (non esistono algoritmi di approssimazione per questo problema con rapporto inferiore a 2).
>
>>[!note] dimostrazione
>>Siano $e_{1},\,e_{2},\,\dots,\,e_{k}$ gli archi di $G$ non coperti che vengono trovati durante l'esecuzione.
>>
>>Per come funziona l'algoritmo, deduciamo che $A(I)=2k$.
>> 
>>I $k$ archi non coperti sono tra loro disgiunti (infatti i due estremi di ognuno di questi archi sono stati incontrati per la prima volta durante l'algoritmo, altrimenti sarebbero stati coperti), quindi, in qualunque delle soluzioni ottime deve essere presente almeno un estremo di ciascuno dei $k$ archi. Deduciamo quindi che $k\leq OTT(I)$.
>>
>>Da quanto detto prima, ricaviamo quindi che $A(I)=2k\leq 2 \cdot OTT(I)$, da cui segue $\frac{A(I)}{OTT(I)}\leq 2$.
>
>Implementazione:
> ``` python
> def copertura1(G):
> 	n = len(G)
> 	E = [(x,y) for x in range(n) for y in G[x] if x<y]
> 	presi = [0]*n # presi[i] == 1 se i è in S
> 	sol = []
> 	
> 	for a, b in E:
> 		if presi[a]==presi[b]==0:
> 			sol.append(a)
> 			sol.append(b)
> 			presi[a] = presi[b] = 1
> 	return sol
> ```
> 
> - l'algoritmo ha complessità $O(n+m)$