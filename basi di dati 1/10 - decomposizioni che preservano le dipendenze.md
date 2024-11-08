bisogna formalizzare il concetto di *decomposizione che preserva un insieme di dipendenze funzionali*.

>[!info] definizione di decomposizione
>Sia $R$ uno schema di relazione. Una **decomposizione** di $R$ è una famiglia $\rho=\{ R_{1},R_{2},\dots R_{k}\}$ di sottoinsiemi di $R$ che ricopre $R$, ovvero:
>$$\large\bigcup_{i=1}^kR_{i}=R$$
>- essenzialmente, decomporre $R$ significa definire dei sottoschemi che contengono ognuno un sottoinsieme degli attributi di $R$.

La proiezione di $F$ su un certo elemento $R_i$ contiene:
- le dipendenze funzionali di $F^+$la cui unione di determinante e determinato fa parte di $R_{i}$ (quindi le dipendenze con elementi in $R_{i}$)

Visto che due insiemi di dipendenze si possono scambiare quando hanno la stessa chiusura, una decomposizione preserva $F$ se la chiusura di $F$ è uguale alla chiusura dell'insieme $G = \{\text{unione delle proiezioni di F sui vari } R_{i}\}$.

>[!info] equivalenza tra due insiemi di dipendenze funzionali
>Siano $F$ e $G$ due insiemi di dipendenze funzionali. 
>$F$ e $G$ sono **equivalenti** $(F\equiv G)$ se $F^+=G^+$.
>- ovvero non sono uguali ma hanno la *stessa chiusura*.

### lemma 2
Siano $F$ e $G$ due insiemi di dipendenze funzionali. Se $F\subseteq G^+$ allora $F^+\subseteq G^+$ (in realtà è un $\iff$, ma l'altra implicazione è banale).

>[!note] dimostrazione $F\subseteq G^+\implies F^+\subseteq G^+$
>Sia $f\in F^+-F$ (una dipendenza di $F^+$ che non compare in $F$).
>- noi sappiamo che ogni dipendenza funzionale in $F$ è derivabile da $G$ mediante gli assiomi di Armstrong (perché $F\subseteq G^+$, e $G^+=G^A$, quindi le dipendenze di $F$ sono dipendenze di $G^A$)
>- anche $F^+(=F^A)$ è derivabile da $F$ tramite gli assiomi di Armstrong.
>- continuando ad applicare gli assiomi di Armstrong in $G^+$ (per ricavare $F^+$), non "esco"  da $G^+$, le cui dipendenze sono state trovate con gli assiomi di Armstrong
>- quindi, $f\in F^+ -F$  è derivabile da $G$ con gli assiomi di Armstrong, e $F^+\subseteq G^+$

### preservare le dipendenze

>[!info] definizione
>Sia $R$ uno schema di relazione, $F$ un insieme di dipendenze funzionali su $R$, e $\rho=\{ R_{1},R_{2},\dots,R_{K}\}$ una decomposizione di $R$.
>Diciamo che **$\rho$ preserva $F$** se:
>$$\large F\equiv\bigcup_{i=1}^k\pi_{Ri}(F)$$
>dove $\pi_{Ri}(F)=\{ X\to Y\mid X\to Y\in F^+\land XY\subseteq R_{i} \}$
>- ogni $\pi_{Ri}$ è un insieme di dipendenze funzionali dato dalla proiezione di $F$ su $R_i$
>	- proiettare un insieme di dipendenze su un sottoschema significa prendere tutte e sole le dipendenze in *$F^+$* che hanno *tutti gli attributi in $R_i$*
#### verifica
Supponiamo di avere una decomposizione e voler verificare se preserva le dipendenze funzionali.
Questo corrisponde a verificare che $G \equiv F$, ovvero che $G^+\subseteq F^+$ e che $F^+\subseteq G^+$.

> [!tip] utilità del lemma 2 per la verifica
> Grazie al *lemma 2*, per verificare che $F^+=G^+$ mi basta verificare che $F\subseteq G^+$ e che $G^+\subseteq F$.

La verifica di $G\subseteq F^+$ è superflua, perché tutti gli elementi di $G$ sono necessariamente in $F^+$ 
- (infatti $G$ è definito come l'unione della proiezione di $F$ sulle varie decomposizioni, quindi l'unione di tutte le dipendenze di $F^+$ che hanno determinante e dipendente in $R_i$ -> è possibile che in $G$ non ci siano alcune dipendenze di $F^+$, ma non il contrario)

Quindi, bisogna solo verificare che $F\subseteq G^+$.

Grazie al [[6 - chiusura di un insieme di dipendenze funzionali#lemma 1|lemma 1]], mi basta verificare che 
$$\forall X\to Y \in F,\,\,Y\subseteq X_{G}^+$$

Si può fare con l'algoritmo che segue:
- basta verificare che **una sola dipendenza non appartiene alla chiusura di G** per affermare che l'equivalenza non sussiste

> [!summary] algoritmo
> - input - due insiemi $F$, $G$ di dipendenze funzionali su $R$
> - output - la variabile `successo`, che indica se $F\subseteq G^+$
> 
> $$
> \begin{align}
> &\text{begin}\\
> &\qquad\text{successo}:=true\\
> &\qquad \text{for every }X\to Y\in F\\
> &\qquad\text{do}\\
> &\qquad \text{begin}\\
> &\qquad\qquad\text{calcola } X^+\\
> &\qquad\qquad \text{if }Y\not\subset X^+_{G} \text{ then successo}:=false\\
> &\qquad\text{end} \\
> &\text{end}
> \end{align}
> $$
>
>- se $Y\not\subset X^+_{G}$, allora $X\to Y \not\in G^A$ per il lemma, ovvero $X\to Y\not\in G^+$ per il Teorema
> 

Nasce un problema: come calcoliamo $X^+_{G}$? Potremmo usare l'[[8 - chiusura di un insieme di attributi#come calcolare $X +$|algoritmo]] per il calcolo della chiusura di un insieme di attributi, ma dovremmo prima calcolare $G$, e quindi $F^+$, il che richiederebbe tempo esponenziale.

Per questo, esiste un algoritmo:
### calcolo della chiusura di X rispetto a G a partire da F

- **input** - uno schema $R$, un insieme $F$ di dipendenze funzionali su $R$, una decomposizione $\rho=\{ R_{1},R_{2},\dots,R_{k} \}$, un sottoinsieme $X$ di $R$.
- **output** - la chiusura di $X$ rispetto a $G=\cup_{i=1}^k\pi_{Ri}(F)$

$$
\begin{align}
&\text{begin}\\
&\qquad Z:=X \\
&\qquad S:=\varnothing \\
&\qquad \text{for }i:=1\text{ to }k\\
&\qquad\text{do}\qquad S:=S\cup(Z\cap R_{i})^+_{F}\cap R_{i}  \\
&\qquad\text{while } S\not\subset Z \\
&\qquad\qquad\text{do}\\
&\qquad\qquad \text{begin}\\
&\qquad\qquad\qquad Z:=Z\cup S\\
&\qquad\qquad\qquad \text{for }i:=1\text{ to }k \\
&\qquad\qquad\qquad\text{do}\qquad S:=S\cup(Z\cap R_{i})^+_{F}\cap R_{i} \\
&\qquad\qquad\text{end} \\
&\text{end}
\end{align}
$$

- partendo da un sottoinsieme di attributi $X$ di $R$, per prima cosa definiamo $Z$ come $X$ stesso per riflessività.
- dopodiché, ad ogni iterazione:
	$$S:=S\cup(Z\cap R_{i})^+_{F}\cap R_{i}$$fa: 
	- prima l'interzezione tra $Z$ e $R_i$, per considerare *solo gli elementi di $Z$ che riguardano quello specifico sottoinsieme*
	- poi la chiusura di quell'intersezione rispetto ad $F$, per trovare tutti gli attributi che ci interessano (tutti quelli determinati da dipendenze in $F^+$)
	- dopodiché l'intersezione con $R_i$, perché dobbiamo *tenere solo gli attributi che sono effettivamente in $R_i$* (per la questione dipendenze con det e dip in $R_i$)
	- e infine l'unione con l'accumulatore $S$, dove salviamo questo passo fatto per *tutti i sottoinsiemi $R_i$*

>[!info]
>Con $S:=S\cup(Z\cap R_{i})^+_{F}\cap R_{i}$ sostanzialmente si calcola la chiusura in $F$ degli elementi (di cui cerchiamo di calcola la chiusura in $G$) rispetto al sottoschema $R_{i}$, infine facciamo l’intersezione con $R_{i}$ in modo tale da avere al massimo tutti gli attributi contenuti di $R_{i}$.
>In questo modo rispettiamo la definizione di $G=\cup_{i=1}^k\pi_{R_{i}}(F)$


ma l'algo di calcolare chiusura x rispetto a g va usato solo per quelle dipendenze "a cavallo"

l'algo a partire da F ricalca le definizioni di proiezioni di F.
Z iniz a X per riflessività.
accumulatore inizializzato al vuoto.

Ciclo sui sottoschemi - vado a verificare le proiezioni di F, prendo i pezzi della chiusura di X che sono imputabili a qualche sottoschema.
