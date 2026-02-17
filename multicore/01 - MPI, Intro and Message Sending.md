MPI is a library used by [[multicore/00 - intro#types of parallel systems|distributed memory]] systems.
It follows the Single-Program Multiple-Data (SPMD) model, so the same program is executed by multiple processes that communicate through message passing.

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

**knowing how much data is being received**:
```C
int MPI_Get_count(
	MPI_Status*  status_p, // in
	MPI_Datatype type,     // in
	int*         count_p   // out
);
```
- `status_p` ⟶ status of the receive (identifies the communication)
- `type` ⟶ type of data being received
- `count_p` ⟶ "return" value: how many `type`s have been received

> [!summary] data types
> 
> | MPI datatype         | C datatype             |
> | -------------------- | ---------------------- |
> | `MPI_CHAR`           | `signed char`          |
> | `MPI_SHORT`          | `signed short int`     |
> | `MPI_LONG`           | `signed long int`      |
> | `MPI_LONG_LONG`      | `signed long long int` |
> | `MPI_UNSIGNED_CHAR`  | `unsigned char`        |
> | `MPI_UNSIGNED_SHORT` | `unsigned short int`   |
> | `MPI_UNSIGNED`       | `unsigned int`         |
> | `MPI_UNSIGNED_LONG`  | `unsigned long int`    |
> | `MPI_FLOAT`          | `float`                |
> | `MPI_DOUBLE`         | `double`               |
> | `MPI_LONG_DOUBLE`    | `long double`          |
> | `MPI_BYTE`           |                        |
> | `MPI_PACKED`         |                        |
> 

A message is **successfully received** if:
- `recv_type` = `send_type`
- `recv_buf_sz` >= `send_buf_sz` (i can send less bytes than i can receive)

A receiver can get a message without knowing:
- the amount of data in it
- the sender (wildcard `MPI_ANY_SOURCE`)
- the tag of the message (wildcard `MPI_ANY_TAG`)

To find out, you can operate on `&status`, an `MPI_Status`-type argument (the last argument of an `MPI_Recv`):
- `status.MPI_SOURCE` to find the source
- `status.MPI_TAG` to find the tag
- `status.MPI_ERROR` to find the error code

### issues with send and receive
Some things are well-defined (tags, id), but others have been left up to the implementation:
- `MPI_Send` may behave differently with regard to buffer size, cutoffs and blocking
	- with an `MPI_Send`, there is no way of knowing if the message has been sent and whether it has arrived, so the next instruction could be executed with the message still inside the process; the only guarantee is that, when the next instruction is executed, if the buffer (with the message) is modified, the correct data will be sent anyway (even if the message hadn't left yet) (MPI might make a copy of it, or something similar) 
		- different implementations handle this differently

MPI has a buffer for sent messages that haven't been received; if the message is too big, instead of using the buffer, the sender will check if the receiver is ready (*rendezvous*).

`MPI_Receive` blocks the process until the message is received (so, when it ends, there's a guarantee that the buffer has been received).
- if a process tries to receive a message and there's no matching send, the process will hang
- if a call to `MPI_Send` blocks and there's no matching receive, the sending process can hang
- if a call to `MPI_Send` is buffered and there's no matching receive, the message will be lost
- if the rank of the destination process is the same as the source process, the process will hang (or worse, the receive may match another send)

>[!question] what happens when you do a send?
> ![[send-request.png|center|500]]

## point-to-point communication models
As explained above, `MPI_Send` uses the so-called **standard communication mode**: based on the size of the message, it decides whether to block the call until the destination process collects it or (if the message is small enough) to return before a matching receive is issued (**locally blocking**).

There are three more communication models:
- **buffered** ⟶ the sending operation is always locally blocking (it will return as soon as the message is copied to a buffer), and the buffer is *user-provided*
- **synchronous** ⟶ the sending operation will return only after the destination process has initiated and started the retrieval of the message (**globally blocking** - the sender can be sure of the point the receiver is at without any further explicit communication)
- **ready** ⟶ the send operation will only succeed if a matching receive operation has already been initialised (otherwise, it returns an error code); used to reduce the overhead of handshaking operation

the different modes are implemented with `MPI_Bsend()`, `MPI_Ssend()` and `MPI_Rsend()`, that share the same arguments `(void *buf, int count, MPI_Datatype datatype, int dest, int tag, MPI_Comm comm)`

## non-blocking communication
Buffered sends are considered bad for performance (the caller has to wait for the copying to take place). Non-blocking or immediate functions allow communication and computation to overlap by returning immediately upon initiating a transfer.

The downside is that the completion of the operations (for both end-points) has to be queried explicitly for both senders (so that they can re-use or modify the message buffer) and receivers (so that they can extract the content of the messages).

>[!tip] communication modes
> Non-blocking communication can be coupled with any communication mode (`MPI_Isend`, `MPI_Ibsend`, `MPI_Issend` etc)

### functions

**send**:
```C
int MPI_Isend(
	void *buf, // address of data buffer (IN)
	int count, // number of data items (IN)
	MPI_Datatype datatype, // type of buffer elements (IN)
	int dest, // rank of destination process
	int tag, // label to identify the message (IN)
	MPI_Comm comm, // identifies the communicator (IN)
	MPI_Request *req // used to return a handle for checking status (OUT)
)
```

**receive**:
```C
int MPI_Irecv(
	void *buf, // addfess of data buffer (IN)
	int count, // number of data items (IN)
	MPI_Datatype datatype, // type of buffer elements (IN)
	int source, // rank of destination process
	int tag, // label to identify the message (IN)
	MPI_Comm comm, // identifies the communicator
	MPI_Request *req // used to return a handle for checking status (OUT)
)
```

#### check for completion
The non-blocking functions are associated with a wait command that can be blocking or non-blocking.

**blocking** (destroys handle)
```C
int MPI_Wait(
	MPI_Request *req, // address of the handle identifying the
					  // operation queried (IN/OUT)
	                  // the call invalidates *req by 
	                  // setting it to MPI_REQUEST_NULL
	MPI_Status *st // addess of the structure that will hold the 
				   // comm. information (OUT)
)
```

**non-blocking** (destroys handle if operation was successful (i.e. `*flag=1`))
```C
int MPI_Test(
	MPI_Request *req, // address of the handle identifying the
					  // operation queried (IN)
	int *flag, // set to true is operation is complete (OUT)
	MPI_Status *st // addess of the structure that will hold the 
				   // comm. information (OUT)
)
```

There are several variants available, like:
- `Waitall`
- `Testall`
- `Waitany`
- `Testany`

#### `MPI_Sendrecv`
Carries out a **blocking send** and a **receive** in a single, atomic call.
- an alternative to scheduling the communications
- it won't deadlock if two processes simultaneously try to exchange data
- the send and receive operations can target different processes and use different message tags and datatypes (flexible)

> [!summary] header
> ```C
> int MPI_Sendrecv(
> 	void* send_buf_p,            // in
> 	int send_buf_size,           // in
> 	MPI_Datatype send_buf_type,  // in
> 	int dest,                    // in
> 	int send_tag,                // in
> 	void* recv_buf_p,            // out
> 	int recv_buf_size,           // in
> 	MPI_Datatype recv_buf_type,  // in
> 	int source,                  // in
> 	int recv_tag,                // in
> 	MPI_Comm communicator,       // in
> 	MPI_Status* status_p         // in
> )
> ```
