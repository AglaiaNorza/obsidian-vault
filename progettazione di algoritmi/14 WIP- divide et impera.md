---
created: 2025-04-18T18:43
updated: 2025-04-19T13:34
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
