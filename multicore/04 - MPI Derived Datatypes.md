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
Formally, derived data types are implemented with a **sequence of basic MPI data types** together with a **displacement** for each of the data types.

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
We can't be sure of the size of the displacements (because of the implementation)

