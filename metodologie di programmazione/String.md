---
tags:
  - tipi
sticker: lucide//text-cursor
---
## metodi:

##### length:
```java
var.length()
```
##### upper/lower case:
```java
var.toLowercase()
var.toUppercase()
```
si ottiene una *nuova stringa* minuscola o maiuscola (la stringa originale non viene modificata).

##### indexing:
è possibile ottenere il k-esimo carattere di una stringa
```java
char c = var.charAt(k);
```

##### slicing:
```java
String s = var.substring(startIndex, endIndex);
```
- startIndex **incluso**, endIndex **escluso**

##### concatenazione:
- due metodi: `+` e `concat`
```java
String s3 = s1+s2;
String s4 = s1.concat(s2);
```
- se si devono concatenare molte stringhe, si può usare la classe `StringBuilder`, con metodi `append(String s)` e `insert(int posizione, String s)`
```java
StringBuilder sb = new StringBuilder();
sb.append(s1).append(s2);
String s5 = sb.toString();
```

##### cercare:
si può cercare la prima posizione di un carattere *o di una sottostringa* con `indexOf`

```java
int k = "happy happy birthday".indexOf('a');
//ritorna 1
int j = "din din don don".indexOf("don");
//ritorna 8
```
>[!warning] attenzione!
>se il carattere/la stringa non è presente, ritornerà -1

anche Java implementa i metodi `startsWith` e `endsWith`.
```java
var.startsWith("hel")
```
##### sostituire:
Java implementa il metodo `replace` , che sostituisce tutte le occorrenze di un carattere o di una stringa.
```java
var.replace(torepl, replwith);

String s1 = "uno_due_tre".replace('_', ' ');
//ritorna "uno due tre"
```

##### confrontare:
le stringhe (e tutti gli altri oggetti) vanno sempre confrontate con il metodo `equals`.
- l'operatore == confronta il riferimento (memoria) quindi dà `True` *solo se si confrontano gli stessi oggetti*.
- l'operatore `equals` **confronta** la stringa **carattere per carattere** e restituisce `True` se le stringhe contengono la stessa sequenza di caratteri

##### split:
il metodo `split` prende in input un'espressione regolare s e restituisce un array di sottostringhe separate da s.
```java
String[] parole = "uno due tre".split(" ");
//parole contiene {"uno", "due", "tre"}
```

