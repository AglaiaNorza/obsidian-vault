### aritmetiche
![[arithmetic ops.png]]
### logiche
![[logical ops.png]]
### data transfer
![[loads.png]]

| instr  | ex            | meaning   | comment                                            |
| ------ | ------------- | --------- | -------------------------------------------------- |
| `move` | `move $1, $2` | `$1 = $2` | pseudo-instruction, copy from register to register |
##### caricare 32 bit
Nessuna istruzione permette di caricare 32 bit tutti insieme:
l'idea è di spezzare l'istruzione in due da 16.
un **load upper immediate** + un **or immediate**
>[!example]- esempio
>caricare la sequenza `0000 0000 1111 1111 0000 1001 0000 0000` nel registro `$s0`:
>```java
>lui $t0, 255  //carica 255 seguito da tutti 0 in $t0
>//ovvero 0000 0000 1111 1111
>ori $s0, $s0, 2304
>//or tra il valore caricato prima e 2304 
>//(il resto delle cifre, che in or con 0 "passeranno" tutte)
>
>```


### branch
![[branch.png]]

### jump
![[jump.png]]

differenza tra jump e branch:
- il **jump** porta il PC a puntare alla locazione in memoria del text segment all’indirizzo dato.
- per il **branch**  l'Indirizzo non è assoluto, ma uno scostamento in word relativo al PC.
### altro
per altro, ecco il pdf completo:
[[MIPS Instruction Set.pdf]]