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
>$$\large F=\bigcup_{i=1}^k\pi_{Ri}(F)$$
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

Grazie al [[6 - chiusura di un insieme di dipendenze funzionali#lemma 1|lemma 1]] - mi basta verificare che $\forall X\to Y \in F,\, Y\subseteq X_{G^+}$ e che $\forall V\to W \in G,\, W\subseteq V^+_{F}$

g contenuto in f+ superfluo perché g ha vari pezzi di f+ al suo interno (perché è l'unione delle proiezioni di F sulle varie decomposizioni, quindi le dipendenze di f+ che hanno entrambi determinante e determinato in una stessa decomposizione) - il problema sono le dipendenze di f "a cavallo"

ma l'algo di calcolare chiusura x rispetto a g va usato solo per quelle dipendenze "a cavallo"

l'algo a partire da F ricalca le definizioni di proiezioni di F.
Z iniz a X per riflessività.
accumulatore inizializzato al vuoto.

Ciclo sui sottoschemi - vado a verificare le proiezioni di F, prendo i pezzi della chiusura di X che sono imputabili a qualche sottoschema.