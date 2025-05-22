---
created: 2025-04-30T17:16
updated: 2025-05-22T19:33
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
	- i simboli di funzione di arità 0 sono detti simboli di *costante*
	- (essenzialmente) i simboli di funzione ritornano valori che possono essere oggetti del dominio

>[!example] esempi
>- $\text{zero/0}$ è un simbolo di costante che rappresenta il numero naturale 0
>- $\text{succ/1}$ ⟶ $\text{succ(x)}$ è il numero naturale $x+1$
>- $\text{padre/1}$ ⟶ $\text{padre(x)}$ è il padre dell'individuo $\text{x}$

- un insieme $P$ di **simboli di predicato**, ognuno associato al suo numero di argomenti, detto *arità*
	- i simboli di predicato di arità 0 vengono denominati *lettere proposizionali* (richiamo alla logica proposizonale)
	- (essenzialmente) i simboli di predicato assumono un valore di verità in base all'interpretazione

>[!example] esempi
>- $\text{doppio/2}$ ⟶ $\text{doppio(x, y)}$: il numero naturale $\text{y}$ è il doppio del numero naturale $\text{x}$
>- $\text{uomo/1}$  ⟶ $\text{uomo(x)}$: l'individuo $\text{x}$ è un uomo

- i **connettivi logici** $\neg,\,\land,\lor,\,\implies,\,\iff$
- i **quantificatori** $\forall,\,\exists$ (quantificatore universale e quantificatore esistenziale)
- i **simboli speciali**: parentesi "(", ")" e virgola ","

>[!tip] assunzioni/convenzioni
>- si assume che $P$ contenga il predicato di arità 2 "$=$" (uguaglianza)
>- per riferirsi a un simbolo di funzione $f$ o di predicato $p$ di arità $k$, si scrive $f/k$ e $p / k$

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
> [!summary] nella logica proposizionale
> La semantica della logica proposizionale è formata da formule atomiche date dalle lettere proposizionali, un'interpretazione che assegna un valore di verità ad ogni lettera proposizionale, e una funzione di valutazione predefinita che calcola la verità di una formula rispetto a un'interpretazione delle sue lettere.
> 
> Senza fare riferimento a particolari interpretazioni, si può estendere il significato di ogni formula proposizionale categorizzandola come:
> - **soddisfacibile** ⟶ esiste una interpretazione che è suo modello
> - **valida** ⟶ ogni interpretazione è suo modello
> - **insoddisfacibile** ⟶ nessuna interpretazione è suo modello

Nella logica di primo ordine, si segue lo stesso itinerario concettuale:
1) si definisce la nozione di **interpretazione** (valutazione delle formule atomiche)
2) si definisce come viene valutata una formula data una particolare interpretazione
3) si stabilisce il significato di ogni formula senza riferimento a particolari interpretazioni

Poiché ci sono due livelli sintattici (termini e formule), ci sono due nozioni di valutazione:
- la **valutazione dei termini**
	- formata da valutazione dei termini atomici - pre-interpretazione (valutazione dei simboli di funzione) e assegnamento di variabili (valutazione delle variabili) - e valutazione dei termini "complessi" a partire da quelli atomici
- la **valutazione delle formule**
	- formata dall'interpretazione delle formule atomiche e dalla valutazione delle formule "complesse" a partire da quelle atomiche

#### interpretazione



## FOL e UML
- simboli di predicato sono definiti dai nomi dei moduli e costrutti dell'UML
- le funzioni sono definite dalle operazioni necessarie per operare sui valori dei domini

- **ogni classe** definisce il simbolo di predicto unario `C/1` ⟶ le istanze di C hanno $C(x)=\text{true}$
- **ogni dominio** definisce il simbolo `dom/1`(es. Intero/1 true se intero)
	- ogni *dominio specializzato* definisce due simboli:
	- `dom` e `dom_spec`
	- es. Intero/1 e Intero>=0/1 (devono essere entrambi veri)\
	- ogni *dominio composto* definisce:
	- un simbolo unario `dom/1`
	- un simbolo di predicato unario per ogni dominio di ogni campo
	- un simbolo di predicato binario per ogni campo
- **ogni attributo di una classe** definisce il simbolo binario `attr/2` in cui i valori dell'attributo attr per l'istanza c di C sono rappresentati dagli elementi $v$ tali che $attr(c,v)=\text{true}$
- **ogni associazione** tra C1 e C2 definisce il simbolo binario `assoc/2` le coppie (ruolo1: c1, ruolo2: c2) del dominio tali che $assoc(c1, c2)=true$
	- ORDINE DEGLI ARGOMENTI DEFINITO DALL'ORDINE LESSICOGRAFICO DEI NOMI DEI RUOLI
- **ogni attributo di una associazione** definisce il simbolo di predicato ternario `attr/3` (c1, c2, v) = true se v valore....
- **ogni operazione** avente n argomenti definisce un simbolo di predicato (n+2)-ario (classe, argomenti..., valore di ritorno)
	- nel caso dell'overloading, in logica dobbiamo cambiare il nome di una delle due operazioni (es. op_classe1 e op_classe2)

Estendiamo la logica con
- relazioni matematiche
- somme tra date