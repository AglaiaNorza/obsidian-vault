è possibile passare riferimenti a metodi esistenti, utilizzando la sintassi:
- `Classe::metodoStatico`
- `riferimentoOggetto::metodoNonStatico`
- `Classe::metodoNonStatico`
 
```java
Converter<String, Integer> converter = Integer::valueOf; 

Integer converted = converter.convert("123");
```

###### riferimento a metodi d'istanza usando il nome di classe vs usando un riferimento a un oggetto
- nel caso di `rifOggetto::metodo`, il metodo verrà chiamato **sull'oggetto riferito**
- nel caso di `nomeClasse::metodo`, **non stiamo specificando su quale oggetto** applicare il metodo
	- il metodo è d'istanza, quindi utilizza membri d'istanza (campi, metodi)
	- ci si riferisce al *metodo implicitamente esteso* con un primo parametro aggiuntivo: un riferimento a un oggetto della classe cui appartiene il metodo
