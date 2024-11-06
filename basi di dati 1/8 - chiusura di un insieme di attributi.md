### cosa vogliamo ottenere?

Quando si decompone uno schema di relazione R su cui è definito un insieme di dipendenze funzionali F, oltre ad ottenere **schemi 3NF** occorre:
- **preservare le dipendenze**
- poter **ricostruire tramite join** tutta e sola l'informazione originaria.

Le dipendenze funzionali che si vogliono preservare sono tutte quelle che sono **soddisfatte da ogni istanza legale di R** - le dipendenze funzionali in $F^+$.

Vogliamo quindi calcolare $F^+$, ma questo richiede tempo - è sufficiente avere un metodo per decidere se una dipendenza funzionale $X\to Y\in F^+$. Questo può essere fatto **calcolando $X^+$** e **verificando se $Y\subseteq X^+$**.
Infatti, ricordiamo il [[6 - chiusura di un insieme di dipendenze funzionali|lemma 1]]: $X\to Y\in F^A\iff Y\subseteq X^+$ e il  [[6 - chiusura di un insieme di dipendenze funzionali|teorema]] che dimostra che $F^A=F^+$.
### come calcolare $X^+$
![[algoritmo-X+.png]]

>[!example] esempio 
>$$F=\{AB\to C,\: B\to D,\: AD\to E,\: CE\to H\}$$
> $$R=ABCDEHL$$


#### teorema: l'algoritmo è corretto
L'algoritmo "calcolo di $X^+$" calcola correttamente la chiusura di un insieme di attributi $X$ rispetto ad un insieme $F$ di dipendenze funzionali.

>[!info] dimostrazione
>Indichiamo con $Z^0$ il valore iniziale di Z $Z^0=X$ e con $Z^i$ ed $S^i$, con $i\geq1$, i valori di $Z$ e $S$ dopo l'i-esima esecuzione del corpo del ciclo.
>È facile vedere che $Z^i \subseteq Z^{i+1}$
>
>Sia $j$ tale che $S^j \subseteq Z^j$ con $Z^j$ valore di $Z$ quando l'algoritmo termina.
>
>Proveremo che $A\in Z^j\iff A\in X^+$ 
>
>DIMOSTRAZIONE PRESA A MANO DA COPIARE

### proprietà dell'insieme vuoto
- l'insieme vuoto $\emptyset$ è un **sottoinsieme di ogni insieme** A: $\forall A:A$
=======
#### come calcolare $X^+$
![[algoritmo-X+.png]]