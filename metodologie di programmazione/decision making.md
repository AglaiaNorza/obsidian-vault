---
sticker: emoji//2754
---
#### istruzione if:
la sintassi è:
```java
//singola istruzione
if (<espressione booleana>) <istruzione>;
else <istruzione>;
```

```java
//per più istruzioni
if (<espressione booleana>){

	<istruzioni>;
}
else if (<espr. booleana>{
	<istruzioni>;
}
else{
	<istruzioni>;
}
```

problema del dangling else:
- l'else si riferisce sempre all'*istruzione if immediatamente precedente* (la tabulazione non conta nulla)

#### operatore condizionale(ternario):
sintassi:
```java
condizione ? valoreCasoVero : valoreCasoFalso
```

```java
int abs = x < 0 ? -x : x
```
- è anche detto operatore Elvis.

#### switch case:
utile per lunghissimi if/else
(come case in verilog)
```java
switch(<espressione intera o Stringa>)
{
	case <valore> : <istruzioni>; break;
	case <valore> : <istruzioni>; break;
	case <valore> : <istruzioni>; break;
	default : <istruzioni>; break;
}
```
