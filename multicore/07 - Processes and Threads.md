> [!summary] the basics
> - A process is an instance of a running (or suspended) program
> - Threads are analogous to a “light-weight” process. 
> - In a shared memory program, a single process may have multiple threads of control

>[!]
## OpenMP vs Pthreads
OpenMP provides a **higher abstraction interface**. 
- On POSIX systems, it is most likely implemented on top of Pthreads (on non-POSIX systems, on top of some other threading abstraction)
- = it is more portable than Pthreads (you can write the OpenMP code and run it “everywhere“ without modifying it).

Pthreads provides **more fine-grained control**.

(As usual, it's a matter of trade-offs between ease-of-use and flexibility/performance)

> [!warning] using both
> **Mixing** OpenMP and Pthreads in the same code should work, but there might be corner cases where it doesn't. It is usually better to use **either one or the other** unless there's a very strong reasons to mix them.

