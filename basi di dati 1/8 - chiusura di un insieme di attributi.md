### cosa vogliamo ottenere?
Quando si decompone uno schema di relazione R su cui è definito un insieme di dipendenze funzionali F, oltre ad ottenere **schemi 3NF** occorre:
- **preservare le dipendenze**
- poter **ricostruire tramite join** tutta e sola l'informazione originaria.

Le dipendenze funzionali che si vogliono preservare sono tutte quelle che sono **soddisfatte da ogni istanza legale di R** - le dipendenze funzionali in $F^+$.

Vogliamo quindi calcolare $F^+$, ma questo richiede tempo - è sufficiente avere un metodo per decidere se una dipendenza funzionale $X\to Y\in F^+$. Questo può essere fatto **calcolando $X^+$** e **verificando se $Y\subseteq X^+$**.
Infatti, ricordiamo il [[6 - chiusura di un insieme di dipendenze funzionali|lemma 1]] $X\to Y\in F^A\iff Y\subseteq X^+$ e il  [[6 - chiusura di un insieme di dipendenze funzionali|teorema]] che dimostra che $F^A=F^+$.
### come calcolare $X^+$
per il calcolo di $X^+$ possiamo usare il seguente algoritmo:

- input: uno schema di relazione $R$, un insieme $F$ di dipendenze funzionali su $R$, e un sottoinsiee $X$ di $R$
- output: la chiusura di $X$ rispetto a $F$ (nella variabile $Z$)

algoritmo:
$$
\begin{aligned}
&\text{begin} \\
&Z := X \\
&S := \{A \mid Y \to V \in F,\, A \in V,\, Y \subseteq Z\} \\
&\text{while } S \not\subset Z \\
&\quad \text{do} \\
&\quad \text{begin} \\
&\quad \quad Z := Z \cup S \\
&\quad \quad S := \{A \mid Y \to V \in F,\, A \in V,\, Y \subseteq Z\} \\
&\quad \text{end} \\
&\text{end}
\end{aligned}
$$

(latex rubato a flavio cambiato alignment)

- per prima cosa, si definisce $Z$ come $X$ stessa (infatti, per riflessività, come minimo $X\to X$) 
- poi si definisce $S$, un accumulatore per i nuovi attributi, come 
  $$S:={A \mid Y\to V \in F \, \land \, Y \subseteq Z}$$
  quindi, partendo da $X$, devo trovare $Y\to V$ tale che $Y \subseteq Z$ (con $Z$ inizialmente uguale a $X$). Dire che $Y\subseteq X$ vuol dire che $X\to Y$ (per riflessività), perciò $X\to Y$ e $Y\to V$ mi danno per transitività $X\to V$.
  Essenzialmente, $S$ *prende le dipendenze con un determinante contenuto in $X$* e le mette nella sua chiusura.
<br>
- dopodiché, controlla se ha aggiunto cose nuove a $S$ (ovvero se $S\not\subset Z$) :
	- se ha aggiunto nuove dipendenze, ridefinisce $Z$ come $Z\cup S$ (aggiunge l'accumulatore a $Z$) e riapplica l'algoritmo (perché le nuove aggiunte possono essere usate per trovare altre dipendenze)
	- altrimenti,vuol dire che ha finito di trovare altre dipendenze e $Z$ è completo


>[!tip]- slide algoritmo
>![[algoritmo-X+.png]]


>[!example] esempio 
>$$F=\{AB\to C,\: B\to D,\: AD\to E,\: CE\to H\}$$
> $$R=ABCDEHL$$

#### teorema: l'algoritmo è corretto
L'algoritmo "calcolo di $X^+$" calcola correttamente la chiusura di un insieme di attributi $X$ rispetto ad un insieme $F$ di dipendenze funzionali.

>[!info] dimostrazione
>
>![[algo-dim-1.jpg]]
>![[algo-dim-2.jpg]]
>DA FINIRE IL LATEX: v
>
>Indichiamo con $Z^0$ il valore iniziale di $Z$ ($Z^0=X$) e con $Z^i$ ed $S^i$, con $i\geq1$, i valori di $Z$ e $S$ dopo l'i-esima esecuzione del corpo del ciclo.
>È facile vedere che $Z^i \subseteq Z^{i+1}$
>
>Sia $j$ tale che $Z^j$ è $Z^\text{finale}$, ovvero $Z$ al termine dell'algoritmo. Quindi $S(j)\subseteq Z(j)$. 
>Dobbiamo provare
>$$A\in Z^j \iff A\in X^+$$
>
>##### parte $A\in Z^j \implies A\in X^+$
>Si dimostra per induzione.
>
>- **caso base**: $Z^0=X$, per riflessività $X\subseteq X^+$, quindi $X\subseteq X^+ \implies Z^0\subseteq X^+$
>- **ipotesi induttiva**: $Z^{i-1}\subseteq X^+_{f}\implies X\to Z^{i-1}\in F^A$ (per il *lemma 1*: $X\to Y\in F^A\iff Y\subseteq X^+$)
>- **passo induttivo**: 


### proprietà dell'insieme vuoto
- l'insieme vuoto $\emptyset$ è un **sottoinsieme di ogni insieme** A: $\forall A:A$