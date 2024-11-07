bisogna formalizzare il concetto di *decomposizione che preserva un insieme di dipendenze funzionali*.

>[!info] definizione di decomposizione
>Sia $R$ uno schema di relazione. Una **decomposizione** di $R$ è una famiglia $\rho=\{ R_{1},R_{2},\dots R_{k}\}$ di sottoinsiemi di $R$ che ricopre $R$ - $\cup_{i=1}^kR_{i}=R$.
>- essenzialmente, decomporre $R$ significa definire dei sottoschemi che contengono ognuno un sottoinsieme degli attributi di $R$.

La proiezione di $F$ su un certo elemento $R_i$ contiene:
- le dipendenze di $F^+$la cui unione di determinante e determinato fa parte di $R_{i}$

(due insiemi di dipendenze si possono scambiare quando hanno la stessa chiusura) - una decomposizione preserva $F$ se la chiusura di $F$ è uguale alla chiusura dell'insieme $G$ = unione delle proiezioni di $F$ sui vari elementi della decomposizione.


>[!info] equivalenza tra due insiemi di dipendenze funzionali
>Siano $F$ e $G$ due insiemi di dipendenze funzionali. 
>$F$ e $G$ sono **equivalenti** $F\equiv G$ se $F^+=G^+$.
>- ovvero non sono uguali ma hanno la *stessa chiusura*.

### lemma 2
Siano $F$ e $G$ due insiemi di dipendenze funzionali. Se $F\subseteq G^+$ allora $F^+\subseteq G^+$ (in realtà è un $\iff$, ma l'altra implicazione è banale).

>[!note] dimostrazione
>(quindi in $G^A$, quindi può essere ottenuto da $G$ applicando gli assiomi di armstrong)
continuando ad applicare gli assiomi di armstrong ottengo $F^+$, e rimango sempre dentro $G$

> [!tip] utilità del lemma 2 per la mia dimostrazione
> Grazie al lemma 2, per verificare che $F^+=G^+$ mi basta verificare che $F$ è contenuto in $G+$ e che $G$ è contenuto in $F+$.

Grazie al **lemma 1** - mi basta verificare che $\forall X\to Y \in F,\, Y\subseteq X_{G^+}$ e che $\forall V\to W \in G,\, W\subseteq V^+_{F}$

>[!info] 
>Sia R uno schema di relazione e F un inisieme di dipendenze funzionali .......
>diciamo che $\rho\text{ preserva } F$ se


g contenuto in f+ superfluo perché g ha vari pezzi di f+ al suo interno (perché è l'unione delle proiezioni di F sulle varie decomposizioni, quindi le dipendenze di f+ che hanno entrambi determinante e determinato in una stessa decomposizione) - il problema sono le dipendenze di f "a cavallo"

ma l'algo di calcolare chiusura x rispetto a g va usato solo per quelle dipendenze "a cavallo"

l'algo a partire da F ricalca le definizioni di proiezioni di F.
Z iniz a X per riflessività.
accumulatore inizializzato al vuoto.

Ciclo sui sottoschemi - vado a verificare le proiezioni di F, prendo i pezzi della chiusura di X che sono imputabili a qualche sottoschema.