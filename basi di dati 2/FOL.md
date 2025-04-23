---
created: 2025-04-23T20:07
updated: 2025-04-23T20:26
---
Una **logica** è una famiglia di linguaggi formali per rappresentare informazioni e derivare conseguenze.

Ogni logica è definita da:
- **sintassi** 
- **semantica**

>[!info] modello
> Dato un mondo $m$ e una formula $\varphi$, si ha  $m \vDash \varphi \iff \varphi$ è vera nel mondo $m$.
> 
> In questo caso, $m$ si dice **modello** di $\varphi$
> >[!summary] (concetto di conseguenza logica)
>> - (conseguenza logica: $\Gamma \vDash m$  significa che, in ogni interpretazione in cui tutte le formule di $\Gamma$ sono vere, anche $\varphi$ è vera)

### sintassi
La **sintassi** di una logica considera il linguaggio come l’insieme delle sequenze finite di simboli ammesse dal linguaggio (*formule*), dove ogni simbolo appartiene ad un insieme prefissato (*alfabeto*). 
- definisce quindi la *struttura delle formule*

Occorre quindi stabilire quali simboli appartengono al suo alfabeto e quali formule compongono il linguaggio.


### semantica
la **semantica** di una logica definisce il significato di ogni formula della logica, ovvero la sua *verità* nei diversi mondi possibili.