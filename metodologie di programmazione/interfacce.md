---
sticker: lucide//monitor
---
parola chiave `interface`.
Le interfacce permettono di modellare **comportamenti comuni** a classi (anche se non sono in relazione gerarchica) - infatti, in Java non è consentito estendere più di una classe, ma una classe può implementare tutte le interfacce desiderate.

- definiscono e standardizzano l'interazione fra oggetti tramite un insieme di operazioni limitato
- specificano solo il **comportamento** che un oggetto deve presentare all'esterno (quello che l'oggetto può fare) - l'*implementazione* di tale operazioni *non viene definita*.
<br/>
- sono classi astratte se non definiamo metodi di default.
##### metodi e interfacce
- è possibile specificare delle implementazioni di *default* di metodi non statici mediante la parola `default`.
- è anche possibile implementare *metodi statici* (che non godono di polimorfismo).
- da java 9 in poi, è possibile definire *metodi privati* all'interno di un'interfaccia (che possono essere chiamati solo dai metodi dell'interfaccia stessa).
---
Un'interfaccia è una classe che può contenere soltanto:
- <font color="#e5b9b7">costanti</font>
- <font color="#e5b9b7">metodi astratti</font>
- (java 8): implementazione di default di <font color="#e5b9b7">metodi </font>e metodi statici
- (java 9): <font color="#e5b9b7">metodi privati </font>tipicamente da invocare in metodi di default
--- 
>[!info] visibilità di default
>- tutti i **metodi** dichiarati in un'interfaccia sono implicitamente public abstract.
>- tutti i **campi** dichiarati in un’interfaccia sono implicitamente public static final.

>[!warning] attenzione
>Tranne nel caso dei metodi di default o statici, non è possibile specificare alcun dettaglio implementativo dei metodi.

![[interfaccia es.png | 480]]

--- 
### implementazione
Per realizzare un'interfaccia, è necessario che una classe la **implementi** tramite la parola chiave `implements`.
- una classe che implementa un'interfaccia espone pubblicamente il comportamento descritto dall'interfaccia
- è obbligatorio che ogni metodo abbia la *stessa intestazione* che presenta nell'interfaccia.

buco

---
#### interfaccia java.util.Iterator
- interfaccia che permette di **iterare su collezioni**.
 
espone **3 metodi**:	

| metodo              | descrizione                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| `boolean hasNext()` | restituisce true se esiste ancora un successivo elemento nella collezione |
| `E next()`          | restituise l'elemento successivo                                          |
| `void remove`       | rimuove l'elemento corrente                                               |
 
 --- 
##### relazione interfacce-classi
Quando una classe C implementa un'interfaccia I, tra queste due classi c'è una relazione di tipo **is-a** - C è di tipo I.

- anche per le interfacce valgono le regole del polimorfismo