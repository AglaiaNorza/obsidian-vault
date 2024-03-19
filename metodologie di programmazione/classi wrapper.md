---
sticker: lucide//files
---
- permettono di **convertire i valori di un tipo primitivo in un oggetto**
- forniscono metodi di accesso e visualizzazione dei valori
 
![[classi wrapper.png]]
##### confrontare oggetti interi
- i valori interi primitivi si possono confrontare con gli operatori di confronto, ma `new Integer(5) != new Integer(5)`, perché sono oggetti.
- poiché si lavora con oggetti, bisogna usare **metodi per il confronto**:
	- `equals()` - restituisce True se e solo se i due oggetti hanno valori uguali
	- `compareTo()` - restituisce 0 se sono uguali, <0 se il valore del primo oggetto è < di quello in ingresso, >0 altrimenti

##### membri statici delle classi wrapper
- metodi `Integer.parseInt()`, `Double.parseDouble()` ecc.
- metodo `toString()`
- `Character.isLetter()`, `Character.isDigit()`, `Character.isUppercase()` ecc.

#### autoboxing e auto-unboxing
l'**autoboxing** (che usiamo quando definiamo un nuovo wrapper) converte automaticamente un tipo primitivo al suo tipo wrapper associato
- `Integer k = 3;` - viene implicitamente chiamato `new Integer(3)` 

l'**auto-unboxing** converte automaticamente da un tipo wrapper all'equivalente primitivo
- `int j = k;`