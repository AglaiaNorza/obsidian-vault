---
sticker: lucide//arrow-left-right
---
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

