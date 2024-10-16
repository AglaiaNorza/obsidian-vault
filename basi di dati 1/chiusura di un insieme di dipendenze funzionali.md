---
sticker: lucide//arrow-left-right
---
(due insiemi che hanno la stessa chiusura avranno le stesse istanze legali)

$$ F \subseteq F+ = G+ \supseteq G $$
non vuol dire che F=G, a che i due hanno le stesse istanze legali (posso scambiarli).

### assiomi di Armstrong
Denotiamo come $F^A$ l'insieme di dipendenze funzionali definito nel modo seguente:
- $f\in F \implies f\in F^A$ 
- $Y \subseteq X \subseteq R \implies X\rightarrow Y \in F^A$ **assioma della riflessività**
- **assioma dell'aumento**
- **assioma della transitività**

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