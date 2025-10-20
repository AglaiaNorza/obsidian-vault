# parallel design patterns
There are two main categories of parallel program structure patterns:
- **Globally Parallel, Locally Sequential** (GLPS) ⟶ the application is able to perform multiple tasks concurrently with each task running sequentially
	- (SPMD, MPMD, Master-Worker, Map-reduce)
- **Globally Sequential, Locally Parallel** (GSLP) ⟶ the application executes as a sequential program, with individual parts of it running in parallel if requested
	- (Fork/join, Loop parallelism)

## Globally Parallel, Locally Sequential (GLPS)

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
- 