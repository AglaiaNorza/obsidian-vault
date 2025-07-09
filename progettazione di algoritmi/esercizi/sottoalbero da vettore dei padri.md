---
{}
---
Dato un albero di $n$ nodi rappresentato tramite il vettore dei padri $P$ e un nodo $x$, progettare un algoritmo che in tempo $O(n)$ produce la lista dei nodi presenti nel sottoalbero radicato in $x$.

```python
def salbero(P):
    n = len(P)
    alb = [[] for _ in range(n)]

    for i in range(n):
        if P[i] != i: alb[P[i]].append(i)

    return alb

def DFS(G, x, sottoalbero):
    sottoalbero.append(x)
    for i in G[x]:
        DFS(G, i, sottoalbero)

    return sottoalbero

G = salbero(P)
sottoalbero = DFS(G, x, [])
```

- salbero è $O(n)$
- $G$ è un albero, quindi $O(n+m)=O(n)$ per la DFS
