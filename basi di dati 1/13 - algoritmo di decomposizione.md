Dato uno schema di relazione $R$ e un insieme di dipendenze funzionali $F$ su $R$, *esiste sempre* una decomposizione $\rho=\{ R_{1},\,R_{2},\,\,\dots,\,R_{k} \}$ tale che:
- $\forall i,\,i=1,\dots,k,\,\,\,R_{i}$ è in 3NF
- $\rho$ preserva $F$
- $\rho$ ha un join senza perdita

e tale decomposizione può essere calcolata in tempo polinomiale.

- ci interessa una qualunque copertura minimale di dipendenze funzionali definite su $R$ (se ce ne fossero varie, potremmo voler scegliere quella con meno dipendenze, ma non è tra i nostri scopi)
- quindi, come input dell'algoritmo, ci basta averne una qualunque

### algoritmo
- **input**: uno schema di relazione $R$ e un insieme $F$ di dipendenze su $R$ che sia una *copertura minimale*
- **output**: una decomposizone $\rho$ di $R$ che preserva $F$, di cui ogni schema è in 3NF

$$
\begin{align*}
&\mathbf{begin} \\
&S:=\varnothing \\
&\mathbf{for\,\,every} A\in R\text{ tale che }A\text{ non è coinvolto in nessuna dipendenza funzionale in F} \\
&\qquad\mathbf{do} \\
&\qquad S:=S\cup \{A\} \\
&\mathbf{if\,\,}S\neq \varnothing\mathbf{\,\,then} \\
&\qquad \mathbf{begin} \\
&\qquad R:=R-S \\
&\qquad \rho:=\rho \cup \{S\} \\
&\qquad \mathbf{end} \\
&\mathbf{if}\text{ esiste una dipendenza funzionale in }F\text{ che coinvolge tutti gli attributi in }R \\
&\qquad\mathbf{then\,\,}\rho:=\rho \cup \{R\} \\
&\mathbf{else} \\
&\qquad\mathbf{for\,\,every\,\,}X\to A \\
&\qquad\qquad\mathbf{do} \\
&\qquad\qquad \rho:=\rho \cup \{XA\} \\
&\mathbf{end}
\end{align*}
$$
<small> latex algo da [flavio](https://github.com/thegeek-sys/Vault/blob/main/Class/Basi%20di%20dati/Algoritmo%20di%20decomposizione.md)</small>

>[!summary] spiegazione
>- prendo gli attributi che non compaiono nelle dipendenze di $F$ e li metto in $S$
>- se ho aggiunto qualcosa a $S$:
>	- tolgo quello che ho aggiunto in $S$ da $R$
>	- lo metto in $\rho$
>- se esiste una dipendenza in $F$ che coinvolge tutti gli attributi in $R$ (in cui non ci sono più quelli che ho eventualmente tolto):
>	- metto in $\rho$ direttamente tutta $R$
>- else:
>	- metto in $\rho$ tutti gli attributi presenti nelle dipendenze di $F$

### teorema
Sia $R$ uno schema di relazione e $F$ un insieme di dipendenze funzionali su $R$ che è una copertura minimale.
L'algoritmo di decomposizione permette di calcolare in tempo polinomiale una decomposizione di $\rho$ tale che:
- ogni schema di relazione in $\rho$ è in 3NF
- $\rho$ preserva $F$

>[!note] dimostrazione
>###### $\rho$ preserva $F$ (ovvero $F^+=G^+$)
>Sia $G=\bigcup_{i=1}^k\pi_{Ri}(F)$.
> 
>Poiché per ogni dipendenza funzionale $X\to A\in F$ si ha $XA\in \rho$, si ha che tutte le dipendenze di $F$ saranno sicuramente in $G$. 
>Quindi, $F\subseteq G$ e quindi $F^+\subseteq G^+$.
>- (l'inclusione $G^+\subseteq F^+$ è banale, in quanto, per definizione, $G\subseteq F^+$)
>
>###### ogni schema di $\rho$ è in 3NF
>abbiamo tre diversi casi che si possono presentare:
>1) $S\in \rho$ --> ogni attributo in $S$ fa parte della chiave (gli attributi in $S$ sono quelli non coinvolti nelle dipendenze, quindi dovranno necessariamente essere nella chiave) e $S$ è in 3NF 
>2) $R\in \rho$ (ovvero esiste una dipendenza funzionale in $F$ che coinvolge tutti gli attributi in $R$) --> visto che $F$ è una copertura minimale, la dipendenza avrà forma $(R-A)\to A$.
>	Abbiamo quindi che $R-A$ è *superchiave* per $R$ (determina $A$ e $R-A$ per riflessività) - a noi interessano le chiavi e non le superchiavi, ma:
>	- non ci può essere un sottoinsieme di $R-A$ che determini tutto lo schema, perché partiamo da una copertura minimale (per definizione non ci può essere $Y\subset R-A$ tale che $Y\to A$, altrimenti avremmo ridotto $R-A$ a $Y$)
>	- quindi, a qualunque $Y\subset A$ manca determinare $A$, il che implica che $R-A$ *è chiave*
>	- infatti, prendiamo $Y\to B$ una qualsiasi dipendenza in $F$ - abbiamo due casi:
>		- $B=A$ --> $Y=R-A$ (è impossibile che ci siano due dipendenze con lo stesso dipendente visto che è una copertura minimale)
>		- $B\neq A$ --> $B\in R-A$ quindi, visto che $R-A$ è chiave, $B$ è primo
>4) $XA\in \rho$ --> non c'è un $R-A\to A$, ci sono diversi $X\to A$ - quindi, $X$ è superchiave per $\{ XA \}$, ed è anche *chiave* per il ragionamento di sopra (copertura minimale $\implies$ non esiste un $X'\subset X$ che determina $A$).
>	- prendiamo un qualunque $Y\to B\in F$ tale che $YB\subseteq XA$:
>		- $B=A$ --> $Y=X$ (per lo stesso ragionamento di prima - copertura minimale)
>		- $B\neq A$ --> $B\in X$  (è primo)

>[!info] (teorema) avere anche un join senza perdita
>Per avere anche un join senza perdita, se nessun sottoschema contiene una chiave, basta aggiungere un sottoschema che ne contenga una (una qualsiasi).
>- $\sigma=\rho\cup \{ K \}$ ha un join senza perdita

>[!question] è sempre possibile avere una decomposizione con schemi in 3NF, che preservi F e abbia un join senza perdita?
>sì! 
>abbiamo visto un algoritmo che, in tempo polinomiale, fornisce questa decomposizione

## domande orale
>[!question] possibili domande orale
>- dimostrazione $\rho$ preserva $F$ e ogni schema di $\rho$ è in 3NF