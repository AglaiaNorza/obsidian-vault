![[system calls.png | 350]]
Set di servizi messi a disposizione dal Kernel del Sistema Operativo.
Ogni sistema operativo gestisce le syscalls in maniera diversa, ma in generale si tende a seguire questa struttura:

- **input**:
	- registro `$v0` dentro il quale viene inserito il codice della syscall che si vuole richiedere
	- registri `$a0, $a1, $a2, $f0`, dove vengono inseriti parametri aggiuntivi che verranno letti dalla syscall.
 
- **output**:
	- registri `$v0, $f0`, che contengono eventuali valori restituiti dalla syscall.


| syscall (`$v0`) | descrizione    | argomenti <br>(`$a0`...)                      | risultato <br>(`$v0`...) |
| --------------- | -------------- | --------------------------------------------- | ------------------------ |
| 1               | stampa intero  | intero                                        |                          |
| 4               | stampa stringa | string address                                |                          |
| 5               | leggi intero   |                                               | intero                   |
| 8               | leggi stringa  | `$a0` = buffer<br>address<br>`$a1` = n. chars |                          |
| 10              | fine programma |                                               |                          |

>[!example] esempio: hello world
>```
>.data
>string: .asciiz "Hello, World!"
>
>.text
>main:
>la $a0, string
>li $v0, 4
>syscall
>```