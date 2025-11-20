OpenMP is an API for **shared-memory parallel programming**.
- MP stands for MultiProcessing

When using OpenMP, the system is viewed as a *collection of cores or CPUs*, all of which have access to the main memory.

OpenMP's aim is to **decompose a sequential program** into components that can be executed in parallel
- with the assistance of the compiler, it allows an "incremental" conversion of sequential programs into parallel ones
- it relies on compiler directives for *decorating portions of the code*, which the compiler will attempt to parallelize

>[!tip] GSLP
> OpenMP programs are **Globally Sequential, Locally Parallel**, and they follow the **fork-join paradigm**.
> 
> ![[OPENMP-GSLP.png|center|500]]


>[!summary] terminology
> - **Team** ⟶ collection of threads executing the parallel block
> - **Master** ⟶ original thread of execution
> - **Parent** ⟶ thread that encountered a parallel directive and started a team of threads (often the master)
> - **Children** ⟶ threads started by the parent
## pragmas
OpenMP uses special preprocessor instructions called **pragmas**. 
They are added to a system to **allow behaviors that aren't part of the basic C specification**.

>[!bug] compilers that don't support pragmas ignore them

### `# pragma omp parallel`

`# pragma omp parallel` is the most basic parallel directive
- included in the `omp.h` library
- the **number of threads** that run the following block of code is **determined by the run-time system**

>[!summary] syntax
>
>```
>  # pragma omp parallel clause
>```
>
>in which `clause` can be:
>- `if(exp)` ⟶ executes in parallel only if `exp` evaluates to a nonzero value at runtime (only one `if` clause can be specified !)
>- `private` / `shared`⟶ seen [[here]]
>- `num_threads(thread_count)` ⟶ **number of threads** to use for the parallel region; if dynamic adjustment of the number of threads is also enabled, then `thread_count` specifies the maximum number of threads to be used
> 	>[!warning] The OpenMP standard **doesn't guarantee** that this will actually start `thread_count` threads.
> 	> There might be system-defined limitations on the number of threads that a program can start.
>

> [!example]- example
> 
> ```C
> #include <stdio.h>
> #include <stdlib.h>
> #include <omp.h>
> 
> void Hello(void);
> 
> int main(int argc, char* argv[]) {
> 	/* get # of threads from CLI */
> 	int thread_count = strtol(argv[1], NULL, 10);
> 	
> 	# pragma omp parallel num_threads(thread_count)
> 	Hello();
> 	
> 	return 0;
> }
> 
> void Hello(void){
> 	int my_rank = omp_get_thread_num();
> 	int thread_count = omp_get_num_threads();
> 	
> 	printf("Hello from thread %d of %d\n", my_rank, thread_count);
> }
> ```

To compile a program that uses OpenMP, the `-fopenmp` **flag** is necessary.
```C
gcc -g -Wall -fopenmp -o omp_hello omp_hello.c
```

### Thread Team Size Control
There are three levels at which the number of threads can be specified:
1) **Universally** - via the `OMP_NUM_THREADS` *environment variable*
	- sets the default number of threads for **all OpenMP programs** executed in the **current shell section**
	- `export OMP_NUM_THREADS=x` to set it, `echo ${OMP_NUM_THREADS}` to query it
2) **Program level** - via the `omp_set_num_threads` *function* (called outside an OpenMP construct)
3) **Pragma level** - via the `num_threads` *clause* <small>(seen above)</small>
	- sets the number of threads for a single specific parallel construct

The *most specific setting* "overwrites" the others (so, a pragma level specification will "win" over a universal one).

Two very useful functions are:
- `omp_get_num_threads` ⟶ returns the *active threads* in a parallel region (if called in a sequential part, `1`)
- `omp_get_thread_num` ⟶ returns the id of the calling thread

### Compiler support
If the compiler doesn't support OpenMP, the `#ifdef` construct can be used:
```C
#ifdef _OPENMP
#include <omp.h>
#endif
```
- this way, the header only gets included if it's actually supported

The same `#ifdef` has to be used before the OpenMP functions are called, though, since they can't be executed without the library.

```C
#ifdef _OPENMP
	int my_rank = omp_get_thread_num ( );
	int thread_count = omp_get_num_threads ( );
#else
	int my_rank = 0;
	int thread_count = 1;
#endif
```

## Mutual Exclusion
When parallelising with OpenMP, one has to be careful: in cases in which **shared variables** are involved, **results are unpredictable** when 2+ threads attempt to simultaneously execute (because the variable copies stored in the registers are not guaranteed to be consistent - changes could be lost/overwritten).

The solution to that is **mutual exclusion** (critical sections).
- only one thread at a time can execute a critical section

```C
# pragma omp critical
	global_result += my_result;
```
- (the compiler likely replaces it with pthread lock and unlocks)

## Variable scope
In OpenMP, the scope of a variable refers to the **set of threads that can access the variable** in a parallel block.

A variable that can be accessed by all the threads in the team has a **shared scope**; a variable that can only be accessed by a single thread has a **private scope**.
- The default scope for variables declared *before a parallel block* is **shared** (inside a parallel block, it's obviously private)

```C
int x; // shared
#pragma omp parallel
{
	int y // private
}
```

## Reduction clause
Say that we want to have an output parameter `global_result`, where each thread accumulates the result of a function.

We could make the function return the computed area and use a critical section like this:
```C
#pragma omp parallel num_threads(thread_count)
{
	#pragma omp critical
	global_result += Local_function(...);
}
```

but we would be *forcing the threads to execute sequentially* !

We can avoid this problem by declaring a *private variable* inside the parallel block and *moving the critical section* after the function call.
```C
#pragma omp parallel num_threads(thread_count)
{
	double my_result = 0.0 // private
	my_result += Local_function(...);
	#pragma omp critical
	global_result += my_result;
}
```

This is a *reduction* ! And OpenMP provides a native way of doing it.

>[!info] Reduction operators
>- A **reduction operator** is a binary operation (e.g. addition/multiplication)
>- A **reduction** is a computation that repeatedly applies the same reduction operator to a sequence of operands to get a single result
>- All of the intermediate results are stored in the same variable: the **reduction variable**

A **reduction clause** can be added to a parallel directive:
```C
reduction(<operator>: <variable list>)
```

Like so:
```C
#pragma omp parallel num_threads(thread_count) reduction(+: global_result)
	global_result += Local_function(...)
```
- it's likely that OpenMP will implement a tree reduction
- it's always better to use a reduction clause rather than a critical section (worst case scenario, OpenMP will use a critical section itself, but in most cases it will use a faster implementation)

The **private variables** created for a reduction clause are **initialised to the identity value** for the operator.
The reduction at the end of the parallel section accumulates the outside value and the private values computed inside the parallel region.

> [!warning] (wrong) example
> 
> ```C
> int acc = 6;
> #pragma omp parallel num_threads(5) reduction(* : acc) // * operation
> {
> 	acc += omp_get_thread_num(); // uses + instead of *
> 	printf("thread %d: private acc is
> 	%d\n",omp_get_thread_num(),acc);
> }
> printf("after: acc is %d\n",acc)
> ```
> 
> This example doesn't work: you should never use an operation that is different from the one specified in the reduction clause (since the private variables will be initialised to its identity value, using a different operation will not hold the same result)
