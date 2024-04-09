---
sticker: lucide//glasses
tags:
  - classi
---
È possibile definire classi anonime che *implementano un'interfaccia* o *estendono una classe*.
- utilizzate esclusivamente per creare **un'unica istanza**.
- utili per cose "al volo" (es. un iteratore) e codice che non deve essere riutilizzato.

Sintassi:
```java
TipoDaEst unicoRifAOgg = new TipoDaEst(){
	//codice della classe anonima
};
```