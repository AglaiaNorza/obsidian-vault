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
\begin{align*}
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
\end{align*}
$$

<small>(latex algoritmo rubato a [flavio](https://github.com/thegeek-sys/Vault/blob/main/Class/Basi%20di%20dati/Chiusura%20di%20un%20insieme%20di%20attributi.md) con piccoli cambiamenti)</small>

- per prima cosa, si definisce $Z$ come $X$ stessa (infatti, per riflessività, come minimo $X\to X$) 
- poi si definisce $S$, un accumulatore per i nuovi attributi, come 
  $$S:=\{A \;\text{ t.c. }\; Y\to V \in F \, \land \, A\in V \land\, Y \subseteq Z\}$$
  quindi, partendo da $Z=X$, cerco una dipendenza $Y\to V$ con $Y\subseteq Z$ (quindi che abbia come determinante un pezzo di $X$) e metto nell'accumulatore ogni $A$ elemento del dipendente. Dire $Y\subseteq X$ vuol dire $X\to Y$ (riflessività), perciò, per transitività, $X\to Y,\,Y\to V \implies X\to V$
 

> [!tip] Essenzialmente, $S$ *prende le dipendenze con un determinante contenuto in $X$* e le mette nella sua chiusura.
- dopodiché, controlla se ha aggiunto cose nuove a $S$ (ovvero se $S\not\subset Z$) :
	- se ha aggiunto nuove dipendenze, ridefinisce $Z$ come $Z\cup S$ (aggiunge l'accumulatore a $Z$) e riapplica l'algoritmo (perché le nuove aggiunte possono essere usate per trovare altre dipendenze)
	- altrimenti,vuol dire che ha finito di trovare altre dipendenze e $Z$ è completo


>[!tip]- slide algoritmo
>![[algoritmo-X+.png]]


>[!example] esempio 
>$$R=ABCDEH$$
>$$F=\{AB\to CD,\;EH\to D,\;D\to H\}$$
>$AB^+=ABCDH$
 
#### teorema: l'algoritmo è corretto
L'algoritmo "calcolo di $X^+$" calcola correttamente la chiusura di un insieme di attributi $X$ rispetto ad un insieme $F$ di dipendenze funzionali.

>[!note] dimostrazione
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
>- **ipotesi induttiva**: poniamo per ipotesi induttiva che $Z^{i-1}\subseteq X^+$ 
>	- (ricordiamo che per il *lemma 1* abbiamo quindi: $X\to Z^{i-1}\in F^A$)
>
>###### passo induttivo
>Prendiamo $A\in Z^i-Z^{i-1}$, ovvero aggiunto all'ultimo passo.
>Vuol dire che $A$ è stato aggiunto perché $\exists \,Y\to W:Y\subseteq Z^{i-1}\land A\in W$ <small>(a è determinato da qualcosa che si trovava in $Z^{i-1}$).</small>
>
>Per ipotesi induttiva, ho $Z^{i-1}\subseteq X^+$, quindi, per decomposizione ($Y\subseteq Z^{i-1}$) per il *lemma 2*, $X\to Y\in F^A$.
>Per transitività, da $X\to Y,\;Y\to W$ <small>(che è in $F$ e quindi in $F^A$)</small> ottengo $X\to W\in F^A$. Per il *lemma 2*, ho quindi $A\in X^+$.
>
>>quindi, visto che $A\in Z^i-Z^{i-1}\in X^+$ e per ipotesi induttiva $Z^{i-1}\in X^+$, ho dimostrato $Z^i\in X^+$
>
>##### parte $A\in X^+\implies A\in Z^j$
>Sia $A\in X^+$. Sappiamo, per il *lemma due*, che $X\to A\in F^A=F^+$ (per il teorema $F^A=F^+$).
>
>Consideriamo la seguente istanza $r$ di $R$:
>
>![[dim-x+.png|center|400]]
>
>che ha due tuple uguali sugli attributi di $Z^j$ ($Z$ finale) e diverse su $R-Z^j$.
>
>###### mostriamo che $r$ è un'istanza legale
>
>Prendiamo una qualunque dipendenza funzionale $V\to W\in F$.
>- se $V\not\subseteq Z^j$ (quindi $V\cap(R-Z^j)\neq \emptyset$) le tuple sono diverse su almeno un attributo di $V$, quindi la dipendenza è rispettata
>
>Se $V\subseteq Z^j$ le due tuple avranno valori uguali su $W$.
>Infatti, se per assurdo avessimo $t_{1}[V]=t_{2}[V]$ ma $t_{1}[W]\neq t_{2}[W]$, ci sarebbe almeno un elemento di $W$ in $R-Z^j$. Questo è impossibile per come è definito l'algoritmo:
>$$S:=\{ A: V\to W\in F\land V\subseteq Z^{i-1}\land A\in W \}$$
>Vorrebbe dire che, applicando l'algoritmo, potrei ancora inserire nuovi elementi in $Z$ - ma questo è impossibile perché, per costruzione, $Z$ è finale. 
>Quindi vuol dire che $W\cap R-Z^j$ è impossibile, e quindi la dipendenza è soddisfatta.
>
>> $r$ è quindi un'istanza legale (rispetta una qualsiasi dipendenza di $F$)
>
>###### dimostriamo l'implicazione
>Visto che $r$ è un'istanza legale, deve soddisfare $X\to A\in F^+$.
>Sappiamo che $X=Z^0\subseteq Z^j$, quindi le due tuple sono uguali su $X$ e lo saranno quindi anche su $A$, quindi $A\in Z^j$.

### proprietà dell'insieme vuoto
- l'insieme vuoto $\emptyset$ è un **sottoinsieme di ogni insieme** A: $\forall A:A$
- l'**unione** di qualunque insieme $A$ con l'insieme vuoto è $A$ stesso: $\forall A:A\cup \emptyset=A$
- l'**intersezione** di qualunque insieme $A$ con l'insieme vuoto è l'insieme vuoto: $\forall A:A\cap \emptyset=\emptyset$
- il **prodotto cartesiano** di un qualunque insieme $A$ con l'insieme vuoto è l'insieme vuoto: $\forall A:A\times \emptyset=\emptyset$
- l'unico **sottoinsieme** dell'insieme vuoto è l'insieme vuoto stesso
- la **cardinalità** dell'insieme vuoto è zero: l'insieme vuoto *è finito*