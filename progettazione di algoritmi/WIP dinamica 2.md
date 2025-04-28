---
created: 2025-04-28T14:09
updated: 2025-04-28T14:30
---
Dato un intero $n$, vogliamo contare il numero di diversi tassellamenti di una superfice di dimensione $n\times 2$ tramite tessere di dimensione $1 \times 2$.

Utilizziamo una tabella monodimensionale di dimensioni $n+1$ e definiamo il contenuto delle celle come segue:
- $T[i]=$ numero di tassellamenti possibili per la superficie di dimensione $i \times 2$

trovo la piastrella orizzontale?
- sì ⟶ $T[i-1]$
- no ⟶ $T[i-2]$

```python
def tassellamento(n):
	m = max(3, n)
	T = [0]*(n+1)
	T[1], T[2] = 1, 2
	for i in range(3, n+1):
		T[i] = T[i-1] + T[i-2]
	return T[n]
```

