---
created: 2025-05-05T14:14
updated: 2025-05-05T14:43
---
Dato un vettore $V$ di interi e un suo sottovettore $v[i,j)$ definisco **spessore** di $v[i,j)$ come $max(v[i,j)) - min(v[i,j))$.

Data una costante $c$, trovare, in $\Theta(n \log n)$, il più lungo sottovettore $v[i,j)$ di spessore al più $c$

- se ho due sottovettori $v[i,\,j)$ e $v[i,\,j+1)$, non mi serve ricalcolare il massimo e il minimo elemento ⟶ mi basta fare $max(max(v[i,\,j), j+1)$
	- questo porta il nostro algoritmo naïf da $O(n^3)$ a $O(n^2)$

Lo spessore segue il principio di monotonia: $[i,j) \subseteq[i',\,j']\implies spess(v[i,j))\leq spess(v[i',\,j'))$

infatti, $max(v[i,j))-min(v[i,j))\leq max(v[i',j'))-min(v[i,j))\leq max(v[i',j'))-min(v[i',j))=spess(v[i',j'))$

- un sottovettore di lunghezza 1 ha spessore 0
- $i=0,\,j=1$ ⟶ $spess=0$
- se lo spessore è minore di c, allargo (a destra), se è maggiore di c, stringo da sinistra
- (assumiamo che c sia positivo, quindi la massima lunghezza ha come minimo 1)

```python
maxS = v[0]; minS = v[0]
spess = 0
i = 0; j =  1
maxL = 0; maxi = 0; maxj = 1
# ccontrolla se devi mettere n-1 per evitare out of bounds (v[n] non esiste)
while j < n:
	if spess < c:
		j += 1
		maxS = max(maxS, v[j])
		minS = min(minS, v[j])
		spess = maxS - minS
		if spess < c and j-i > maxL:
			maxL = j-i
			maxi, maxj = i, j
	
	else:
		i = i+1
		maxS = max(v[i, j])
		minS = min(v[i, j]) 
		spess 

```
