# Caching

> [!info] on caches (already seen in comparch)
> **Caches** are memory locations that can be accessed in *less time* than others. 
> - CPU caches are typically located on the same chip or on a chip (usually closer to the CPU) that can be accessed much faster than ordinary memory
> - caches use more performing but also more expensive technology, so they are typically smaller
> 
> The main issue with caches is: since they're smaller (thus we can't put everything in them), what should we store in them?
> 
> The answer relies on the assumption of **locality** (programs don't access memory randomly, but in reliable patterns)
> - *spatial locality* ⟶ if you access a specific memory location, you are highly likely to access a nearby location soon
> - *temporal locality* ⟶ if you access a memory location now, you are highly likely to access that same location again (ore one close by) in the near future
> 
> For these reasons, data is transferred from memory to cache in blocks or lines (i.e. when `z[0]` is transferred, so will be `z[1]`, `z[2]`, ..., `z[15]`)
> - doing one transfer of 16 memory locations is better than doing 16 transfers of one - when accessing `z[0]`, one will have to wait for the transfer, but the other 15 elements will already be there for the future
> 
> ---
> 
> Caches are organised *by speed* in levels. `L1` is the smallest and the fastest, `L3` is the largest and slowest.
> - the CPU first checks if the data is in `L1`, if not, in `L2`, etc…
> 
> A cache *hit* happens when data is found, a *miss* when it isn't. If all of the caches miss, the CPU will get the data from main memory and move it to the cache.
> --- 
>  
> When a CPU writes data to a cache, the value in the cache might be inconsistent with the value in main memory.
>  
> Caches handle this with one of these two strategies:
> - **write-through** ⟶ they update the data in the main memory at every write in the cache
> - **write-back** ⟶ when a change happens, the data in the cache is marked as dirty - when a cache line is replaced by a new one, the dirty line is written to memory

>[!question] why do we care
> To write efficient parallel code, its sequential parts must be efficient.

## Caching on multicores
In multicore systems, each core is in possession of a `L1` cache, while `L2` and `L3` caches might be shared amongst threads. The programmer has no control over caches and when they get updated, and the **inconsistency** problem becomes more serious, as a variable needs to be **consistent across caches for all of the cores**.

>[!example] example
>
>![[multicore-cache-es.png|center|450]]

There are two ways to keep the cache coherent:
- **Snooping Cache Coherence** ⟶ the cores share a *bus*
	- any signal transmitted on the bus can be "seen" by all cores 