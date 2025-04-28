---
created: 2025-04-28T17:21
updated: 2025-04-28T22:20
---
>[!info] programmazione dinamica
>La programmazione dinamica è una tecnica di progettazione di algoritmi basata sulla divisione del problema in **sottoproblemi** e sull'utilizzo di **sottostrutture ottimali** (la soluzione ottimale al sottoproblema può essere usata per trovare la soluzione ottimale all'intero problema).
>
>>[!summary] programmazione dinamica vs divide et impera
>> - il **divide et impera** suddivide il problema in sottoproblemi indipendenti e li risolve separatamente; nel caso in cui i sottoproblemi risultino uguali, risolve lo stesso problema più volte svolgendo lavoro inutile
>>- la **programmazione dinamica** ottimizza evitando ricalcoli inutili tramite memoization, ed è adatta a problemi i cui sottoproblemi si ripetono e/o sono dipendenti tra loro (overlapping di sottoproblemi)

>[!tip] memoization
>La **memoization** (memoizzazione) è una tecnica che consiste nel salvare in memoria i valori restituiti da una funzione, in modo da averli a disposizione senza doverli ricalcolare.
>- una funzione può essere "memoizzata" solo se non ha effetti collaterali e restituisce sempre lo stesso valore quando riceve in input gli stessi parametri 
>	- (si dice che "soddisfa la trasparenza referenziale")

(thx wikipedia)

## numeri di Fibonacci
La sequenza $f_{0},\,f_{1},\,f_{2}\dots$ dei numeri di Fibonacci è definita dall'equazione di ricorrenza:

$$f_{i}=f_{i-1}+f_{i-2}$$
con $f_{0}=f_{1}=1$.

>[!bug] soluzione divide et impera
>Una soluzione naïf è quella che utilizza il metodo divide et impera sfruttando la definizione stessa di numero di Fibonacci:
>```python
> def Fib(n):
> 	if n <= 1: return 1
> 	a = Fib(n-1)
> 	b = Fib(n-2)
> 	return a + b
>```
>
>L'equazione di ricorrenza di questo algoritmo è $T(n)=T(n-1)+T(n-2)+O(1)$. Si ha $T(n)\geq 2T(n-2)+O(1)$, che può essere risolta ottenendo $T(n)\geq \Theta(2^{n/2})$. 
>
>Quindi, $T(n)\in\Omega (2^{n/2})$.
>
>Il problema sta nel fatto che la funzione `Fib` viene chiamata sullo stesso input molte volte - i sottoproblemi in cui viene scomposto il problema non sono disgiunti, mentre l'algoritmo si comporta come se lo fossero.

Per rendere l'algoritmo più efficiente, basta quindi usare la *memoizzazione* e salvare in una lista i valori $fib(i)$ quando li si calcola la prima volta.

```python
def memFib(n, F):
	if n <= 1: return 1
	if F[n] == -1:
		a = memFib(n-1, F)
		b = memFib(n-2, F)
		F[n] = a + b
	return F[n]

F = [-1]*(n+1)
```

- in questo modo, l'algoritmo effettuerà esattamente $n$ chiamate ricorsive
- tenendo conto che ogni chiamata ricorsiva costa $O(1)$, la complessità di `memFib` è $\Theta(n)$

>[!tip] ulteriori ottimizzazioni
>Questo algoritmo può essere ulteriormente ottimizzato: 
>- sostituendo la ricorsione con l'iterazione, si risparmia lo spazio occupato dalla gestione della ricorsion
>- la complessità spaziale della lista ($\Theta(n)$) può essere ridotta a $O(1)$ tenendo conto che basta conservare in memoria solo gli ultimi due valori calcolati
>```python
> def FibOtt(n):
> 	if n <= 1:
> 		return n
> 	a = b = 1
> 	for i in range(2, n+1):
> 		a, b = b, a + b
> 	return b
>```
>
>>[!summary] top-down, bottom-up
>>si può notare che:
>>- nella versione *ricorsiva* dell'algoritmo, si parte dal problema scomponendolo in sottoproblemi sempre più piccoli fino ad arrivare a problemi facilmente risolvibili ⟶ si parla di approccio **top-down**
>>- nella versione *iterativa*, si comincia dai sottoproblemi di dimensione piccola per poi passare a quelli di dimensione via via crescente fino ad arrivare alla soluzione del problema originario ⟶ si parla di approccio **bottom-up**

## problema dei file su disco
Abbiamo un disco di capacità $C$ e $n$ file di varie dimensioni (ciascuna inferiore a $C$). Vogliamo trovare il sottoinsieme di file che può essere memorizzato su disco che massimizzi lo spazio occupato.
- per semplicità di esposizione, ci limiteremo a calcolare il valore della soluzione ottima, ovvero il massimo spazio del disco che può essere occupato grazie agli $n$ file

>[!bug] implementazioni alternative


Un algoritmo **divide et impera** può partire dalle seguenti informazioni:
- se la lista è vuota o $C=0$, la soluzione ottima vale 0
- in caso contrario, l'ultimo file della lista può appartenere o no alla soluzione ottima:
	- se l'ultimo file non appartiene alla soluzione ottima, scegliendo tra i rimanenti $n-1$ file si trova una soluzione ottima per $A[:-1],\,C$  
	- se l'ultimo file appartiene alla soluzione, scegliendo tra i rimanenti $n-1$ file si trova una soluzione ottima per $A[:-1],\,C-A[n-1]$
- possiamo quindi ricondurci al calcolo della soluzione ottima di due sotto-problemi di dimensione inferiore e, una volta risolti questi due problemi e ottenuti i valori $v_{1},\,v_{2}$ delle loro soluzioni, la soluzione al problema di partenza (passo *combina*) sarà data da:
	- $max(v_{1},\,\,v_{2}+A[-1])$

**implementazione**:
```python
def es(A, i, C):
	if i == 0 or C == 0:
		return 0
	lascio = es(A, i-1, C)
	if A[i-1] > C: # sicuramente non posso prenderlo
		return lascio
	prendo = A[i-1] + es(A, i-1, C-A[i-1])
	return max(lascio, prendo)
```

l'equazione di ricorrenza di questa implementazione è:

$T(n,\,C)=T(n-1,\,C) + T(n-1,\,C-A[n-1])+\Theta(1)$

che $\in\Omega (2^{n/2})$.