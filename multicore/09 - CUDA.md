## CPUs vs GPUs



**CPU**s are **latency-oriented** (latency = time taken to complete a single task). 
They aim for high clock frequency, and feature:
- large caches, to convert long latency memory to short latency cache accesses
- sophisticated control mechanisms to reduce latency (like branch prediction, out-of-order execution etc)
- powerful ALUs (which carry out the actual computation) (each ALU is considered a core)

> [!info] architecture
> ![[CPU.png|center|450]]

**GPUS** are **throughput-oriented** (throughput = amount of work done for unit of time). They feature:
- moderate clock frequency
- **small caches**
- **simple control** (no branch prediction, execution is done in order)  
	- control units are very small, which means there are a lot more of them
	- 32-thread blocks (called warps) share one controlling unit (they all execute the same assembly instruction)
- **high bandwith memory** (way higher than that used by CPU and DRAM) 
	- CPU works on DRAM, GPUs have their own memory
	- needs to be higher because many more cores are trying to access it - the latency in memory access is masked by the high amount of cores present


> [!info] architecture
> ![[GPU.png|center|450]]

>[!summary] CUDA-capable GPUs
> ![[CUDA-GPU.png|center|550]]
> 
> features:
> - *CUDA cores* (streaming processors) ⟶ ALU-like components, optimised for parallel code execution
> - *streaming multiprocessors* ⟶ CUDA cores on the same SM share control logic and instruction cache

>[!summary] CPU vs GPU applications
>So, in summary:
>- CPUs are oriented towards *sequential* parts where *latency* matters (CPUS can be 10+x faster than GPUS for sequential code)
>- GPUs are oriented towards *parallel* parts where *throughput* matters (GPUs can be 10+x faster than CPUs for parallel code)
>

## CPU-GPU architecture

There are many ways to link GPUs to CPUs

![[CPU-GPU-architecture.png|center|500]]
- (a) older architecture where GPU, CPU and RAM are all connected to the *northbridge*
	- the GPU is connected to the northbridge via a high-speed link like PCIe (express)
	- the data transfer between CPU and GPU (or RAM and VRAM) must pass through the northbridge, adding latency and extra steps
 - (b): a common architectured used today, the *memory controller* (that handles RAM communication) is removed from the northbridge and placed *on the CPU itself* 
 - (c): architecture of the modern integrated systems, CPU an GPU cores are combined onto a *single chip package*, often called an *APU*
	- the CPU and GPU are physically integrated, and share the same system RAM. this eliminates the need to copy data between separate VRAM and RAM
	- the communication between CPU and GPU is extremely fast

(grz diego)

## GPU software development platforms
the main GPU software delopment platforms are:
- **CUDA**: provides 2 sets of APIs (high-level and low-level). **only for NVIDIA hardware** (however there are tools to run CUDA code on AMD GPUs)
- **HIP**: AMD’s equivalend of CUDA. most calls are the same, with only the first 4 characters changing (CUDA-command ⟶ HIP-command)
	- there are tools to convert CUDA code to HIP
- *OpenCL*  (*open computing language*): open standard for writing programs that can execute across a variety of heterogeneous platforms that include GPUs, CPUs, DSPs or other processors. its supported by both NVIDIA and AMD, and is the primary development platform of the latter
- *OpenACC*: open standard for an API that allows the use of compiler directives (like openMP !) to automatically map computations to GPUs or multicore chips, according to the programmer
there are many more …
---
Il problema di CUDA e' che funziona solo su GPU nvidia (anche se ormai esistono tool per compilare per GPU AMD)

- **HIP** is AMD's equivalent of CUDA 
-

other options are OPENCL and OPENACC (portable both to GPs and CPU/GPUs)

---
CUDA enables a general-purpose programming model on NVIDIA GPUs
- initially created for 3d graphics, then adapted to the general public

It enables explicit GPU memory management.

The GPU is viewed as a **compute device** that:
- is a *co-processor* to the CPU
- has its own DRAM ("global memory")
- runs many threads in parallel

>[!summary] CUDA program structure
> 1) **Allocate** GPU memory
> 2) **Transfer data** from host to GPU memory
> 3) Run CUDA **kernel** (functions executed on the GPU)
> 4) (when the kernel is done) **Copy results** from GPU memory to host memory


