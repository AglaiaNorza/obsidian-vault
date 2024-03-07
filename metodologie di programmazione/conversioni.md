---
sticker: lucide//arrow-left-right
tags:
  - tipi
---
### conversione esplicita:
utilizza un metodo che prende in ingresso  un argomento di un tipo e ne restituisce uno di un altro.
```java
Integer.parseInt()
Double.parseDouble()
Math.round()
Math.floor()
Math.ceil()
```
### cast esplicito:
anteponendo il tipo desiderato tra parentesi.
```java
(int)2.71828 //produce 2
```
da double a int, viene eliminata la parte decimale (prende la *parte intera*).
### cast implicito:

- Se il tipo di partenza è meno preciso, Java converte automaticamente il valore al tipo più preciso.
```java
double d = 2;
```
int è meno preciso di double, quindi non bisogna specificare (double)2.

può avvenire:

**in fase di assegnazione**:
- byte, short e char possono diventare int.
- int può diventare long.
- float può diventare double.
 
**in fase di calcolo di un'espressione**:
- se un operando è double, tutta l'espressione diventa double.
- sennò, se c'è un float, viene promossa a float.
> [!warning]- precedenza
> in un'espressione, il casting ha precedenza più elevata, quindi prima gli operandi vengono convertiti e poi vengono svolte le operazioni.
>>[!example] es.
>>`(int)42 * 0.4` dà come risultato un double 16.8
### conversioni "inaspettate"
> [!operando "+"]
> Java definisce + sul tipo String.
> Se si effettua una somma con almeno un operando String, Java **converte automaticamente** l'altro operando a String e restituisce una stringa (concatenazione).
```java
String s = (8+5) + "ciao" //s = "13ciao"
```
