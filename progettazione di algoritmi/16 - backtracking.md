---
created: 2025-04-01
updated: 2025-07-07T10:39
---
>[!info] backtracking
>Il **backtracking** è una tecnica algoritmica utilizzata tipicamente per risolvere problemi in cui devono essere soddisfatti dei vincoli. Costruisce progressivamente una soluzione, scartando i percorsi che violano i vincoli e tornando indietro quando una scelta porta a un vicolo cieco o quando una soluzione parziale è stata completata.
>- il backtracking ha una complessità esponenziale, quindi è poco efficiente nell'affrontare problemi che non siano NP-completi [[15 - programmazione dinamica#problema dei file su disco|(problemi NP-completi)]]

## esercizi

### stringhe binarie

> [!example] stringhe binarie (senza vincoli)
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

La tecnica del backtracking si vede nell'uso del `pop()` - infatti, prima si aggiunge `0` alla soluzione parziale e si esplorano tutte le stringhe che iniziano con quel prefisso, e poi si *rimuove* l'ultima scelta (dello `0`) con un `pop()` e si esplorano tutte le stringhe con un `1`. Anche dopo questa chiamata si esegue un altro `pop()` per ripristinare lo stato iniziale della lista prima di tornare ancora indietro.

- questo algoritmo genera un albero di chiamate ricorsive alto $n$
- l'albero ha quindi $\sum_{i=o}^h 2^i=2^{h+1}-1$ nodi, che $\in \Theta(2^n)$
- ogni nodo esegue solo operazioni in $\Theta(1)$, tranne per il `print()`, che costa $\Theta(n)$ e viene eseguito solo dalle foglie 

quindi, i nodi interni lavorano per $\Theta(1) \cdot \Theta(2^n) = \Theta(2^n)$, mentre i nodi foglia per $2^n \cdot \Theta(n)$, per un totale di:

$$
\Theta(2^n) + 2^n \cdot \Theta(n) = \Theta(2^n \cdot n)
$$

> [!example] vincolo sugli zeri
> Si vogliono stampare solo le stringhe che contengono massimo $k$ zeri, con $k\leq n$.

>[!error] soluzione ottimizzabile
>Una soluzione in $\Theta(2^n \cdot n)$ è quella per cui si creano tutte le stringhe, ma si stampano solo quelle ammissibili:
> ```python
> def strbinkLame(n, k, tot1 = 0, sol = []):
> 	if len(sol) == n:
> 		if sol.count('1') <= k:
> 			print(''.join(sol))
> 	return
> 	
> 	sol.append('0')
> 	strbinkLame(n, k, tot1, sol)
> 	sol.pop()
> 	sol.append('1')
> 	bk2(n, k, tot1+1, sol)
> 	sol.pop()
> ```
> - questo algoritmo non è però ottimale: infatti, genera

$\sum_{i=0}^k \binom{n}{i} \approx n^{k+1}$

```python
def strbink(n, k, tot1 = 0, sol = []):
	if len(sol) == n:
		print(''.join(sol))
	return
	
	sol.append('0')
	strbink(n, k, tot1, sol)
	sol.pop()
	 
	if tot1<k:
		sol.append('1')
		bk2(n, k, tot1+1, sol)
		sol.pop()
```

es. esame sett. 2020