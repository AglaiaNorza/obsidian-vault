There are two types of parallelism:
- **task parallelism** ⟶ tasks are partitioned amongst cores (an example would be the "temporal parallelism" seen in the CPU pipeline)
- **data parallelism** ⟶ data is partitioned, and different cores carry out similar operations to solve different problems on their part of the data

>[!example] example
>If i need to grade 300 exams, each with 15 questions, and i have 15 assistants:
>- if i make each assistant grade 100 exams, i'm doing *data parallelism*
>- if i'm giving each assistent a subset of questions to grade, i'm doing *task parallelism*

Cores need to coordinate for different reasons:
- **communication** (ex. one core sends its partial sum to another one)
- **load balancing** (the work needs to be shared evenly, so that no core is too heavily loaded)
- **synchronisation** (since each core works at its own pace, we need to make sure that no core gets too far ahead)

