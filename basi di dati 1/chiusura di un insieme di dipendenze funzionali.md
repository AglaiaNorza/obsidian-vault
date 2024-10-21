---
sticker: lucide//arrow-left-right
---
(due insiemi che hanno la stessa chiusura avranno le stesse istanze legali - perché la chiusura è l'insieme di dipendenze che viene soddisfatto da ogni istanza legale)

$$ F \subseteq F+ = G+ \supseteq G $$
non vuol dire che F=G, ma che i due hanno le stesse istanze legali (posso scambiarli).

### assiomi di Armstrong
Denotiamo come $F^A$ l'insieme di dipendenze funzionali definito nel modo seguente:
- $\text{se }f\in F \text{ allora }f\in F^A$ 
- **assioma della riflessività**:
$$\text{se } Y \subseteq X \subseteq R \text{ allora } X\rightarrow Y \in F^A$$
- **assioma dell'aumento**:
	$$\text{se } X \rightarrow Y \in F^A \text{ allora } XZ \rightarrow YZ \in F^A \,\,\, \forall Z \subseteq R $$
- **assioma della transitività**:
$$\text{se } X\rightarrow Y \in F^A \text{ e } Y\rightarrow Z \in F^A \text{ allora } X\to Z \in F^A$$

>[!example] esempio
>- CF -> COGNOME in F
>- istanza legale -> soddisfa anche CF -> cognome
>- T1.CF = T2.CF -> T1.COGNOME = T2.COGNOME
><br></br>
>- <CF, INDIRIZZO>. <COGNOME, INDIRIZZO>
>- T1.<CF, INDIRIZZO>=T2.<CF, INDIRIZZO>
>- T1.CF=T2.CF and T1.INDIRIZZO = T2.INDIRIZZO
>- (è un'istanza legale, quindi soddisfa CF-> COGNOME, quindi) T1.COGNOME = T2.COGNOME
>- ()P

altre tre regole che producono elementi di $F^A$

- **regola dell'unione** se $X\rightarrow Y\in F^A$ e $X\rightarrow Z \in F^A$, allora $X\rightarrow YZ \in F^A$ - **regola dell'unione**

- se $X\to Y \in F^A$ e $Z \subseteq Y$ allora $X\to Z \in F^A$ 

nome, cognome -> nome, padre
CF->nome
CF, cognome -> nome, padre

**dimostrazione**
Teorema:
sia F un insieme di dipendenze funzionali. Valgono le seguenti implicazioni:


!!! slide !!!!


### chiusura di un insieme di attributi
Sia R uno schema di relazione, F un insieme di dipendenze funzionali su R, e X un sottoinsieme di R.
La **chiusura di X rispetto a F**, denotata con $X_{F}^+$ (o $X^+$), è definita come:
$$X_{F}^+ = \{ A|X\rightarrow A\in F^A\}$$
- essenzialmente, fanno parte della chiusura di un insieme di attributi X tutti quelli che sono **determinati funzionalmente da X** eventualmente applicando gli assiomi di Armstrong.
- banalmente:
$$X\subseteq X_{F}^+$$

