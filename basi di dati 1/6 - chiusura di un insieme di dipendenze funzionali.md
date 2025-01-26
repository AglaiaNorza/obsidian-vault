[ quasi tutto da [appunti flavio](https://github.com/thegeek-sys/Vault) (grz)]
 
(due insiemi che hanno la stessa chiusura avranno le stesse istanze legali - perché la chiusura è l'insieme di dipendenze che viene soddisfatto da ogni istanza legale)

$$ F \subseteq F+ = G+ \supseteq G $$
non vuol dire che F=G, ma che i due hanno le stesse istanze legali (posso scambiarli).

### assiomi di Armstrong
Denotiamo come $F^A$ l'insieme di dipendenze funzionali definito nel modo seguente:
- $\text{se }f\in F \text{ allora }f\in F^A$ 
- se rispetta l'**assioma della riflessività**
- se rispetta l'**assioma dell'aumento**
- se rispetta l'**assioma della transitività**

Dimostreremo che $F^+=F^A$, ovvero che la chiusura di un insieme di dipendenze funzionali F ($F^+$) $può essere ottenuta a partire da F applicando ricorsivamente i tre assiomi di Armstrong.

#### assioma della riflessività
$$\text{se } Y \subseteq X \subseteq R \text{ allora } X\rightarrow Y \in F^A$$
> [!example] esempio
> $\text{Nome}\subseteq(\text{Nome, Cognome})$ 
> - ovviamente se due tuple hanno uguale la coppia $(\text{Nome, Cognome})$ allora sicuramente avranno uguale l’attributo $\text{Nome}$ (e $\text{Cognome}$), quindi 
> - $(\text{Nome, Cognome}) \rightarrow \text{Nome}$ viene sempre soddisfatta

#### assioma dell'aumento
$$\text{se } X \rightarrow Y \in F^A \text{ allora } XZ \rightarrow YZ \in F^A \,\,\, \forall Z \subseteq R $$

>[!example] esempio
>- $\text{CodFiscale}\rightarrow\text{Cognome}$ è soddisfatta quando, se due tuple hanno $\text{CodFiscale}$ uguale, allora hanno anche $\text{Cognome}$ uguale.
>- Se aggiungo l’attributo $\text{Indirizzo}$, avrò che se due tuple sono uguali su $(\text{CodFiscale, Indirizzo})$ lo devono essere anche su $(\text{Cognome, Indirizzo})$
>- Quindi se viene soddisfatta $\text{CodFiscale}\rightarrow\text{Cognome}$ viene soddisfatta anche $\text{CodFiscale, Indirizzo}\rightarrow\text{Cognome, Indirizzo}$

#### assioma della transitività
$$\text{se} X\rightarrow Y \in F^A \text{ e } Y\rightarrow Z \in F^A \text{ allora } X\to Z \in F^A$$

>[!example] esempio
> - $\text{Matricola}\rightarrow\text{CodFiscale}$ è soddisfatta quando, se due tuple hanno $\text{Matricola}$ uguale, allora hanno anche $\text{CodFiscale}$ uguale.
>- $\text{CodFiscale}\rightarrow\text{Cognome}$ è soddisfatta quando, se due tuple hanno $\text{CodFiscale}$ uguale, allora hanno anche $\text{Cognome}$ uguale.
> - Allora se entrambe le dipendenze sono soddisfatte, e due tuple hanno $\text{Matricola}$ uguale, allora hanno anche $\text{CodFiscale}$ uguale, ma questo implica che hanno anche $\text{Cognome}$ uguale.
> - Quindi se entrambe le dipendenze sono soddisfatte, ogni volta che due tuple hanno $\text{Matricola}$ uguale avranno anche $\text{Cognome}$ uguale, e quindi viene soddisfatta anche $\text{Matricola}\rightarrow\text{Cognome}$
>   
>   ($\text{Matricola}\to \text{CodFiscale}\to \text{Cognome}$)

### conseguenze degli assiomi di Armstrong
Ci sono altre tre regole che producono elementi di $F^A$.

#### regola dell'unione
$$
\text{se } X\to Y \in F^A \text{ e } X\to Z \in F^A \text{ allora } X \to YZ \in F^A
$$
>[!example] esempio
>- Se $\text{CF}\to\text{Nome}$
>- e $\text{(Nome, Cognome)}\to\text{(Nome, Padre)}$
>- allora $\text{(CF, Cognome)}\to\text{(Nome, {Padre})}$

>[!Note] dimostrazione
>- Se $X\rightarrow Y \in F^A$, per l’assioma dell’aumento si ha $X\rightarrow XY \in F^A$ (sono insiemi, $\text{XX=X}$)
>- Analogamente se $X\rightarrow Z \in F^A$, per l’assioma dell’aumento si ha $XY \rightarrow YZ \in F^A$
>- Quindi poiché $X\rightarrow XY \in F^A$ e $XY \rightarrow YZ \in F^A$, per l’assioma della transitività si ha $X\rightarrow YZ \in F^A$

#### regola della decomposizione
$$ \text{se }X \rightarrow Y \in F^A\text{ e }Z \subseteq Y\text{ allora }X\rightarrow Z \in F^A $$
$$\text{(X}\to\text{sottoinsiemi di Y)}$$
>[!example] esempio
>- Se $\text{CF}\to\text{(Nome, Cognome)}$
>- (chiaramente $\text{Nome}\subseteq\text{(Nome, Cognome)}$)
>- allora possiamo dedurre $\text{CF}\to\text{Nome}\in F^A$

>[!note] dimostrazione
>- Se $Z \subseteq Y$, per l’assioma della riflessività, si ha $Y\to Z\in F^A$
>- Quindi poiché $X\to Y\in F^A$ e $Y\to Z\in F^A$, per l’assioma della transitività si ha $X\to Z\in F^A$

#### regola della pseudotransitività
$$\text{se }X \rightarrow Y \in F^A\text{ e }WY \rightarrow Z \in F^A\text{ allora }WX \rightarrow Z \in F^A$$
>[!example] esempio
>- Se $\text{ID}\to\text{Studente}$
>- e $\text{(Corso, Studente)}\to\text{Voto}$
>- allora $\text{(Corso, ID)}\to\text{Voto}$

>[!note] dimostrazione
>- Se $X\to Y\in F^A$, per l’assioma dell’aumento si ha $WX\to WY\in F^A$
>- Quindi poiché $WX\to WY\in F^A$ e $WY\to Z\in F^A$, per l’assioma della transitività si ha $WX\to Z\in F^A$

#### osservazione
Osserviamo che:
- per la regola dell’**unione**, se $X\to A_{i}\in F^A$, $i=1,\, \dots,\,n$ allora $X\to A_{1},\,\dots,\,A_{i}\,\dots\,A_{n}\in F^A$
- per la regola della  
### chiusura di un insieme di attributi
Sia R uno schema di relazione, F un insieme di dipendenze funzionali su R, e X un sottoinsieme di R.
La **chiusura di X rispetto a F**, denotata con $X_{F}^+$ (o $X^+$), è definita come:
$$X_{F}^+ = \{ A|X\rightarrow A\in F^A\}$$
- essenzialmente, fanno parte della chiusura di un insieme di attributi X tutti quelli che sono **determinati funzionalmente da X** eventualmente applicando gli assiomi di Armstrong.
- banalmente:
$$X\subseteq X_{F}^+$$

>[!example] esempio
>- $\text{CF}\rightarrow\text{COMUNE}$
>- $\text{COMUNE}\rightarrow\text{PROVINCIA}$
>
>$\text{CF}\rightarrow\text{COMUNE}$ è diretta, mentre $\text{CF}\rightarrow\text{PROVINCIA}$ è indiretta
>$$
>\text{CF}^+_{F}=\{\text{COMUNE, PROVINCIA, CF}\}
>$$

#### determinare la chiave di una relazione
La chiusura di un insieme di attributi ci può essere utile per determinare le chiavi di una relazione.

>[!example] esempio
>- $\text{Auto(MODELLO, MARCA, CILINDRATA, COLORE)}$
>- $F=\{\text{MODELLO} \rightarrow \text{MARCA, MODELLO }\rightarrow\text{COLORE}\}$
>
>Le chiusure sono:
>- $(\text{MODELLO})^+_{F}=\{\text{MODELLO, MARCA, COLORE}\}$
>- $(\text{MARCA})^+_{F}=\{\text{MARCA}\}$
>- $(\text{CILINDRATA})^+_{F}=\{\text{CILINDRATA}\}$
>- $(\text{COLORE})^+_{F}=\{\text{COLORE}\}$
>
>Il che ci fa capire che:
>$$\text{chiave}=\text{MODELLO, CILINDRATA}$$
>(modello e cilindrata, insieme, determinano tutti gli altri)

---
### lemma 1
Siano $R$ uno schema di relazione ed $F$ un insieme di dipendenze funzionali su $R$.
Si ha:
$$X \to Y \in F^A \iff Y \subseteq X^+$$
>[!inote] dimostrazione
>Sia $Y=A_{1}, A_{2}, \dots, A_{n}$
>
>- (dimostro $X \to Y \in F^A \impliedby Y \subseteq X^+$)
>
>Poiché $Y \subseteq X^+$, per ogni $i$, $i=1,\, \dots,\, n$ si ha che $X\rightarrow A_{i} \in F^A$. Pertanto per la regola dell’unione, $X\rightarrow Y \in F^A$
>
>- (dimostro $X \to Y \in F^A \implies Y \subseteq X^+$)
>
>Poiché $X\rightarrow Y \in F^A$, per la regola della decomposizione si ha che, per ogni $i$, $i=1, \dots, n$, $X \rightarrow A_{i} \in F^A$, cioè $A_{i} \in X^+$ per ogni $i, i=1,\, \dots,\, n$, e, quindi, $Y \subseteq X^+$
>$\begin{flalign}&& \square\end{flalign}$


### teorema: $F^+=F^A$

Siano $R$ uno schema di relazione ed $F$ un insieme di dipendenze funzionali su $R$.
Si ha: $$F^+=F^A$$
#### dimostrazione
##### $F^A\subseteq F^+$

Sia $X \to Y \in F^A$. Dimostriamo che $X \to Y \in F^+$ per induzione su $i$ applicazioni di uno degli assiomi di Armstrong.

**caso base**: ($i=0$): $X\to Y\in F\implies X\to Y\in F^+,,,, F\subseteq F^+$
 - (non abbiamo applicato nessun assioma di Armstrong: $X\to Y$ è in $F$ quindi banalmente è in $F^+$)

**ipotesi induttiva** ($i>0$): $X\to Y\in F^A\implies X\to Y\in F^+\implies X\to Y$ è soddisfatto da ogni istanza legale
- (ogni dipendenza in $F^A$ ottenuta applicando fino a $i-1$ assiomi di Armstrong è in $F^+$)

**passo induttivo**: consideriamo $i$: $X\to Y\in F^A$ ottenuto in $i$ passi. 
Dobbiamo dimostrare che appartiene anch'esso a $F^+$

Ci sono *tre casi* (tre assiomi di Armstrong che potremmo aver applicato all'$i+1$-esimo passo per ottenere $X\to Y$):

###### 1: riflessività

Ho ottenuto $X\to Y$ perché $Y\subseteq X$.  

In questo caso, $\forall r\text{ legale}, \;t_{1}[x]=t_{2}[x]\land Y\subseteq X\implies t_{1}[y]=t_{2}[y]$.

> (supponiamo che abbiano $X$ uguale: se hanno $X$ uguale e $Y$ è un sottoinsieme di $X$, logicamente anche $Y$ sarà uguale)

###### 2: aumento
Ho ottenuto $X\to Y$ per aumento su $V\to W \in F^A$.
Quindi $V\to W \in F^+$ è stata ottenuta in massimo $i-1$ passi e appartiene a $F^+$ per ipotesi induttiva.

Ci troviamo quindi nel caso in cui $X=VZ$ e $Y=WZ$ per qualche $Z\subseteq R$.

Sia $r$ un'istanza legale e siano $t_{1},\,t_{2}$ due tuple di $r$ tali che $t_{1}[X]=t_{2}[X]$.
- visto che $X=VZ$ e $Y=WZ$, si ha che $t_{1}[V]=t_{2}[V]$ e $t_{1}[Z]=t_{2}[Z]$

Per ipotesi induttiva ($V\to W \in F^+$):
- da $t_{1}[V]=t_{2}[V]$ segue $t_{1}[W]=t_{2}[W]$
- da $t_{1}[W]=t_{2}[W]\land t_{1}[Z]=t_{2}[Z]$ segue $t_{1}[Y]=t_{2}[Y]$ (perché $Y=WZ$)

###### 3: transitività
Ho ottenuto $X\to Y$ per transitività da $X\to Z$ e $Z\to Y$ in $F^A$.
- le due dipendenze sono state ottenute in massimo $i-1$ e appartengono a $F^+$ per ipotesi induttiva

Sia $r$ un'istanza legale di $R$ e siano $t_{1},\,t_{2}$ tali che $t_{1}[X]=t_{2}[X]$.
Per ipotesi induttiva, da $t_{1}[X]=t_{2}[X]$ segue $t_{1}[Z]=t_{2}[Z]$, da cui, sempre per ipotesi induttiva, segue $t_{1}[Y]=t_{2}[Y]$.

##### $F^+\subseteq F^A$
Supponiamo per assurdo che esita una dipendenza funzionale $X\to Y\in F^+$ tale che $X\to Y\notin F^A$.

Consideriamo la seguente istanza legale:

![[dimFAF+istanza.png|center|500]]

