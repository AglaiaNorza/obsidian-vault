---
created: 2025-04-23T20:07
updated: 2025-04-27T11:05
---
Una **logica** è una famiglia di linguaggi formali per rappresentare informazioni e derivare conseguenze.

Ogni logica è definita da:
- **sintassi** ⟶ considera il linguaggio come l’insieme delle sequenze finite di simboli ammesse dal linguaggio (*formule*), dove ogni simbolo appartiene ad un insieme prefissato (*alfabeto*)
	- definisce quindi la struttura delle formule
- **semantica** ⟶ definisce il significato di ogni formula della logica, ovvero la sua *verità* nei diversi mondi possibili

>[!info] modello
> Dato un mondo $m$ e una formula $\varphi$, si ha  $m \vDash \varphi \iff \varphi$ è vera nel mondo $m$.
> 
> In questo caso, $m$ si dice **modello** di $\varphi$
> >[!summary] (concetto di conseguenza logica)
>> - (conseguenza logica: $\Gamma \vDash m$  significa che, in ogni interpretazione in cui tutte le formule di $\Gamma$ sono vere, anche $\varphi$ è vera)

## FOL: Logica di Primo Ordine
### alfabeto
L'**alfabeto** della logica di primo ordine è composto da:
- un insieme $V$ di **variabili**
- un insieme $F$ di **simboli di funzione**, ognuno associato al suo numero di argomenti, detto *arità*
	- (essenzialmente) i simboli di funzione ritornano valori che possono essere oggetti del dominio

>[!example] esempi
>- $\text{zero/0}$ è un simbolo di costante che rappresenta il numero naturale 0
>- $\text{succ/1}$ ⟶ $\text{succ(x)}$ è il numero naturale $x+1$
>- $\text{padre/1}$ ⟶ $\text{padre(x)}$ è il padre dell'individuo $\text{x}$

- un insieme $P$ di **simboli di predicato**, ognuno associato al suo numero di argomenti, detto *arità*
	- (essenzialmente) i simboli di predicato assumono un valore di verità in base all'interpretazione

>[!example] esempi
>- $\text{doppio/2}$ ⟶ $\text{doppio(x, y)}$: il numero naturale $\text{y}$ è il doppio del numero naturale $\text{x}$
>- $\text{uomo/1}$  ⟶ $\text{uomo(x)}$: l'individuo $\text{x}$ è un uomo

- i **connettivi logici** $\neg,\,\land,\lor,\,\implies,\,\iff$
- i **quantificatori** $\forall,\,\exists$ (quantificatore universale e quantificatore esistenziale)
- i **simboli speciali**: parentesi "(", ")" e virgola ","

>[!tip] assunzioni e convenzioni
>- si assume che $P$ contenga il predicato di arità 2 "$=$" (uguaglianza)
>- per riferirsi a un simbolo di funzione $f$ o di predicato $p$ di arità $k$, si scrive $f/k$ e $p / k$
>- i simboli di funzione di arità 0 vengono detti *simboli di costante*
>- i simboli di predicato di arità 0 vengono denominati *lettere proposizionali* (poiché sono quanto di più vicino alle lettere proposizionali della logica proposizonali)

### termini e formule
A partire dall'alfabeto, si può definire il linguaggio della logica di primo ordine. La sua definizione induttiva deve essere effettuata in due passi:
- si definisce un linguaggio intermedio dei **termini**
- si definisce il linguaggio delle **formule** utilizzando il linguaggio dei termini

>[!info] termini
>L'insieme dei **termini** è definito induttivamente così:
>- ogni *variabile* in $V$ è un termine
>- ogni simbolo di *costante* in $F$ è un termine
>- se $f$ è un simbolo di funzione di arità $n>0$ e $t_{1},\,\dots,\, t_{n}$ sono termini, allora anche $f(t_{1},\dots,\, t_{n})$ è un termine.
>
>>[!example] esempi
>>sia $F=\{\text{zero/0, succ/1, socrate/0, padre/1}\}$, e sia $V=\{ \text{MiaVariabile, X} \}$
>>
>>questi sono termini:
>>- $\text{zero}$
>>- $\text{MiaVariabile}$
>>- $\text{succ(zero)}$
>>- $\text{padre(succ(x))}$

>[!tip] formule
>L'insieme delle **formule** è definito induttivamente come segue:
>- se $p$ è un *simbolo di predicato* di arità $n$ e $t_{1},\,\dots t_{n}$ sono *termini*, allora $p(t_{1},\,\dots,\,t_{n})$ è una **formula** (detta "atomica").
>- se $\phi$ e $\psi$ sono formule, lo sono anche
>	- $(\phi),\,\,\neg \phi$
>	- $\phi \lor \psi,\;\;\phi \land \psi$
>	- $\phi \implies \psi,\;\; \phi \iff \psi$
>- se $\phi$ è una formula e $X$ è una variabile, allora anche $\forall X \;\phi$ e $\exists X\; \phi$ sono formule
>
>>[!example] esempi
>>siano  $F=\{ \text{zero/0, succ/1, socrate/0, padre/1} \}$ e $P=\{ \text{doppio/2, somma/3, uomo/1, mortale/1} \}$ e $V=\{ X,\,Y,\,I,\,J,\,K \}$
>>
>>queste sono formule:
>>- $\text{doppio(succ(zero), X)}$
>>- $\forall X\, \forall Y\text{ somma(X, X, Y)}\implies \text{doppio(X, Y)}$
>>- $\text{mortale(socrate)}$

### semantica
Nella logica proposizionale, la