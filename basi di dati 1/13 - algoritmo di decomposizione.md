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
>###### $\rho$ preserva $F$
>Sia $G=\bigcup_{i=1}^k\pi_{Ri}(F)$.
> 
>Poiché per ogni dipendenza funzionale $X\to A\in F$ si ha $XA\in \rho$, si ha che questa dipendenza di $F$ sarà sicuramente in $G$. 
>Quindi, $G\subseteq F$ e quindi $G^+\subseteq F^+$ (l'inclusione $G^+\subseteq F^+$ è banale, in quanto, per definizione, $G\subseteq F^+$)