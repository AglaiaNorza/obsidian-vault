## Scheduling loops

>[!example] default and cyclic partitioning for loops
> ```C
> sum = 0.0
> for (i = 0; i <= n; i++)
>```
>
> If we were to parallelise this for, how would iterations be assigned to threads?
> 
> Two different ways to assign them are:
> 
> **default partitioning**:
> 
> | Thread  | Iterations                  |
> | ------- | --------------------------- |
> | 0       | $0, 1, 2, \dots, n/t - 1$   |
> | 1       | $n/t, n/t + 1, \dots, 2n/t$ |
> | $\vdots$ | $\vdots$                     |
> | $t-1$   | $n(t-1)/t, \dots, n-1$      |
> 
> **cyclic partitioning**:
> 
> | Thread   | Iterations                                |
> | -------- | ----------------------------------------- |
> | 0        | $0, n/t, 2n/t, \dots$                     |
> | 1        | $1, n/t + 1, 2n/t + 1, \dots$             |
> | $\vdots$ | $\vdots$                                  |
> | $t - 1$  | $t - 1, n/t + t - 1, 2n/t + t - 1, \dots$ |

