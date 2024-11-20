Se si decompone uno schema di relazione $R$, si vuole che la decomposizione ottenuta sia tale che che *ogni istanza legale* $r$ di $R$  sia *ricostruibile mediante join naturale* da un'istanza legale  $\{r_{1},\,r_{2},\,\dots,\,r_{k}\}$ dello schema decomposto $\{R_{1},\,R_{2},\dots ,\,R_{k}\}$.

>[!info] definizione
>Sia $R$ uno schema di relazione. 
>Una decomposizione $\rho=\{ R_{1},\,R_{2}, \dots,\,R_{k}\}$ di $R$ ha un *join senza perdita* se **per ogni istanza legale di $r$ si ha**:
>$$r=\pi_{R_{1}}(r)\bowtie\pi_{R_{2}}\bowtie\dots\bowtie\pi_{R_{k}}(r)$$

>[!tip] introduciamo $m_{p}(r)$
>definiamo $m_{\rho}(r)=\pi_{R_{1}}(r)\bowtie\pi_{R_{2}}\bowtie\dots\bowtie\pi_{R_{k}}(r)$ 
> 
>join naturale delle proiezioni dei sottoschemi su $r$ (che deve quindi essere uguale a $r$ stessa)

### teorema
Sia $R$ uno schema di relazioni e $\rho={R_{1},\,R_{2},\,\dots,\,R_{k}}$.
Per ogni istanza legale $r$ di $R$ e per il "suo" $m_{\rho}$ si ha:
1) $r\subseteq m_{\rho}(r)$ - non serve dimostrarlo perché $m_{\rho}(r)$ non potrà mai contenere istanze in meno, quindi al minimo è $=r$
2) $\pi_{R_{i}}(m_{\rho})=\pi_{R_{i}}(r)$ - perché nella proiezione i duplicati vengono collassati
3) $m_{\rho}(m_{\rho}(r))=m_{\rho}(r)$

### verifica
esiste un algoritmo che permette di verificare se una decomposizione data ha un join senza perdita in tempo polinomiale:

- **input**: uno schema di relazione $R$, un insieme $F$ di dipendenze funzionali su $R$, una decomposizione $\rho=\{ R_{1},\,R_{2},\,\dots,R_{3}  \}$ 
- **output**: decide se $\rho$ ha un join senza perdita

$$
\begin{align*}
&\mathbf{begin} \\
&\text{Costruisci una tabella }r\text{ nel modo seguente:} \\
&r\text{ ha } \#R\text{ colonne e }\#\rho \text{ righe} \\
&\text{all'incrocio dell'i-esima riga e della j-esima colonna metti} \\
&\text{il simbolo }a_{j}\text{ se l'attributo }A_{j}\in R_{i} \\
&\text{il simbolo }b_{ij}\text{ altrimenti} \\
&\mathbf{repeat} \\
&\mathbf{for\,\,every\,\, X\to Y\in F} \\
&\qquad\mathbf{do\,\,if} \text{ ci sono due tuple }t_{1}\text{ e }t_{2}\text{ in }r\text{ tali che }t_{1}[X]=t_{2}[X] \text{ e }t_{1}[Y]\neq t_{2}[Y] \\
&\qquad\qquad\mathbf{then\,\,for\,\,every\,\,attribute\,\,A_{j}\in Y} \\
&\qquad\qquad\qquad\mathbf{do\,\,if\,\,}t_{1}[A_{j}]='{a_{j}}' \\
&\qquad\qquad\qquad\qquad\mathbf{then\,\,}t_{2}[A_{j}]:=t_{1}[A_{j}] \\
&\qquad\qquad\qquad\qquad\mathbf{else\,\,}t_{1}[A_{j}]:=t_{2}[A_{j}] \\
&\mathbf{until\,\,}r\text{ ha una riga con tutte 'a' }\mathbf{or\,\,}r\text{ non è cambiato} \\
&\mathbf{if\,\,}r\text{ ha una riga con tutte 'a'} \\
&\qquad\mathbf{then\,\,}\rho \text{ ha un join senza perdita} \\
&\qquad\mathbf{else\,\,}\rho \text{ non ha un join senza perdita}
\end{align*}
$$

quando finisce l'algoritmo, o:
- sono arrivato alla fine e non posso più cambiare cose (è un'istanza legale)
- mi fermo in anticipo - le a non possono diventare b, e ho trovato una tupla di tutte a (so già che l'istanza diventerà legale alla fine dell'algoritmo, e posso fermarmi perché non ho perdite)

>[!summary]- spieghiamo meglio
>- costruiamo una tabella $r$ in modo da evere un numero di colonne pari al numero di attributi in $R$ e un numero di righe pari al numero di sottoschemi nella decomposizione $\rho$
>- nelle celle ad indice $i$ per le righe e $j$ per le colonne, inseriamo $a_{ij}$ se l'attributo della colonna $j$ appartiene al sottoschema della riga $i$ - altrimenti inseriamo $b_{ij}$
>- adesso, per ogni dipendenza $X\to Y \in F$, controlliamo se nella tabelle i sono tuple che non rispettano la dipendenza (ovvero $t_{1}[X]=t_{2}[X]$ e $t_{1}[Y]\neq t_{2}[Y]$) - le "facciamo diventare legali": se in una tupla è presente una $a$ nell'attributo $Y$, la propaghiamo a tutte le altre, altrimenti scegliamo un $b$ a piacere e lo propaghiamo su tutte le altre (due attributi sono uguali se hanno entrambi $a$ o una $b$ con lo stesso pedice)

#### esempio

dati
$R=(A,\,B,\,C,\,D)$ e
$F = \{  C\to D,\,AB \to E,\,D\to B \}$
dire se la decomposizione
$\rho=\{ AC,\,ADE,\,CDE,\,AD,\,B \}$
ha un join senza perdite

![[esempio-losslessjoin.png|center|500]]

prima iterazione:
![[llj-es1.png|center|500]]

in ordine rispetto alle dipendenze funzionali:
- $C\to D$: la prima e la terza riga coincidono su $C=a3$ - cambiamo $b14$ in $a4$ in modo che la dipendenza funzionale sia soddisfatta
- $AB\to E$ è già soddisfatta
- $D\to B$: nelle prime quattro righe, $D=a4$, quindi cambiamo $b22$, $b 32$, $b 42$ in $b 12$ 

seconda iterazione:
![[llj-es2.png|center|500]]

- $C\to D$ è già soddisfatta
- $AB\to E$: prima, seconda e quarta riga coincidono su $AB$, quindi cambiamo $b 15$ e $b 45$ in $a 5$ 
- $D\to B$ è già soddisfatta

terza iterazione (fine):
![[llj-es3.png|center|500]]

- non c'è più nulla da cambiare quindi l'algoritmo termina.

Bisogna verificare se c'è una tupla con tutte $a$ - non c'è, quindi il join *non è senza perdita*.

