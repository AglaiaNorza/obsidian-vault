# parallel design patterns
There are two main categories of parallel program structure patterns:
- **Globally Parallel, Locally Sequential** (GLPS) ⟶ the application is able to perform multiple tasks concurrently with each task running sequentially
	- (SPMD, MPMD, Master-Worker, Map-reduce)
- **Globally Sequential, Locally Parallel** (GSLP) ⟶ the application executes as a sequential program, with individual parts of it running in parallel if requested
	- (Fork/join, Loop parallelism)

## Globally Parallel, Locally Sequential (GLPS)
 <small>(the application is able to perform multiple tasks concurrently with each task running sequentially)</small>

### SPMD, MPMD
The application logic is stored in a single program.

>[!summary] typical program structure
>- **program initialization** 
>- **obtaining a unique identifier** (numbered from `0`, they enumerate the threads or processes used)
>- **running the program** - execution path changes based on ID
>- **shutting-down the program** (clean-up, saving results)

>[!warning] potential issues with SPMD
>SPMD fails when:
>- memory requirements are too high for all nodes
>- it has to deal with heterogenous platforms

For SPMD, the execution steps are identical to SPMD, but deployment involves different programs.

- both SPMD and MPMD are supported by MPI

### Master-Worker
The Master-Worker model is made up of two kinds of components: Masters and Workers.

The **Master** (1+) is responsible for:
- handing out pieces of work to workers
- collecting the result of the computation from the workers
- performing I/O duties on behalf of the workers
- interacting with the user


The **Workers** do the work given by the masters.

This system is good for implicit load balancing - every time that a worker is done computing, it receives a new task until there are no more tasks available. 
The master can be a bottleneck, but there can be a hierarchy of masters.

### Map-Reduce
Map-Reduce is a variation of the Master-Worker pattern (made popular by Google's search engine implementation).

The master coordinates the whole operation, while the workers run two types of tasks:
- **map** ⟶ apply a function on data (resulting in a set of partial results)
- **reduce** ⟶ collect the partial results and derive the complete one

Map workers and reduce workers are separate, and they can vary in number.

>[!question] Master-Worker vs Map-Reduce
> With the Master-Worker pattern, the same function is applied to different data items, while, with the Map-Reduce pattern, the same function can be applied to **different parts of a single data item**

## Globally Sequential, Locally Parallel (GLPS)
<small>the application executes as a sequential program, with individual parts of it running in parallel if requested</small>

### Fork/Join
There is a single **parent thread** of execution, and **children tasks are created dynamically** at run-time.
- tasks may run via spawning of threads, or via use of a static pool of threads
- children tasks *have to finish* for the parent thread to continue <small>(globally sequential)</small>

>[!tip] used by OpenMP/Pthread

> [!example] example
> 
> ```C
> mergesort(A, lo, hi):
> 	if lo < hi: // |A| >= 1 
> 		mid = [lo + (hi - lo)/2]
> 		fork mergesort(A, lo, mid) // process (potentially) in parallel
> 		mergesort(A, mid, hi) // second recursion handled by the main task
> 		join
> 		merge(A, lo, mid, hi)
> ```

### Loop parallelism
Loop parallelism is employed for migration of sequential/legacy software to multicore. It focuses on **breaking up loops** by manipulating the loop control variable.
- loops have to be in a particular form to support this
- the flexibility is limited, but so is the effort

>[!tip] supported by OpenMP