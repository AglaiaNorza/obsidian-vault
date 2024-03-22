---
sticker: lucide//align-left
---
### aritmetiche
![[arithmetic ops.png]]
### logiche
![[logical ops.png]]
### data transfer
![[loads.png]]

| instr  | ex            | meaning   | comment                                            |
| ------ | ------------- | --------- | -------------------------------------------------- |
| `move` | `move $1, $2` | `$1 = $2` | pseudo-instruction, copy from register to register |
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