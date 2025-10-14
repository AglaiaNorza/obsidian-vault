From 1986 to 2003, the performance of microprocessors has increased, on average, by 50% per year. But since 2003, the increase has slowed down, getting to about 4% a year. That's why, instead of trying to have more powerful monolithic processors, we are putting multiple processors on a single integrated circuit.
Traditionally, performance increases are caused by increase in the density of transistors, but there are physical limits that make parallel computing necessary (eg. smaller transistors = more power consumption, increased heat).

## writing parallel programs

There are two types of parallelism:
- **task parallelism** ⟶ tasks are partitioned amongst cores (an example would be the "temporal parallelism" seen in the CPU pipeline)
- **data parallelism** ⟶ data is partitioned, and different cores carry out similar operations to solve different problems on their part of the data

>[!example] example
>If i need to grade 300 exams, each with 15 questions, and i have 15 assistants:
>- if i make each assistant grade 100 exams, i'm doing *data parallelism*
>- if i'm giving each assistent a subset of questions to grade, i'm doing *task parallelism*

If each core were to work independently, it would be similar to writing a serial program - we need cores to coordinate, for different reasons:
- **communication** (ex. one core sends its partial sum to another one)
- **load balancing** (the work needs to be shared evenly, so that no core is too heavily loaded)
- **synchronisation** (since each core works at its own pace, we need to make sure that no core gets too far ahead)

To write parallel programs, we'll use four different extensions of the C APIs:
- **Message-Passing Interface** (MPI)
- **Posix Threads** (Pthreads)
- **OpenMP**
- **CUDA**

## types of parallel systems 
There are different types of parallel systems

### memory-wise
- **shared memory** ⟶ the cores can share access to the computer's memory; they are coordinated by having them examine and update shared memory locations
- **distributed memory** ⟶ each core has its own private memory; cores must communicate explicitly by sending *messages* across a network

### instruction-wise
- **multiple-instruction multiple-data** (MIMD)