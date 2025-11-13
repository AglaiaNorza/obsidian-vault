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
>- ``


```C
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

void Hello(void);

int main(int argc, char* argv[]) {
	/* get # of threads from CLI */
	int thread_count = strtol(argv[1], NULL, 10);
	
	# pragma omp parallel num_threads(thread_count)


}
```