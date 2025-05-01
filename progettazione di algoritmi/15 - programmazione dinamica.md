---
created: 2025-04-28T17:21
updated: 2025-05-01T09:55
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

(definizioni da wikipedia, thx wikipedia)

>[!summary] caratteristiche della programmazione dinamica
>Gli algoritmi di programmazione dinamica si basano quindi spesso sulla costruzione di una tabella (lista o matrice) che memorizza soluzioni intermedie ai sottoproblemi, che verranno poi usate per arrivare a quella finale.
>- in una prima fase, ci si può concentrare sul calcolo del valore ottimo della soluzione; successivamente, la stessa tabella può essere utilizzata per risalire alla soluzione vera e propria cui quel valore corrisponde.
>- l’idea è partire dall’elemento che rappresenta la soluzione ottima e, seguendo a ritroso le decisioni registrate nella tabella, ricostruire il percorso che ha portato a quel risultato.

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

>[!bug]- implementazione divide et impera
> Un algoritmo **divide et impera** può partire dalle seguenti informazioni:
> - se la lista è vuota o $C=0$, la soluzione ottima vale 0
> - in caso contrario, l'ultimo file della lista può appartenere o no alla soluzione ottima:
> 	- se l'ultimo file non appartiene alla soluzione ottima, scegliendo tra i rimanenti $n-1$ file si trova una soluzione ottima per $A[:-1],\,C$  
> 	- se l'ultimo file appartiene alla soluzione, scegliendo tra i rimanenti $n-1$ file si trova una soluzione ottima per $A[:-1],\,C-A[n-1]$
> - possiamo quindi ricondurci al calcolo della soluzione ottima di due sotto-problemi di dimensione inferiore e, una volta risolti questi due problemi e ottenuti i valori $v_{1},\,v_{2}$ delle loro soluzioni, la soluzione al problema di partenza (passo *combina*) sarà data da:
> 	- $max(v_{1},\,\,v_{2}+A[-1])$
> 
> **implementazione**:
> ```python
> def es(A, i, C):
> 	if i == 0 or C == 0:
> 		return 0
> 	lascio = es(A, i-1, C)
> 	if A[i-1] > C: # sicuramente non posso prenderlo
> 		return lascio
> 	prendo = A[i-1] + es(A, i-1, C-A[i-1])
> 	return max(lascio, prendo)
> ```
> 
> l'equazione di ricorrenza di questa implementazione è:
> 
> $T(n,\,C)=T(n-1,\,C) + T(n-1,\,C-A[n-1])+\Theta(1)$
> 
> che $\in\Omega (2^{n/2})$.

Attraverso la memoizzazione, possiamo ottenere una soluzione **pseudopolinomiale**.

>[!info] algoritmo pseudopolinomiale
>In teoria della complessità computazionale, un algoritmo è detto **pseudopolinomiale** se la sua complessità temporale è polinomiale nel *valore numerico* del suo input e non necessariamente nella sua *dimensione* (risolve un problema in tempo polinomiale quando i numeri presenti nell'input sono codificati in unario).

Creiamo una tabella $T$ di dimensione $n+1 \times (C+1)$, in cui $T[i][j]$ è il valore ottenuto dalla soluzione del sottoproblema in cui si hanno i primi $i$ file e la dimensione del disco è $j$ <small>(quindi il massimo spazio che si può occupare in un blocco grande $j$ con i primi $i$ file)</small>.

Per compilarla, usiamo questo criterio:

$$
T[i][j]=\begin{cases} T[i-1,\,j] & \text{se non prendo i (lascio)} \\
A[i]+T[i-1,\,j-A[i]] & \text{se prendo i}
\end{cases}
$$

- (primo caso) se non aggiungo il file $i$, la capienza rimane quella calcolata per i primi $i-1$ file
- (secondo caso) se invece aggiungo il file $i$, sto occupando $A[i]$ unità di spazio e mi resterà una capacità di $j-A[i]$
	- quindi, il valore totale sarà dato dalla dimensione di $i$ sommata al massimo valore ottenibile con i file precedenti e lo spazio residuo (ovvero $T[i-1,\,j-A[i]]$)

Ogni cella deve contenere il massimo spazio occupato con i dati delle coordinate, quindi l'equazione generale per una cella sarà:

$$
T[i][j]=\begin{cases} 0 & i = 0 \\
T[i-1,\,j]& j<A[i-1]  \\
max(\text{lascio, prendo}) & \text{altrimenti}
\end{cases}
$$
con $max(\text{lascio, prendo})$ 
 
$$
\begin{align} \\
=max(T[i-1,\,c],\;\;A[i-1]+T[i-1,\,c-A[i-1]]) \\
\end{align}
$$

**implementazione top-down**
```python
def es(A, C):
	T = [[-1]*(C+1) for i in range(len(A)+1)]
	return disco(A, len(A), C, T)

def disco(A, i, c, T):
	if T[i][c] == -1:
		if i == 0 or c == 0: T[i][c] = 0 
		else:
			lascio = disco(A, i-1, c, T) # opzione senza i
			T[i][c] = lascio
			if A[i-1] <= c: # se non c'entra devo sicuramente lasciare
				prendo = A[i-1] + disco(A, i-1, c-A[i-1], T)
				T[i][c] = max(lascio, prendo) # max spazio occupato
	return T[i][c]
```

Il tempo di calcolo è limitato dalla *dimensione della tabella*: le operazioni di ogni chiamata di `disco()` costano infatti $O(1)$, e il numero totale di chiamate non può superare la dimensione della tabella.

La complessità è quindi $O(nC)$ 
- in realtà, $\Theta(nC)$ a causa dell'inizializzazione della tabella

>[!question] questo algoritmo è quindi più efficiente della versione divide et impera?
>- se $C$ è molto grande (ad esempio se supera $2^n$), la versione memoizzata si comporta peggio; altrimenti, può risultare anche molto più efficiente.

Spesso però <small>(visto che si parla di capienza di dischi ed è comune che si lavori con numeri grandi)</small> la profondità dell'albero delle chiamate ricorsive è molto grande e può portare ad uno stack overflow. Per evitare questo problema, ci si può concentrare direttamente sul calcolo della tabella $T$ eliminando la ricorsione.

**implementazione bottom-up**:
```python
def discoI(A, C):
	n = len(A)
	T = [ [0]*(C+1) for i in range(n+1) ]
	for i in range(1, n+1):
		for c in range(C+1):
			if c < A[i-1]:
				T[i][c] = T[i-1][c]
			else:
				T[i][c] = max(T[i-1][c], A[i-1]+T[i-1][c-A[i-1]])
	return T[n][C]
```
- anche questa versione ha una complessità di $O(nC)$

>[!tip] pseudopolinomiale
>Questo algoritmo è pseudopolinomiale perché la capacità $C$ dell'input è codificata in $\log C$ bit. Considerando il numero di bit come misura, infatti, la complessità dell'algoritmo sarà $O(nC)=O(n \cdot 2^{\log C})$, ovvero esponenziale nella dimensione binaria dell'output.