- si definiscono specificando `static` nell'intestazione del campo

accesso:
- dall'interno della classe con `nomeCampo`
- dall'esterno con `NomeClasse.nomeCampo`

##### importazione statica di campi
- `import static` permette di importare campi statici come se fossero definiti nella classe in cui si importano
```java
import static java.lang.Math.E
```

- è anche possibile importare **tutti i campi statici** di una classe attraverso l'espressione regolare "*":
	```java
	import static java.lang.Math.*
	```