---
sticker: lucide//align-horizontal-justify-start
---
Le classi che rappresentano sequenze di elementi (array, stringhe...) hanno in comune il fatto che è possibile **iterare sui loro elementi**.
È possibile implementare un'interfaccia iterabile, ma Java fornisce già le funzioni necessarie:

- `java.lang.Iterable` - implementa il metodo `iterator()`, che ritorna un iterabile.
 
e `java.util.Iterator`, che espone i metodi:

| metodo              | descrizione                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| `boolean hasNext()` | restituisce true se esiste ancora un successivo elemento nella collezione |
| `E next()`          | restituise l'elemento successivo                                          |
| `void remove()`     | rimuove l'elemento corrente                                               |
|                     |                                                                           |
