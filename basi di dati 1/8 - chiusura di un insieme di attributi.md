### cosa vogliamo ottenere?

Quando si decompone uno schema di relazione R su cui è definito un insieme di dipendenze funzionali F, oltre ad ottenere **schemi 3NF** occorre:
- **preservare le dipendenze**
- poter **ricostruire tramite join** tutta e sola l'informazione originaria.

Le dipendenze funzionali che si vogliono preservare sono tutte quelle che sono **soddisfatte da ogni istanza legale di R** - le dipendenze funzionali in $F^+$.

Vogliamo quindi calcolare $F^+$, ma questo richiede tempo - è sufficiente avere un metodo per decidere se una dipendenza funzionale $X\to Y\in F^+$. Questo può essere fatto **calcolando $X^+$** e **verificando se $Y\subseteq X^+$**.
Infatti, ricordiamo il [[6 - chiusura di un insieme di dipendenze funzionali|lemma 1]]: $X\to Y\in F^A\iff Y\subseteq X^+$ e il  [[6 - chiusura di un insieme di dipendenze funzionali|teorema]] che dimostra che $F^A=F^+$.

#### come calcolare $X^+$
![[algoritmo-X+.png]]


dimostrazione da aggiungere