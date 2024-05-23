#### strategy pattern
- progettiamo un'**interfaccia funzionale** per ogni comportamento
- per ogni possibile tipo di comportamento *implementiamo l'interfaccia*

![[interfacce e comportamenti .png|center|500]]
![[esempio anatra comportamenti.png|center|500]]

#### observer observable

> [!Example] esempio
> un esempio valido è quello di un abbonamento:
> - ci si abbona a un determinato settimanale e, ogni volta che viene stampata una nuova edizione, questa viene consegnata.
> - si cancella l'abbonamento quando non si vogliono più ricevere copie, ma l'abbonamento rimane "disponibile"

![[observer observable.png|center|500]]

- è essenziale che le classi osservabili **non dipendano** da quelle che osservano


| metodo                            | cosa fa                                                                                                                          |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `void addObserver(Observer o)`    | aggiunge un observer alla lista di observer dell'oggetto                                                                         |
| `void deleteObserver(Observer o)` | elimina un dato observer dalla lista di observer dell'oggetto                                                                    |
| `void deleteObservers()`          | elimina tutti gli observers dalla lista                                                                                          |
| `void notifyObservers()`          | se l'observable è cambiato, notifica tutti gli osservatori e chiama il metodo `clearChanged` per indicare che non è più cambiato |
| `void clearChanged()`             | indica che il metodo non è più cambiato                                                                                          |
| `protected void setChanged()`     | segna questo oggetto come "cambiato" - ora `hasChanged` ritornerà `true`                                                         |
| `boolean hasChanged()`            | testa se l'oggetto è cambiato                                                                                                    |
