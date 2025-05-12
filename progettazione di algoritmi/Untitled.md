---
created: 2025-05-12T14:20
updated: 2025-05-12T14:48
---

> [!example] stringhe binarie
> Dato un parametro intero $n$, stampare tutte le stringhe binarie lunghe $n$.

> [!tip] osservazioni
> - le stringhe da stampare sono $2^n$
> - stampare una stringa lunga $n$ costa $\Theta(n)$
> 
> quindi, il meglio che ci si può aspettare da un algoritmo è $\Omega (2^n\cdot n)$

```python
def strbin(n, sol = []):
	if len(sol) == n:
		print(''.join(sol))
		return
	sol.append('0')
	strbin(n, sol)
	sol.pop()
	sol.append('1')
	strbin(n, sol)
	sol.pop()
```

- questo algoritmo genera un albero di chiamate ricorsive alto $n$
- l'albero ha quindi $\sum_{i=o}^h 2^i=2^{h+1}-1$ nodi, che $\in \Theta(2^n)$
- ogni nodo esegue solo operazioni in $\Theta(1)$, tranne per il `print()`, che costa $\Theta(n)$ e viene eseguito solo dalle foglie 

quindi, i nodi interni lavorano per $\Theta(1) \cdot \Theta(2^n) = \Theta(2^n)$, mentre i nodi foglia per $2^n \cdot \Theta(n)$, per un totale di:

$$
\Theta(2^n) + 2^n \cdot \Theta(n) = \Theta(2^n \cdot n)
$$

> [!example] vincolo sugli zeri
> Si vogliono stampare solo le stringhe che contengono massimo $k$ zeri, con $k\leq n$.

```python
def strbink(n, k, sol = []):
```