

## MPI
- same program by multiple processes w/message passing
- message sending and receiving

communication can be:
- buffered ⟶ the sending operation is always locally blocking (it will return as soon as the message is copied to a buffer), and the buffer is *user-provided*
- synchronous ⟶ the sending operation will return only after the destination process has initiated and started the retrieval of the message (**globally blocking** - the sender can be sure of the point the receiver is at without any further explicit communication)
- ready ⟶ the send operation will only succeed if a matching receive operation has already been initialised (otherwise, it returns an error code); used to reduce the overhead of handshaking operation

+can be blocking or non-blocking


