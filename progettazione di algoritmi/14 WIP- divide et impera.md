---
created: 2025-04-18T18:43
updated: 2025-04-24T13:21
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
	- se $|A_{1}|< k-1$, l'elemento è l'elemento di rango $k-|A_{1}|-1$ in $A_{2}$
 