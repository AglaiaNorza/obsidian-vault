**Derived datatypes** are used to represent any **collection of data items** in memory
- both the item types and their locations are stored in memory
- if a function that sends data knows this information about a collection of data items, it can collect the items from memory before they are sent
- and a function that receives data can distribute the items into their correct destinations in memory when they are received

>[!bug] naive implementation
> An implementation like this one wouldn't work, because different platforms could implement a structure's layout differently
> 
> ```C
> const int N = ...;
> typedef struct Point{
> 	int x;
> 	int y;
> 	int color;
> };
> 
> Point image[N];
> MPI_Send(image, N*sizeof(Point), .....);
> ```
> 
> ![[struct-in-memory.png|center|400]]

## implementation
Formally, derived data types are implemented with a **sequence of basic MPI data types** together with a **displacement** for each of the datatypes.

### `MPI_Type_create_struct`
Builds a derived datatype that consists of *individual elements with different basic types*.

>[!summary] header
> 
> ```C
> int MPI_Type_create_struct(
> 	int           count,                    // in
> 	int           array_of_blocklengths[],  // in
> 	MPI_Aint      array_of_displacements[], // in
> 	MPI_Datatype  array_of_types[],         // in
> 	MPI_Datatype* new_type_p                // out
> );
> ```

### `MPI_Get_address`
We can't be sure of the size of the displacements (because of the implementation) - we can use `MPI_Get_address` to get the **address of the memory location**.

>[!summary] header
> 
> ```C
> int MPI_Get_address(
> 	void*     location_p, // in
> 	MPI_Aint* address_p   // out
> );
> ```

> [!example]- example
> 
> ```C
> struct t {
> 	double a;
> 	double b;
> 	int n;
> };
> ```
> 
> ```C
> MPI_Aint a_addr, b_addr, n_addr;
> 
> MPI_Get_address(&a, &a_addr);
> array_of_displacements[0] = 0; // start
> MPI_Get_address(&b, &b_addr);
> array_of_displacements[1] = b_addr-a_addr; //first displacement
> MPI_Get_address(&c, &c_addr);
> array_of_displacements[2] = c_addr-a_addr; // second displacement (from a, not from b !!)
> ```
> 
> 
> > [!warning] warning !
> > This approach would be wrong:
> > ```C
> > array_of_displacements[0] = 0;
> > array_of_displacements[1] = &b - &a;
> > array_of_displacements[2] = &n - &a;
> > ```
> > because `&` cast-expressions return a pointer, not an address. 
> > ISO C does not require that the value of a pointer (or the pointer cast to int) be the absolute address of the object pointed at (though this is commonly the case).
> > Referencing may not have a unique definition on machines with a segmented address space. The use of `MPI_Get_address` guarantees portability.

## `MPI_Type_commit`
Allows the MPI implementation to optimize its internal representation of the datatype for use in communication functions (it **finalizes** a user-defined datatype before it can be used in any communication operations)
- it **must** be called before using the type in an operation !!

>[!summary] header
>```C
> int MPI_Type_commit(MPI_Datatype* new_mpi_t_p); //in&out
>```

## `MPI_Type_free`
Frees any additional storage used for the new data type, after one is done using it.

> [!summary] syntax
> 
> ```C
> int MPI_Type_free(MPI_Datatype* old_mpi_t_p); //in&out
> ```

## other functions for new datatypes
MPI defines ~400 functions, 40 of which are used to manage datatypes.
Some other examples are:

![[MPI-more-data.png|center|450]]

- `MPI_Type_contiguous`:
    - Creates a new datatype for a single, contiguous block of elements.
- `MPI_Type_vector`:
    - Creates a datatype for data elements of the same datatype that are regularly spaced (strided) in memory.
    - This is defined by a `Count` (number of blocks), a `Block Length` (elements per block), and a `Stride` (distance between the start of consecutive blocks).
- `MPI_Type_create_subarray`:
    - Creates a datatype that describes a multidimensional subarray within a larger array.
    - Requires specifying the full array size (`arraysizes`), the desired subarray size (`subsizes`), and the starting coordinates (`startsizes`).
- `MPI_Pack` / `MPI_Unpack`:
    - Used to manually pack (serialize) non-contiguous or heterogeneous data into a contiguous buffer before a send, and then unpack it on the receiving side.