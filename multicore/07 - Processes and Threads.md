> [!summary] the basics
> - A process is an instance of a running (or suspended) program
> - Threads are analogous to a “light-weight” process. 
> - In a shared memory program, a single process may have multiple threads of control

>[!question] how many threads?
>- in principle, there shouldn't be more threads than there are cores (though there are situations in which it could make sense)
>
> To check the number of cores:
> ```sh
> $ lscpu | grep -E '^Thread|^Core|^Socket|^CPU\('
> ```

## OpenMP vs Pthreads
OpenMP provides a **higher abstraction interface**. 
- On POSIX systems, it is most likely implemented on top of Pthreads (on non-POSIX systems, on top of some other threading abstraction)
- = it is more portable than Pthreads (you can write the OpenMP code and run it “everywhere“ without modifying it).

Pthreads provides **more fine-grained control**.

(As usual, it's a matter of trade-offs between ease-of-use and flexibility/performance)

> [!warning] using both
> **Mixing** OpenMP and Pthreads in the same code should work, but there might be corner cases where it doesn't. It is usually better to use **either one or the other** unless there's a very strong reasons to mix them.

## MPI and Threads
### `MPI_Init_thread()`
To use MPI in a thread-safe manner, MPI should be initialised with an `MPI_Init_thread()` instead of an `MPI_Init()`.

>[!summary] header
> ```C
> int MPI_Init_thread(int *argc, char ***argv, int required, int *provided);
> ```
> - `required` ⟶ (in) threading level (seen below)
> - `provided` ⟶ (out) supported (provided) threading level - if < than the required level, the communication might not be thread-safe

### threading levels
- `MPI_THREAD_SINGLE` ⟶ caller rank  is not allowed to use threads (basically equivalent to an `MPI_Init`)
- `MPI_THREAD_FUNNELED` ⟶ rank can be multi-threaded but only the **main thread** may call MPI functions
	- ideal for fork-join parallelism 
- `MPI_THREAD_SERIALIZED` ⟶ rank can be multi-threaded but **only one thread at a time** may call MPI functions; the rank must ensure that MPI is used in a thread-safe way. one approach is to ensure that MPI usage is mutally excluded by all the threads
- `MPI_THREAD_MULTIPLE` ⟶ rank can be multi-threaded and any thread may call MPI functions. *the MPI library ensures that this access is safe across threads*. note that this makes all MPI operations less efficient, even if only one thread makes MPI calls, so should be used only when necessary


