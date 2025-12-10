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

### `static` schedule type
(iterations can be assigned to the threads before the loop is executed)

>[!example] `static` schedule type
twelve iterations, three threads
>
>`schedule(static, 1)`
>- thread 0: 0,3,6,9
>- thread 1: 1,4,7,10
>- thread 2: 2,5,8,11
>
`schedule(static, 2)`
>- thread 0: 0,1,6,7
>- thread 1: 2,3,8,9
>- thread 2: 4,5,10,11
>
`schedule(static, 4)`
>- thread 0: 0,1,2,3
>- thread 1: 4,5,6,7
>- thread 2: 8,9,10,11

### `dynamic` schedule type

(Iterations are assigned to the threads while the loop is executing)

The iterations are also broken up into **chunks** of `chunksize` consecutive iterations.
- until all iterations are complete, each thread executes a chunk, and, when done, requests another one from the run-time system
- `chunksize` can be omitted, and it defaults to `1`

This type of scheduling has better *load balancing*, but higher *overhead* (that can still be tuned through `chunksize`).

### `guided` schedule type
(iterations are assigned while the loop is executed)

This schedule type also uses chunk - however, as chunks are completed, the *size of new chunks decreases*. 
- chunks have size = `num_iterations/num_threads`, where `num_iterations` = number of unassigned iterations
- the size decreases up to `chunksize` ("lower bound") - default is `1`
	- exception: the very last chunk can be smaller than `chunksize`

>[!example] trapezoidal rule iterations 1–9999 using a guided schedule with two threads.
>
> ![[guided-for-loop-es.png|center|450]]


### `runtime` schedule type
(schedule is determined at run-time)

The system uses the `OMP_SCHEDULE` environment variable to determine how to schedule loops at run-time.
- it can take on any of the values that can be sed for a static, dynamic or guided schedule

>[!summary] usage
>The value can be specified as an env variable: 
>```bash
> $ export OMP_SCHEDULE="static,1"
>```
>
>or through a function
>```C
> omp_set_schedule(omp_sched_t kind, int chunksize);
>```


>[!info] selecting a schedule option
>- `static` ⟶ if iterations are *homogeneous* (in execution time)
>- `dynamic/guided` ⟶ if execution cost varies (ex due to input data, conditional logic or cache effects)
>
> the best practice is to use performance tools to measure the runtime for different schedule options *on your target hardware*