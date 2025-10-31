Collective communication involves a group of processes within a specified communicator.
- every process needs to call the collective function
- collective functions are *highly optimized i*n their MPI implementations, so it makes sense to use them over their manual implementations
- collective calls are matched solely based on *communicator* and *calling order* (there are no tags)

## `MPI_Reduce()`

