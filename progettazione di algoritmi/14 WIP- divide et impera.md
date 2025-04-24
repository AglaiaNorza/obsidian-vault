---
created: 2025-04-18T18:43
updated: 2025-04-24T23:06
---
> [!info] divide-et-impera
> Il **divide et impera** è un approccio di risoluzione di problemi che si basa sulla divisione di un problema in sotto-problemi indipendenti, che vengono risolti ricorsivamente. In generale, è formato da 2+1 step:
> 1) **divide**: il problema viene suddiviso in più sotto-problemi simili a quello originale, che vengono a loro volta suddivisi ricorsivamente finché possibile
> 2) **impera**: si risolvono ricorsivamente i sotto-problemi
> 3) (**combina**: i risultati vengono combinati fino a formare una soluzione del problema di partenza)

### problema della selezione
Data una lista $A$ di $n$ interi distinti e un intero $k$, con $1 \leq k \leq n$, vogliamo sapere quale elemento occuperebbe la posizione $k$ se il vettore venisse ordinato.

>[!tip] casi particolari
>- $k=1$ sarà il minimo di $A$
>- $k=n$ sarà il massimo di $A$
>- $k=\left\lceil  \frac{n}{2}  \right\rceil$ sarà il mediano di $A$

> [!bug] algoritmo naïf
> Un possibile algoritmo in $\Theta(n \log n)$ è questo:
> ```python
> def selezione1(A, k):
> 	A.sort()
> 	return A[k-1]
> ```
> 

Utilizzando la tecnica del divide et impera, il problema può però risolversi in $\Theta(n)$.
- si dimostra quindi che il problema della selezione è computazionalmente più semplice di quello dell'ordinamento

#### algoritmo divide et impera
- si sceglie nella lista $A$ l'elemento in posizione $A[0]$ (**perno**)
- a partire da $A$, si costruiscono due liste $A_{1}$ e $A_{2}$, la prima contenente gli elementi minori del perno e la seconda contenente gli elementi maggiori del perno
- per trovare l'elemento di rango $k$:
	- se $|A_{1}|\geq k$, l'elemento è nel vettore $A_{1}$
	- se $|A_{1}|=k-1$, l'elemento è il perno
	- se $|A_{1}|< k-1$, l'elemento è l'elemento di $A_{2}$ con rango $k-|A_{1}|-1$

```python
def selezione(A, k):
	if len(A) == 1:
		return A[0]
		
	pivot = A[0]
	A1, A2 = [], []
	
	for i in range(1,len(A)):
		if A[i] < pivot:
			A1.append(A[i])
		else:
			A2.append(A[i])
			
	if len(A1) >= k:
		return selezione(A1,k)
	elif len(A1) == k-1:
		return pivot
	return selezione(A2, k-len(A1)-1)
```

La procedura che tripartisce la lista in $A_{1},\,A[0]$ e $A_{2}$ può restituire una partizione massimamente sbilanciata in cui ad esempio $|A_{1}|=0$ e $|A_{2}|=n-1$ se il perno è l'elemento minimo nella lista.
Qualora succedesse sistematicamente per tutte le partizioni eseguite dall'algoritmo, allora la complessità dell'algoritmo sarebbe:

$$T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$$

In generale, la **complessità superiore** della procedura è catturata dalla ricorrenza

$$T(n)=T(m)+\Theta(n)$$

dove $m=max(|A_{1}|,\,|A_{2}|)$.

>[!tip] bilanciamento
>Se avessimo una regola di scelta del perno in grado di garantire una partizione bilanciata, ovvero $m=\frac{n}{2}$, allora la complessità sarebbe $T(n)=T\left( \frac{n}{2} \right)+\Theta(n)=\Theta(n)$.
>
>Ma potremmo anche accontentarci di avere partizioni non perfettamente bilanciate, ma semplicemente non troppo sbilanciate, come quelle per cui $m=\frac{3n}{4}$. In questo caso si avrebbe $T(n)\leq T \left( \frac{3}{4}n \right)+\Theta(n)=\Theta(n)$.
>
>In generale, *finché $m$ è una frazione di $n$*, la ricorrenza dà sempre $T(n)=\Theta(n)$.

#### scelta equiprobabile di $p$
Se scegliamo $p$ a caso in modo equiprobabile tra gli elementi della lista, non si creerà necessariamente una partizione bilanciata ma la complessità rimane lineare in $n$.

```python
def selezioneR(A,k):
	if len(A)==1:
		return A[0]
		
	pivot = A[randint(0, len(A)-1)]
	A1, A2 = [], []
	
	for x in A:
		if x<pivot:
			A1.append(x)
		elif x>pivot:
			A2.append(x)
			
	if len(A1) >= k:
		return selezioneR(A1,k)
	elif len(A1) == k-1:
		return pivot
	return selezioneR(A2, k-len(A1)-1)
```

> [!note] Analisi formale del caso medio
> Con la randomizzazione introdotta per la scelta del pivot possiamo assumere che uno qualunque degli elementi del vettore, con uguale probabilità $\frac{1}{n}$, diventi pivot e, poiché la scelta dell’elemento di rango $k$ produce $|A_{1}|=k-1$ e $|A_{2}|=n-k$, per il tempo atteso dell’algoritmo va studiata la ricorrenza:
> 
> $$
> T(n)\leq \frac{1}{n}\sum^n_{k=1}T\Big(\text{max}\big\{T(k-1),T(n-k)\big\}\Big)+\Theta(n)\leq \frac{1}{n}\sum^{n-1}_{k=\left\lfloor  \frac{n}{2}  \right\rfloor }2T(k)+\Theta(n)
> $$
> 
> Possiamo dimostrare che per questa ricorrenza vale $T(n)=O(n)$ tramite il metodo di **sostituzione**.
> 
> $$
> T(n)=
> \begin{cases}
> \frac{1}{n}\sum^{n-1}_{k=\left\lfloor  \frac{n}{2}  \right\rfloor }2T(k)+a\cdot n&\text{se }n\geq 3 \\
> b&\text{altrimenti}
> \end{cases}
> $$
>  
> Dimostriamo $T(n)<cn$ per una qualunque $c>0$ costante
> Per $n\leq 3$ abbiamo $T(n)\leq b\leq 3c$ che è vera ad esempio per $c\geq b$.
> 
> Sfruttando l’ipotesi induttiva $T(k)\leq c\cdot k$ per $k<n$ abbiamo
> $$
> T(n)\leq \frac{2c}{n}\sum^{n-1}_{k=\left\lfloor  \frac{n}{2}  \right\rfloor }k+a\cdot n
> $$
>  
> da cui ricaviamo
>  
> $$
> \begin{align}
> T(n)&\leq \frac{2c}{n}\left( \sum^{n-1}_{k=1}k-\sum^{\lfloor n/2 \rfloor -1}_{k=1}k \right)+a\cdot n\leq \frac{2c}{n}\left( \frac{n(n-1)}{2}-\frac{\left( \frac{n}{2}-1 \right)\left( \frac{n}{2}-2 \right)}{2} \right)+a\cdot n \leq\\
> &\leq \frac{c}{n}\left( \frac{3n^2}{4}+\frac{n}{2}-2 \right)+a\cdot n\leq \frac{3cn}{4}+\frac{c}{2}+a\cdot n=cn-\left( \frac{cn}{4}-\frac{c}{2}-a\cdot n \right)\leq cn
> \end{align}
> $$
>  
> dove l’ultima diseguaglianza segue prendendo $c$ in modo che $\left( \frac{cn}{4}-\frac{c}{2}-a\cdot n \right)\leq 0$; basta ad esempio prendere $c\geq 8a$.

Abbiamo quindi dimostrato che il tempo dell'algoritmo `selezioneR` è $O(n)$ con alta probabilità.
- ovviamente, nel caso peggiore (quando si verifica che il perno scelto a caso risulta sempre vicino al massimo o al minimo della lista), la complessità dell’algoritmo rimane $O(n^2)$; questo accade però con probabilità molto piccola

#### algoritmo deterministico in $O(n)$
Riuscire a selezionare un perno che garantisca che nessuna delle due sottoliste $A_{1}$ e $A_{2}$ abbia più di $c \cdot n$ elementi per una qualche costante $0<c<1$ porta ad una complessità di $O(n)$.

Esiste un metodo chiamato **mediano dei mediani** che permette di selezionare un perno che garantisce sempre due sottoliste $A_{1}$ e $A_{2}$ con ciascuna non più di $\frac{3}{4}n$ elementi.

>[!summary] algoritmo
>- si divide l'insieme $A$ contenente $n$ elementi in gruppi da 5 elementi ciascuno (l'ultimo gruppo potrebbe avere meno di 5 elementi).
>- si considerano solo i primi $\left\lfloor  \frac{n}{5}  \right\rfloor$ gruppi, ciascuno composto esattamente da 5 elementi.
>- si trova il mediano di ciascuno di questi $\left\lfloor  \frac{n}{5}  \right\rfloor$ gruppi
>- si calcola il mediano $p$ dei mediani ottenuti al passo precedente, e si usa come pivot per $A$
>
>esempio:
>
>![[sceltapivot.png|center|450]]

>[!tip] proprietà
>Se la lista $A$ contiene almeno 120 elementi e il perno $p$ viene scelto in base alla regola, si può dire per certo che la dimensione delle due sottoliste sarà limitata da $\frac{3}{4}n$.
>
>>[!note] dimostrazione
>>Il perno $p$ ha la proprietà di trovarsi in posizone $\left\lceil  \frac{n}{10}  \right\rceil$ nella lista degli $\left\lfloor  \frac{n}{5}  \right\rfloor$ mediani selezionati. Ci sono dunque $\left\lceil  \frac{n}{10}  \right\rceil -1$ mediani di valore inferiore a $p$ e $\left\lfloor  \frac{n}{5}  \right\rfloor -\left\lceil  \frac{n}{10}  \right\rceil$.
>>
>>**prova per $A_{2}$**
>> 
>>Consideriamo i $\left\lceil  \frac{n}{10}  \right\rceil-1$ mediani di valore inferiore a $p$. Ognuno di questi appartiene ad un gruppo di 5 elementi in $n$. Ci sono dunque in $A$ altri 2 elementi inferiori a $p$ per ogni mediano. In totale abbiamo quindi $$