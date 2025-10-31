Collective communication involves a group of processes within a specified communicator.
- every process needs to call the collective function
- collective functions are *highly optimized i*n their MPI implementations, so it makes sense to use them over their manual implementations
- collective calls are matched solely based on *communicator* and *calling order* (there are no tags)

## `MPI_Reduce()`

`MPI_Reduce` takes an array of input elements from each process, processes them reducing them into a single result, which gets sent to the root process.

>[!example] example
>
>![[MPI_Reduce.png|center|600]]

>[!summary] header
>```C
>MPI_Reduce(
>    void*          send_data,     // in
>    void*          recv_data,     // *out*
>    int            count,         // in
>    MPI_Datatype   datatype,      // in
>    MPI_Op         operator,      // in
>    int            root,          // in
>    MPI_Comm       comm           // in
>);
>```
>
>- `send_data` is an array of elements (or an element) of type `datatype` that each process wants to reduce
>- `recv_data` is only relevant to the process of rank `root`, and it contains the reduced result
>	- its size is `sizeof(datatype) * count`
>	- even though it doesn't concern them, all of the processes still need to pass in an actual argument corresponding to `recv_data`, even if it’s just `NULL`
> - `MPI_Op` is the reduction operation 
>	- custom operators can be created with `MPI_Op_create()`

> [!example] collective operations
> 
> | operation value | meaning                         |
> | --------------- | ------------------------------- |
> | `MPI_MAX`       | maximum                         |
> | `MPI_MIN`       | minimum                         |
> | `MPI_SUM`       | sum                             |
> | `MPI_PROD`      | product                         |
> | `MPI_LAND`      | logical and                     |
> | `MPI_BAND`      | bitwise and                     |
> | `MPI_LOR`       | logical or                      |
> | `MPI_BOR`       | bitwise or                      |
> | `MPI_LXOR`      | logical exclusive or            |
> | `MPI_BXOR`      | bitwise exclusive or            |
> | `MPI_MAXLOC`    | maximum and location of maximum |
> | `MPI_MINLOC`    | minimum and location of minimum |
> 

>[!warning] only **one call** to `MPI_Reduce` is made - the function will distinguish between the different processes 

>[!tip] other caveats
>- the arguments passed by each process must be "compatible"
>- for example, if one process passes in `0` as the dest_process and another passes in `1`, then the outcome of a call to `MPI_Reduce` is erroneous and the program is likely to hang or crash
>- despite the fact 

> [!example]- example -  average
> 
> ```C
> float *rand_nums = NULL;
> rand_nums = create_rand_nums(num_elements_per_proc);
> 
> // sum the numbers locally
> float local_sum = 0;
> int i;
> for (i = 0; i < num_elements_per_proc; i++) {
>   local_sum += rand_nums[i];
> }
> 
> // print the random numbers on each process
> printf("Local sum for process %d - %f, avg = %f\n",
>        world_rank, local_sum, local_sum / num_elements_per_proc);
> 
> // reduce all of the local sums into the global sum
> float global_sum;
> MPI_Reduce(&local_sum, &global_sum, 1, MPI_FLOAT, MPI_SUM, 0,
>            MPI_COMM_WORLD);
> 
> // print the result
> if (world_rank == 0) {
>   printf("Total sum = %f, avg = %f\n", global_sum,
>          global_sum / (world_size * num_elements_per_proc));
> }
> ```
> 
> - each process creates random numbers and makes a `local_sum` calculation. 
> - the `local_sum` is then reduced to the root process using `MPI_SUM`
> - the global average is then `global_sum / (world_size * num_elements_per_proc)`

## `M`