## Scheduling loops

Loops can be scheduled with the `schedule` clause:

> [!syntax]
> ```C
> schedule(type, chunksize)
> ```
> 
> where `type` can be:
> - `static` ⟶ the iterations can be **assigned to the threads before the loop is executed**
> - `dynamic` or `guided` ⟶ the iterations are assigned to the threads **while the loop is executing**
> - `auto` ⟶ the **compiler and/or the runtime system** determine the schedule 
> 
> and the `chunksize` is a positive integer. 


>[!summary] default and cyclic partitioning for loops
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
> implemented in OpenMP like so:
> 
> ```C
> sum = 0.0;
> #pragma omp parallel for num_threads(thread_count) \
>     reduction(+:sum)
> for (i = 0; i <= n; i++)
>     sum += f(i);
> ```
> 
> **cyclic partitioning**:
> 
> | Thread   | Iterations                                |
> | -------- | ----------------------------------------- |
> | 0        | $0, n/t, 2n/t, \dots$                     |
> | 1        | $1, n/t + 1, 2n/t + 1, \dots$             |
> | $\vdots$ | $\vdots$                                  |
> | $t - 1$  | $t - 1, n/t + t - 1, 2n/t + t - 1, \dots$ |
> 
> Implemented like so:
> ```C
> sum = 0.0;
> #pragma omp parallel for num_threads(thread_count) \
>     reduction(+:sum) schedule(static,1)
> for (i = 0; i <= n; i++)
>     sum += f(i);
> ```

>[!example] `static` schedule
> 
> different ways to divide twelve iterations between three threads:
> 