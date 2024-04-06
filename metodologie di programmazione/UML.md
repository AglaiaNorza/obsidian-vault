---
sticker: lucide//book-copy
---
linguaggio di modellazione specifica per l'object-oriented programming.

##### diagrammi delle classi
permettono di rappresentare progetti.
 
![[UML e analisi.png]]
![[diagrammi classi.png]]

- definire la staticità: `<static>`
- si può taggare anche il metodo costruttore con `<constructor>`
- `-->` indica la dipendenza generica tra due classi (es. punto e segmento) - la freccia parte dalla classe che dipende e arriva a quella da cui dipende

##### relazione di estensione
per indicare il fatto che una classe è sottotipo di un'altra classe, si utilizza una freccia
![[estensione.png]]

### is-a vs has-a
c'è un'importante differenza tra le relazioni del tipo **is-a** e quelle di tipo **has-a**:
1) **is-a** rappresenta l'**ereditarietà** (un oggetto di una sottoclasse può essere trattato come uno della superclasse)
2) **has-a** rappresenta la **composizione** (un oggetto contiene come membri riferimenti ad altri oggetti)
 
![[isahasa.png | 500]]

![[comp-aggreg.png | 500]]