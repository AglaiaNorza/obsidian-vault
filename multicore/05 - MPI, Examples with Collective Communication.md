## sum between vectors
We want to compute the sum between two vectors $x$ and $y$.
$$
\begin{flalign*}
x +  y &= (x_{0},\,x_{1},\,\dots,\,x_{n-1})+(y_{0},\,y_{1},\,\dots y_{n+1}) \\
&= (x_{0}+y_{0},\,\dots x_{n-1}+y_{n-1}) \\
&= (z_{0},\,\dots z_{n-1}) \\
&= z
\end{flalign*}
$$

The serial implementation of a vector sum is:
```C
	void vector_sum(double x[], double y[], double z[], int n){
		int i;
		for(i = 0; i < n i++)
			z[i] = x[i] + y[i];
	}
```

We can parallelize it (with data parallelism) by dividing the vector between the processes:

```C
void parallel_vector_sum(
		double local_x[], // in
		double local_y[], // in
		double local_z[], // out
		int    local_n    // in
) {
	int local_i;
	for (local_i=0; local_i<local_n; local_i++)
		local_z[local_i] = local_x[local_i] + local_y[local_i];
}

```

## matrices
Matrices are stored in memory as a single row, so we could use a `MPI_Reduce` to sum all the elements of a matrix

```
MPI_Reduce(sendbuf, recvbuf, num_rows*num_cols, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD)
```

Dynamically-allocated matrices are different. 

>[!example]- allocation
> ```C
> int** a;
> a = (int**) malloc(sizeof(int*)*num_rows);
> for (int i=0; i<num_rows; i++) {
> 	a[i] = (int*) malloc(sizeof(int)*num_cols)
> }
> ```

The correct way of summing up matrices is:
```C
for(int i = 0; i < num_rows; i++){
	MPI_Reduce(a[i], recvbuf[i], num_cols, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
}
```
- (since each element of a matrix is an array, a reduce needs to be called for each array)

>[!info] linearizing matrices
> we can also linearize matrices by allocating them in a continuous row - we have to access them differently, but collectives become significantly easier
> 
> ```C
> int* a;
> a = (int*) malloc(sizeof(int)*num_rows*num_cols);
> // ...
> // ...
> // a[i][j] =
> a[i * num_cols + j] = ...
> 
> // we can call
> MPI_Reduce(a, recvbuf, num_rows*num_cols, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
> ```

### matrix-vector multiplication

(how to multiply a single row:)
$$
\begin{bmatrix}
A_1 & A_2 & A_3
\end{bmatrix}
\begin{bmatrix}
B_1 \\ B_2 \\ B_3
\end{bmatrix}
= A_1 B_1 + A_2 B_2 + A_3 B_3
$$

(how to multiply an entire matrix by a vector)

$$
\begin{bmatrix}
A_{11} & A_{12} & A_{13} \\
A_{21} & A_{22} & A_{23} \\
A_{31} & A_{32} & A_{33}
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
=
\begin{bmatrix}
A_{11}x_1 + A_{12}x_2 + A_{13}x_3 \\
A_{21}x_1 + A_{22}x_2 + A_{23}x_3 \\
A_{31}x_1 + A_{32}x_2 + A_{33}x_3
\end{bmatrix}
$$

>[!summary] serial version
> ```C
> void Mat_vect_mult(
> 	double A[], // in (matrix)
> 	double x[], // in (vector)
> 	double y[], // out (result of the multiplication)
> 	int    m,   // in (rows)
> 	int    n,   // in (columns)
> ) {
> 	int i,j;
> 	for(i=0; i<m; i++) {
> 		y[i] = 0.0; // clean slate in y
> 		for (j=0; j<n; j++)
> 			y[i] += A[i*n+j]*x[j] // product
> 	}
> }
> ```

How do we parallelize this?
1) **broadcast** the vector `x` from rank `0` to all other processes
2) **scatter** the rows of the matrix from rank `0` to the other processes
3) each process computes a subset of the elements of the resulting vector `y`
4) **gather** the final vector `y` to rank `0`
5) **broadcast** `y` from rank `0` to all other processes

>[!example] reading a matrix from stdin and scattering it
> ```C
> void Read_matrix(
> 	char     prompt[],  // in
> 	double   local_A[], //out
> 	int      m,         // in
> 	int      local_m,   // in
> 	int      n,         // in
> 	int      my_rank,   // in
> 	MPI_Comm comm       // in
> ) {
> 	double* A = NULL;
> 	int i, j;
> 	
> 	// only rank 0 will allocate and use A
> 	if (my_rank == 0) {
> 		
> 		// the matrix is stored as a contiguous 1D array
> 		A = malloc(m*n*sizeof(double));
> 		
> 		printf("Enter the matrix %s\n", prompt)
> 		
> 		for (i=0; i<m; i++)
> 			for (j=0; j<n; j++)
> 				// (the i,j coordinates are converted into a 1D index)
> 				scanf("%lf", &A[i*n+j]);
> 			
> 			// scattered
> 		MPI_Scatter(A, local_m*n, MPI_DOUBLE, local_A, local_m*n, MPI_DOUBLE, 0, comm);
> 		
> 		free(A);
> 	} else {
> 		// the other processes receive the rows of the matrix
> 		MPI_Scatter(A, local_m*n, MPI_DOUBLE, local_A, local_m*n, MPI_DOUBLE, 0, comm);
> 		
> 	}
> }
> ```

We can use [[03 - MPI, Collective Communication#`MPI_Allgather`|MPI_Allgather]] to perform steps 4&5 at once.

```C
void Mat_vect_mult(
	double   local_A[], // in
	double   local_x[], // in
	double   local_y[], // out
	int      local_m,   // in
	int      n,         // in
	int      local_n,   // in
	MPI_Comm comm,      // in
) {
	double* x;
	int local_i, j;
	x = malloc(n*sizeof(double));
	
	// gather x from the different processes
	// (all the processes will call Mat_vect_mult)
	MPI_Allgather(local_x, local_n, MPI_DOUBLE, x, local_n, MPI_DOUBLE, comm);
	
	for (local_i=0; local_i<local_m; local_i++) {
		local_y[local_i] = 0.0;
		for (j=0; j<n; j++)
			// only local_m rows are used
			local_y[local_i] += local_A[local_i*n+j]*x[j];
	}
		
		// allgather to y (steps 4&5)
	    MPI_Allgather(local_y, local_m, MPI_DOUBLE, y, local_m, MPI_DOUBLE, comm);
	
	free(x);
	free(y);
}
```

(so, in the `main` function, one would call `Read_matrix` first and then `Mat_vect_mult`)