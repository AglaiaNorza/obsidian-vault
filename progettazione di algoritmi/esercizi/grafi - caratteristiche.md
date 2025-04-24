---
created: 2025-03-10T10:51
updated: 2025-04-24T21:06
---
## verificare se un grafo diretto ha un pozzo universale
In questo caso, è più comodo utilizzare la rappresentazione tramite matrice - essa ci permette infatti di risolvere il problema in $\Theta(n)$. 

Osserviamo un esempio di un pozzo universale in questa rappresentazione:
$$\begin{bmatrix} 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} & \textcolor{red}{0} \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \\ 0 & 0 & \textcolor{red}{1} & 0 & 0 & 0 \end{bmatrix}$$

C'è un semplice test che ci permette di eliminare uno dei due nodi rappresentati da ogni posizione della matrice:
$$
M[i][j] = \begin{cases} 1 & i \ \text{ non è pozzo } \\ 0 & j \ \text{ non è pozzo universale} \end{cases}

$$

- se $M[i][j]==1$, sicuramente so che $i$ (la riga, ovvero il nodo da cui l'arco parte) non è un pozzo ⟶ infatti, c'è un arco che parte da esso
- se $M[i][j]==0$, so che $j$ non è pozzo universale ⟶  non c'è un arco entrante in $j$ (ma potremmo trovarci nella situazione $(2,2)$ dell'esempio, quindi non escludiamo $i$)

Quindi, una soluzione sarebbe:
```python
def pozzo(M):
n = len(M)
L = [x for x in range(n)]; # creo una lista con tutti i nodi

# prendo due nodi per controllare
while len(L)>1:
	a = L.pop() # uso pop perché è O(1)
	b = L.pop()
	if M[a][b]: # se è 1
		L.append(b) # a non è pozzo, quindi teniamo b
	else:
		L.append(a) # b non è pozzo universale, quindi teniamo a

L.pop()
for j in range(n): # controllo la riga 
	if M[x][j]: 
		return False # se non sono tutti zeri, non è pozzo univ.

for i in range(n):
	if i != x and M[i][x] == 0:
		return False # se ci sono zeri oltre a quello in (x,x), ""

return True
```

