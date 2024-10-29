
> [!note]- fattoriale iterativo
> ```
> factorial:
> 	subi $sp, $sp, 4
> 	sw $a0, ($sp)
> 
> li $v0, 1
> 
> While:
> 	blez $a0, Endwhile
> 	mul $v0, $v0, $a0
> 	sub $a0, $a0, 1
> 	j While
> 
> Endwhile:
> 	lw $a0, ($sp)
> 	addi $sp, $sp,4 
> 	jr $ra
> ```

```
factorial:
	blez $a0, BaseCase

RecursiveStep:
	subi $sp, $sp, 8
	sw, $ra, 0($sp)
	sw $a0, 4($sp)


	subi $a0, $a0, 1
	jal factorial #recursive call

	lw $a0, 4($sp)
	lw $ra, 0($sp)
	addi $sp, $sp, 8

	mul $v0, $v0 $a0
	
	jr $ra
	
BaseCase:
	addi $v0, $zero, 1
	
	jr $ra
```