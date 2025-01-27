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
Siano $F$ e $G$ due insiemi di dipendenze funzionali. $F\subseteq G^+ \iff F^+\subseteq G^+$.

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
> \begin{align*}
> &\text{begin}\\
> &\qquad\text{successo}:=true\\
> &\qquad \text{for every }X\to Y\in F\\
> &\qquad\text{do}\\
> &\qquad \text{begin}\\
> &\qquad\qquad\text{calcola } X^+\\
> &\qquad\qquad \text{if }Y\not\subset X^+_{G} \text{ then successo}:=false\\
> &\qquad\text{end} \\
> &\text{end}
> \end{align*}
> $$
>
>- se $Y\not\subset X^+_{G}$, allora $X\to Y \not\in G^A$ per il lemma, ovvero $X\to Y\not\in G^+$ per il Teorema
> 

basta fare i controlli solo per le dipendenze "a cavallo" - quelle che hanno sia determinante che dipendente in una decomposizione sono rispettate per forza

Nasce un problema: come calcoliamo $X^+_{G}$? Potremmo usare l'[[8 - chiusura di un insieme di attributi#come calcolare $X +$|algoritmo]] per il calcolo della chiusura di un insieme di attributi, ma dovremmo prima calcolare $G$, e quindi $F^+$, il che richiederebbe tempo esponenziale.

Per questo, esiste un algoritmo:
### calcolo della chiusura di X rispetto a G a partire da F

- **input** - uno schema $R$, un insieme $F$ di dipendenze funzionali su $R$, una decomposizione $\rho=\{ R_{1},R_{2},\dots,R_{k} \}$, un sottoinsieme $X$ di $R$.
- **output** - la chiusura di $X$ rispetto a $G=\cup_{i=1}^k\pi_{Ri}(F)$ 

$$
\begin{align*}
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
\end{align*}
$$

- partendo da un sottoinsieme di attributi $X$ di $R$, per prima cosa definiamo $Z$ come $X$ stesso per riflessività.
- dopodiché, ad ogni iterazione:
	$$S:=S\cup(Z\cap R_{i})^+_{F}\cap R_{i}$$fa: 
	- prima l'interzezione tra $Z$ e $R_i$, per considerare *solo gli elementi di $Z$ che riguardano quello specifico sottoinsieme*
	- poi la chiusura di quell'intersezione rispetto ad $F$, per trovare tutti gli attributi che ci interessano (tutti quelli determinati da dipendenze in $F^+$)
	- dopodiché l'intersezione con $R_i$, perché dobbiamo *tenere solo gli attributi che sono effettivamente in $R_i$* (per la questione dipendenze con det e dip in $R_i$)
	- e infine l'unione con l'accumulatore $S$, dove salviamo questo passo fatto per *tutti i sottoinsiemi $R_i$*
		- nota: ad ogni iterazione (prima dell'unione con $S$), potremo ottenere massimo $R_i$ stesso (per l'intersezione con $R_i$)
	- ho trovato quindi la chiusura rispetto a ogni singolo $R_{i}$, e quindi rispetto a $G$
	- quindi, avremo **gli attributi che dipendono funzionalmente da $X$, anche se appartengono a sottoschemi in cui $X$ non è incluso** - perché dipendono da attributi che si trovano nello stesso sottoschema di $X$ e dipendono da $X$, e anche in altri sottoschemi

>[!example]- esempio inventato del passo cruciale
>$R=(A,\,B,\,C,\,D,\,E,\,H)$
>- $R_{1}=(A,\,B),\;R_{2}=(C,\,D),\; R_{3}=(E,\,H)$
>
>cerchiamo $(AE)_{G}^+$
>- $Z=AE$
>- il passo prima dell'unione con $S$:
>	- $Z\cap R_{1}=A$
>	- trovo $A_{F}^+$
>	- $A^+_{F}\cap R_{1}\subseteq AB$
>- poi aggiungo a $S$

<small>(anche qui il latex dell'algoritmo rubato a [flavio](https://github.com/thegeek-sys/Vault/blob/main/Class/Basi%20di%20dati/Decomposizioni%20che%20preservano%20le%20dipendenze.md), che si diverte a fare queste cose)</small>

>[!note] dimostrazione
>dimostrare che l'algoritmo funziona significa mostrare che, alla fine dell'algoritmo, $Z$ conterrà tutta e sola la chiusura di $X$ rispetto a $G$.
>Quindi, che $Z^f\subseteq X^+_{G}\land Z^f\supseteq X^+_{G}$.
>
>Dimostriamo solo $Z^f\subseteq X^+_{G}$.
>>ricordiamo:
>>- $G=\cup_{i=1}^k\pi_{R_{i}}(F)$, con $\pi_{R_{i}(F)}=\{ X\to Y\mid X\to Y\in F^+\land XY\subseteq R_{i} \}$ 
>>- $S:=S\cup(Z\cap R_{i})^+_{F}\cap R_{i}$ (passo fondamentale dell'algoritmo)
>
>Si dimostra per induzione sui $i$ ($\forall i,\,Z^i\subseteq X^+_{G}$)
>
>- **caso base** ($i=0$): $Z^0=X$, e $X\subseteq X^+$, quindi $Z^0\subseteq X^+_{G}$
>- **ipotesi induttiva**: $Z^{i-1}\subseteq X^+_{G}$
>
>**passo induttivo**:
>Sia $A\in Z^i-Z^{i-1}$ (aggiunto all'ultimo passo).
>Se $A$ è stato aggiunto, vuol dire che deve esistere un sottoschema $R_{j}$ della decomposizione tale che: $A\in(Z^{i-1}\cap R_{j})^+_{F}\cap R_{j}$, ovvero $A\in(Z^{i-1}\cap R_{j})^+_{F}\land A\in R_{j}$.
>
>Abbiamo quindi: 
>- $(Z^{i-1}\cap R_{j})\to A\in F^A=F^+$ (per il *lemma 1* e teorema $F^+=F^A$).
>
>Sappiamo che $A\in R_{j}$, ma anche $(Z^{i-1}\cap R_{j})\subseteq R_{j}$.
>Notiamo quindi che la dipendenza $(Z^{i-1}\cap R_{j})\to A$ ha sia determinante che dipendente in un sottoschema $R_{j}$, e quindi, per definizione di $\pi_{R_{i}(F)}=\{ X\to Y\in F^+ :XY\subseteq R_{i}\}$, appartiene a $\pi_{R_{j}}(F)$ e, per costruzione di $G=\bigcup_{i=0}^n\pi_{R_{i}}(F)$, appartiene a $G$.
>- quindi $(Z^{i-1}\cap R_{j})\to A\subseteq G\subseteq G^+=G^A$
>
>In più, $(Z^{i-1}\cap R_{j})\subseteq Z^{i-1}$, e, per ipotesi induttiva $Z^{i-1}\subseteq X^+_{G}$.
>Quindi si ha $(Z^{i-1}\cap R_{j})\subseteq X^+_{G}$ e, per il *lemma 1*, $X\to(Z^{i-1}\cap R_{j})\in G^A$.
>Per transitività, da $X\to(Z^{i-1}\cap R_{j}),\; (Z^{i-1}\cap R_{j})\to A\in G^A$, si ha $X\to A\in G^A$, cioè (*l.1*) $A\in X^+_{G}$.
>
>> abbiamo quindi dimostrato che $A\in Z^i\implies A\in X^+_{G}$, ovvero $Z^i\subseteq X^+_{G}\;\; \forall i$