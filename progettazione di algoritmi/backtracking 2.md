---
created: 2025-05-15T16:13
updated: 2025-05-15T16:56
---

> [!example] matrici binarie
> Progettare un algoritmo che prende come parametro un intero $n$ e stampa tutte le matrici binarie $n \times n$.

- le matrici binarie lunghe $n$ sono $2^{n^2}$

Invece di gestire la matrice con `append()` e `pop()` come faremmo con una stringa, conviene crearla e gestirla andando avanti e indietro con gli indici.

```python
def printmatr(n, sol, i=0, j=0):
	if i == n: # saremmo ad una riga n+1 che non esiste
		for row in sol:
			print(row)
		print()
		return
		
	i1, j1 = i, j+1
	
	if j1 == n:
		i1, j1 = i+1, 0
		
	sol[i][j] = 0
	es1(n, sol, i1, j1)
	
	sol[i][j] = 1
	es1(n, sol, i1, j)

def matrbin():
	sol = [[0]*n for _ in range(n)]
	printmatr(n, sol)
```

- l'albero di ricorsione generato da questo algoritmo è binario di altezza $n^2$, e ha quindi $2^{n^2}-1$  nodi interni e $2^{n^2}$ foglie.
- ciascun nodo interno richiede $O(1)$ e ciascuna foglia $O(n^2)$

L'algoritmo ha quindi complessità $O(2^{n^2}n^2)$.
- poiché le matrici da stampare sono $2^{n^2}$ e la stampa di una matrice richiede $\Theta(n^2)$, l'algoritmo è ottimo.