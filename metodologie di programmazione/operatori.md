---
sticker: lucide//divide
---
##### incrementi:
- `var++ (var = var +1)`
- `var--`
 
diversi da:
- `++var, --var`

*pre vs post-incremento*:
a++ ha come risultato a, e poi lo incrementa di 1.

```java
int a = 3;
int c = a++
```
qui, c vale 3 (il compilatore dà prima a c il valore di a, e poi aumenta a di 1)

```java
int a = 3;
int c = ++a
```
qui, c vale 4 (e anche a).

quindi:
```java
int a = 4;
int c = 3;
int z = (a++) - (c--);
```
 prima z = 1 
poi a diventa 5 e c diventa 2

##### booleani:
- && - and logico 
- || - or
- ! - not
- ^ - xor

&  e | - and  e or bit a bit (per i binari)
 
##### relazionali:
- ==
- !=
- < , <= , > , >=
- `istanceof`
##### ternario:
- `? :`
 
##### shift:
- `<<,  >>, >>>`
utili per i numeri binari: ogni shift a sinistra moltiplica per 2 (aggiungo uno 0 a destra in un numero binario)


##### precedenza operatori aritmetici
![[operatori.png]]
come in matematica.