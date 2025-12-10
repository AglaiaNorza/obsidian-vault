OpenMP compilers *don't check for dependencies* among iterations in a loop that is being parallelized with a `parallel for`.

When we have a for loop of this form:
```C
for (i = 1 to N) 
{ 
	// S1: writes/reads on location x 
	...
	// S2: writes/reads on location x
}
```

we have to be careful when parallelising a loop - since both instructions operate on the same memory location, there is a chance that running the loop in parallel might have unwanted effects.

>[!info] loop-carried dependence 
>When results of 1+ iterations of a loop depend on each other, we say that we have a **loop-carried dependence** - these cases cannot in general be correctly parallelized by OpenMP.

## Dependence types

> [!info] dependence types
> 
> ##### Flow dependence: `RAW` (Read After Write)
> 
> **True Dependency**. It occurs when `S1` writes a value to memory location $x$, and `S2` subsequently reads that value. The execution order `S1` , `S2` **must** be preserved.
> 
> >[!summary] Rule
> >The read operation (`S2`) must wait for the write operation (`S1`) to complete.
> >
> > `S1`: Write $x \longrightarrow$ `S2`: Read $x$
> 
> >[!example] RAW Example
> >```
> >x = 10;          // S1: Write to x
> >y = 2 * x + 5;   // S2: Read from x (needs the new value 10)
> >```
> 
> ---
> 
> ##### Anti-flow dependence: `WAR` (Write After Read)
> 
> **False Dependency** (Name Dependence). It occurs when `S1` reads a value from $x$, and `S2` subsequently writes a new value to the same location $x$. If the order is reversed, `S1` would read the wrong (new) value.
> 
> >[!summary] Rule
> >The read operation (`S1`) must complete before the write operation (`S2`) begins, to ensure `S1` reads the old value.
> >
> > `S1`: Read $x \longrightarrow$ `S2`: Write $x$
> 
> >[!example] WAR Example
> >```
> >y = x + 3;       // S1: Read from x (needs the old value)
> >x ++;            // S2: Write to x (overwrites the old value)
> >```
> 
> ---
> 
> ##### Output dependence: `WAW` (Write After Write)
> 
> **False Dependency** (Name Dependence). It occurs when both `S1` and `S2` write to the same memory location $x$. The execution order `S1` then `S2` **must** be preserved to ensure the final value of $x$ is the one written by `S2`.
> 
> >[!summary] Rule
> >The final value of $x$ must be the one produced by the last write (`S2`).
> >
> > `S1`: Write $x \longrightarrow$ `S2`: Write $x$
> 
> >[!example] WAW Example
> >```
> >x = 10;          // S1: Write to x (sets it to 10)
> >x = x + c;       // S2: Write to x (this new value must persist)
> >```
> 
> ---
> 
> ##### Input dependence: `RAR` (Read After Read)
> 
> This is **NOT an actual dependence** that constrains execution order. Since both statements only read from the memory location $x$, their order does not affect the program's result.
> 
> >[!summary] Rule
> >The order of two read operations does not matter for correctness.
> >
> > `S1`: Read $x \longleftrightarrow$ `S2`: Read $x$
> 
> >[!example] RAR Example
> >```
> >y = x + c;       // S1: Read from x
> >z = 2 * x + 1;   // S2: Read from x
> >```

