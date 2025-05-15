---
created: 2025-05-15T16:13
updated: 2025-05-15T16:43
---

> [!example] matrici binarie
> Progettare un algoritmo che prende come parametro un intero $n$ e stampa tutte le matrici binarie $n \times n$.

- le matrici binarie lunghe $n$ sono $2^{n^2}$

Invece di gestire la matrice con `append()` e `pop()` come faremmo con una stringa, conviene crearla e gestirla andando avanti e indietro con gli indici.

```python
def printmatr(n, sol, i=0, j=0):
	if i == n:
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