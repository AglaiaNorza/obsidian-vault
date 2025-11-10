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

>[!summary]- visual representations
>
>single:
>![[MPI-single-thread.png|center|500]]
>
>funneled:
>
>![[MPI-funneled.png|center|500]]
>
>serialized:
>
>![[MPI-serialized.png|center|500]]
>
>multiple:
>
>![[MPI-multiple.png|center|500]]
>

### thread-safety, re-entrant functions
A block of code is **thread-safe** if it can be simultaneously executed by multiple threads without causing problems.

- it is not uncommon for C libraries to not be thread-safe (ex: `strtok`, `random`, `localtime`...)

>[!example]- example, `strtok`
>Suppose we want to use multiple threads to “tokenize” a file that consists of ordinary text. The tokens are just contiguous sequences of characters separated from the rest of the text by white-space.
>
>We could divide the input file into lines of text and assign the lines to the threads in a round-robin fashion:
>- the first line goes to thread 0, second goes to thread 1 etc, and we can serialize access to the lines of input using semaphores
>- after a thread has read a single line of input, it can tokenize the line using the `strtok` function
>- the idea is that, in the first call, `strtok` caches a pointer to string, and for subsequent calls it returns successive tokens taken from the cached pointer.
>  
>>[!bug] thread-safety
>>However, `strtok` caches the pointer to the input line by declaring a variable to have static storage class, which causes the value stored in this variable to persist from one call to the next.
>>Unfortunately, the cached string is shared, not private. 
>>So the `strtok` function is *not thread-safe*. If multiple threads call it simultaneously, the output may not be correct.

In some cases, the C standard specifies **alternate versions** of its functions, called "re-entrant functions", which can be interrupted (typically during thread context-switching), and re-entered by another thread without any ill-effect.
- for example, `strtok_r` is the re-entrant version of `strtok`

In principle, re-entrant $\neq$ thread-safe, but, in practice, **re-entrant functions are often thread-safe**.