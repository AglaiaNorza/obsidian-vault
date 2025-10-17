MPI is a library used by [[multicore/0 - intro#types of parallel systems|distributed memory]] systems.
It follows the Single-Program Multiple-Data (SPMD) model, so a the same program is executed by multiple processes, that communicate through message passing.

MPI's functionalities are included in the C `mpi.h` header file, which needs to be included by any program that uses MPI. Identifiers defined by MPI start with `MPI_`, and the first letter following the underscore is uppercase.

>[!summary] compiling and execution
>
> To compile, run:
>```C
> mpicc -g -Wall -o mpi_hello mpi_hello.c
>```
>
>- `-g` produces debugging information
>- `-Wall` turns on all warnings
>
>To execute, run:
>```C
> mpiexec -n <number of processes> <executable>
>```
>
>- `n` processes will execute the program
>
> Parallel debugging is trickier than debugging serial programs - it can be useful to use MPI with `ddd` (or `gdb`) on one specific process:
>```
> mpiexec -n 4 ./test : -n 1 ddd ./test : -n 1 ./test
>```
>
>- the 5th process is launched under `ddd` 

>[!info] identifying MPI processes
>Every MPI process is defined by a unique nonnegative **rank** (`0` to `p-1`, with `p` = # of processes) 

## communicators
As previously mentioned, MPI processes communicate via messages. 
Communicators are collections of processes that can send messages to each other.
- `MPI_Init()` defines a communicator (called `MPI_COMM_WORLD`) made up of all the processes created when the program is started
- after the MPI calls, before exiting, `MPI_Finalize()` must be called

There are two functions needed to operate with communicators:

```C
int MPI_Comm_size(
	MPI_Comm comm /* in */
	int* comm_sz_p /* out */
)
```

- given a communicator `comm`, it writes the number of processes it contains (cardinality) in `comm_sz_p`, given in input
	- it writes in the pointer given in input instead of returning because the return value is used for the operation's state - whether it was successful, or it returned an error (and which error)

```C
int MPI_Comm_rank(
	MPI_Comm comm /* in */
	int* my_rank_p /* out */
)
```

- writes the rank, relative to `comm`, of the process making the call in `my_rank_p`

## message sending

>[!warning] nonovertaking messages
> MPI requires that messages be **nonovertaking**: if process `q` sends two messages to process `r`, the first message sent by `q` must be available to `r` before the second message.
> - there is no restriction on the arrival of messages sent by different processes

### functions

**sending a message**:
```C
int MPI_Send(
	void*          msg_buf_p, // in
	int            msg_size,  // in
	MPI_Datatype   msg_type,  // in
	int            dest,      // in
	int            tag,       // in
	MPI_Comm       comm       // in
);
```

where:
- `msg_buf_p` ⟶ start address of the memory block that needs to be sent
	- `void*` - any kind of data can be sent
- `msg_size` ⟶ number of elements in the message ($\neq$ number of bytes, the size is deduced from `msg_type`)
- `msg_type` ⟶ type of data that is being sent (types defined by `MPI_Datatype`; new types can be created if needed)
- `dest` ⟶ rank of the receiver
- `tag` ⟶ used to identify messages (optional) - needs to match with the receiver's in its `MPI_Receive`
- `comm` ⟶ communicator to be used

**receiving a message**:
```C
int MPI_Recv(
	void*          msg_buf_p, // in
	int            buf_size,  // in
	MPI_Datatype   buf_type,  // in
	int            source,    // in
	int            tag,       // in
	MPI_Comm       comm,      // in
	MPI_Status*    status_p   // in
);
```

where:
- `msg_buf_p` ⟶ pointer to the address starting from which the data will be written
- `source` ⟶ rank of the sender (can be a special value like `MPI_ANY_SOURCE`)
- `tag` ⟶ has to match the sender's `MPI_Send` `tag`
- `status_p` ⟶ more information about the receive (eg rank of the sender if `MPI_ANY_SOURCE` is used)



A message is successfully received if:
- `recv_type` = `send_type`
- `recv_buf_sz` >= `send_buf_sz` (i can send less bytes than i can receive)

A receiver can get a message without knowing:
- the amount of data in it
- the sender (wildcard `MPI_ANY_SOURCE`)
- the tag of the message (wildcard `MPI_ANY_TAG`)

To find out, you can operate on `&status`, an `MPI_Status`-type argument (the last argument of an `MPI_Recv`)
- `status.MPI_SOURCE` to find the source
- `status.MPI_TAG` to find the tag
- it also offers `status.MPI_ERROR` (to find the error ?)

### issues with send and receive
Some things are well-defined (tags, id), but others have been left up to the implementation:

- MPI_Send - non so se il messaggio sia partito o arrivato - passo all'istruzione successiva, e il messaggio potrebbe essere ancora all'interno del processo - l'unica garanzia che ho è che, quando eseguo l'istruzione successiva, se modifico il buffer da inviare/inviato, i dati inviati saranno comunque corretti, anche se il messaggio non dovesse essere partito (forse MPI fa una copia, o per altri motivi)
	- different implementations handle this differently

MPI ha un buffer per i messaggi inviati ma non ricevuti da nessuno (nessuno ha chiamato la funzione con i parametri giusti) - ma, se il buffer è troppo grande, chi invia controlla se il ricevente è pronto a ricevere (rendezvous).

La receive si blocca fino a quando il messaggio non viene ricevuto (quindi, quando termina, ho la garanzia che il buffer sia stato ricevuto).
- if a process tries to receive a message and there's no matching send, the process will hang
- if a call to `MPI_Send` blocks and there's no matching receive, the sending process can hang

>[!question] what happens when you do a send?
> ![[send-request.png|center|500]]


