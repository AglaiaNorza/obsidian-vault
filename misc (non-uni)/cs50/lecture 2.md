### compiling in c
1) preprocessing - handling of the header files
2) compiling - conversion into assembly code
3) assembling - conversion into machine code
4) linking - conversion of the code from the libraries into machine code

### arrays, strings

- Arrays need to be declared by specifying their type, and either their size or the values inside of them.
	`int scores[3];` or `int scores[] = {1,3,4};`
 
 and
- Strings are actually **arrays of chars**, that end with a NUL character (`\0`)

[ for now, cs50 explains strings with the help of their library, but, actually, strings in c have to be declared like so: `char greetings[] = "Hello World!";` ]

**useful libraries**:
- the `string.h` library defines a function called `strlen`, to find out the length of a string
- the `ctype.h` library defines functions to turn chars uppercase and lowercase (`toupper(char)`) and to recognize the "types" of chars passed to it (ex. `isalnum`, `isalpha`, `isspace` etc.)

### command-line arguments

- command-line arguments can be used inside of programs.

they can be accepted by changing the *main* function's header to `int main(int argc, string argv[]` (`char *argv[]`). the arguments need to be typed after the command to execute the code: `./file argument`

- `argc` represents the number of command line arguments, while `argv` is the array of characters passed

### exit status

when a program ends, the computer is provided with an exit code.
the code will be **0** if the program ended without error, or **1** if an error occurred.

