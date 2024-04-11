---
sticker: lucide//folder-open
tags:
  - classi
---
Java consente di scrivere classi **all'interno di altre classi** - classi annidate, **nested class**.
Le nested class possono essere:
- `static`
- `non-static` - vengono dette *inner class*.

#### inner class
- possono essere `public`, `protected` o `private`.
- per poter creare un oggetto della inner class è necessario istanziare un oggetto della classe top-level che la contiene.
- ciascuna classe interna ha un *riferimento implicito all'oggetto della classe che la contiene*
- dalla classe interna è possibile accedere a **tutte le variabili e metodi della classe esterna**.

Per istanziare la classe interna da quella esterna è sufficiente `new`.
Per istanziare la classe interna da un'altra classe si usa la sintassi:
```java
riferOggClassEsterna.new ClasseInterna()
```

L'accesso a campi e metodi degli oggetti di classe interna e esterna avviene normalmente.
 
>[!tip] disambiguare
>In casi di ambiguità come campi con lo stesso nome:
>- se dalla **classe interna** viene usato `this`, si fa riferimento a campi e metodi di quella classe
>- per far riferimento alla **classe esterna** - prima di `this` si inserisce il nome della classe esterna e un punto (`Classe.this`)

--- 
#### classi annidate statiche
Se la classe interna è statica, essa **non richiede l'esistenza di un oggetto** della classe esterna e *non ha un riferimento implicito ad essa*.
- come per i metodi statici, non ha accesso allo stato degli oggetti della classe esterna.
A livello di comportamento, sono equivalenti a classi top-level inserite in altre classi top-level.

Sono accessibili con la sintassi:
```java
new ClassEsterna.ClasseAnnidataStatica()
```
---

>[!question] why?
>- **raggruppamento logico** delle classi (se due classi sono utili solo una per l'altra, ha senso raggrupparle)
>- **incapsulamento** (una classe B annidata può essere nascosta all'esterno)
>- codice più leggibile e mantainability

---
