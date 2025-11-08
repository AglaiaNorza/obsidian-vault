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

