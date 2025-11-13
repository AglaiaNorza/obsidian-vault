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