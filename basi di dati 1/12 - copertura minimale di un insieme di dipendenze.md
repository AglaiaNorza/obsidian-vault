bisogna affrontare il problema di come ottenere una decomposizone che soddisfi le nostre condizioni.

>[!question] è sempre possibile ottenerla?
>sì.
>dato uno schema $R$ su cui è definito un insieme di dipendenze funzionali $F$, è **sempre possibile** decomporlo in modo da ottenere che:
>- ognin sottoschema è *3NF*
>- la decomposizione *preserva le dipendenze* funzionali
>- è possibile *ricostruire ogni istanza legale* dello schema originale tramite join naturale

>[!warning] attenzione
>- la decomposizione che si ottiene dall'algoritmo non è l'unica possibile che soddisfi le condizioni richieste
>- lo stesso algoritmo, a seconda dell'input di partenza, può fornire risultati diversi ma tutti corretti
>- potrebbe essere possibile che una decomposizione non sia stata generata dall'algoritmo

### copertura minimale
- ci serve introdurre il concetto di **copertura minimale**, che servirà da input all'algoritmo di decomposizione 
- dato un insieme di dipendenze funzionali $F$, possono esserci *più coperture minimali equivalenti* (cioè con la stessa chiusura, uguale a quella di $F$).

>[!info] definizione
>Sia $F$ un insieme di dipendenze funzionali.
>Una **copertura minimale** di $F$ è un insieme $G$ di dipendenze funzionali *equivalente a $F$* tale che:
>- per ogni dipendenza funzionale in $G$, la *parte destra è un singleton* - <small>(ogni attributo nella parte destra è non ridondante)</small>
>- per nessuna dipendenza funzionale $X\to A \in G$ esiste $X'\subset X$ tale che $G\equiv (G-\{ X\to A \})\cup \{ X'\to A \}$ - <small>(ogni attributo nella parte sinistra non è ridondante) (quindi, se elimino la dipendenza $X \to A$, non "recupero" ciò che essa determina attraverso $X' \to A$)</small>
>- per nessuna dipendenza funzionale $X\to A \in G$, $G\equiv G-\{ X\to A \}$  - <small>(ogni dipendenza non è ridondante)</small>

riformulato in modo più informale:
- i dipendenti devono essere singleton
- $AB\to C$ può trovarsi nella copertura minimale solo se nella chiusura di $A$ e di $B$ non si trova $C$ (in caso contrario viene sostituito da $A\to C$ o $B\to C$
- posso eliminare una dipendenza se è possibile ricostruirla in $F^+$ tramite altre dipendenze

### come si calcola
Per ogni insieme di dipendenze funzionali $F$ esiste una copertura minimale equivalente ad $F$ che si può ottenere in *tempo polinomiale* in tre passi:
1) usando la decomposizione, le parti destre delle dipendenze vengono ridotte a singleton
2) si rendono le parti sinistre non ridondanti:
	![[copertura-min-ragionamento.png|center]]
	ora, $G$ diventa il nuovo $F$ per le verifiche successive
3) $\forall X\to A$, devo verificare che $F\equiv F-\{ X\to A \}$ 
	- sappiamo che i due differiscono per una sola dipendenza, $X\to A$, dunque basta verificare che $X\to A\in G^+$, ovvero (per il lemma 1), se $A\in X^+_{G}$
		- **nota**: se $X\to A\in F$, ma non esiste $Y\to A\in F$ con $X\neq Y$, è *inutile provare ad eliminare* $X\to A$ (non potremmo più determinare funzionalmente $A$)

### esempi
>[!example]- esempio 1
>$$R = (A,\,B,\,C,\,D,\,E,\,H)$$
>$$F = \{ AB\to CD,\,C\to E,\,AB\to E,\,ABC\to D \}$$
>
>**passo 1**
>riduciamo le parti destre a singleton
>$$F = \{ AB\to C,\,AB\to D,\,C\to E,\,AB\to E,\,ABC\to D \}$$
>
>**passo 2**
>dobbiamo verificare se ci sono ridondanze nelle parti sinistre.
>- cominciamo da $AB\to C$, e verifichiamo se $A\to C\in F^+$, ovvero se $C\in A^+_{F}$
>	- non ci sono dipendenze che hanno a sinistra solo $A$, quindi $A^+_{F}=\{ A \}$.
>- la stessa cosa vale per $AB\to D$ e $AB\to E$.
>- proviamo a ridurre $ABC\to D$.
>	- nell'insieme di dipendenze esiste $AB\to D$, quindi possiamo eliminare $C$ ma anche tutta la dipendenza risultante, che sarebbe uguale a $AB\to D$.
>
>a fine passo abbiamo quindi
>$$G = \{ AB\to C,\,AB\to D,\,C\to E,\,AB\to E,\}$$
>che diventa il nostro $F$
>
>**passo 3**
>vediamo se il nostro nuovo $F$ contiene dipendenze ridondanti
>- come prima cosa notiamo che $C$ viene determinato solo da $AB$, e la stessa cosa vale per $D$.
>- proviamo a eliminare $C\to E$.
>	- la chiusura di $C$ per il nuovo insieme di prova $G=\{ AB\to C,\,AB\to D,\,AB\to E \}$ è $C^+_{G}=\{ C \}$, quindi la dipendenza deve rimanere
>- proviamo ad eliminare $AB\to E$. $AB^+_{G}= \{ A,\,B,\,C,\,D,\,E \}$ - $E$ compare, quindi possiamo eliminare la dipendenza $A\to E$ (perché otterremmo $E$ in un altro modo)
>
>quindi, la *copertura minimale* di $F$ è $G=\{ AB\to C,\,AB\to D,\,C\to E \}$

>[!example]- esempio 2
>$$F=\{ BC\to DE,\,C\to D,\,B\to D,\,E\to L,\,D\to A,\,BC\to AL \}$$
>
>**passo 1**
>$$F=\{ BC\to D,\,BC\to E,\,C\to D,\,B\to D,\,E\to L,\,D\to A,\,BC\to A,\,BC\to L \}$$
>
>**passo 2**
>- possiamo sicuramente eliminare $BC\to D$, perché in $F$ abbiamo $B\to D$
>- passiamo a $BC\to E$ - dobbiamo vedere se $E\in B^+_{F}$ o $E\in C^+_{F}$
>	- le chiusure sono: $B^+_{F}=\{ B,\,D,\,A \}$, e $C^+_{F}=\{ C,\,D,\,A \}$
>	- notiamo che avremmo potuto direttamente dire solo che $E$ è determinato funzionalmente solo da $BC$, quindi sappiamo che non sarà nella chiusura di nessun attributo
>- passiamo a $BC\to A$ - abbiamo già calcolato le chiusure di $B$ e $C$ (e $F$ non è cambiato, ma altrimenti sarebbe comunque un insieme equivalente), e $A$ si trova in entrambe
>>[!warning] attenzione
>>in questo caso, le dipendenze $B\to A$ e $C\to A$ non sono in $F$, quindi non possiamo semplicemente eliminare $BC\to A$ - dobbiamo sostituirla con una delle due
> - scegliamo quindi per esempio $B\to A$
> - abbiamo quindi: $$F=\{BC\to E,\,C\to D,\,B\to D,\,E\to L,\,D\to A,\,B\to A,\,BC\to L\}$$
> - continuiamo con $BC\to L$
> 	- abbiamo già calcolato le chiusure di $B$ e $C$, e in nessuna delle due è presente $L$, quindi non possiamo eliminare elementi a sinistra
> 
> **passo 3**
> - non possiamo toccare la dipendenza $BC\to E$ perché $E$ è determinato unicamente da quella dipendenza
> - proviamo con $C\to D$ -> la chiusura di $C$ è $\{ C \}$, quindi deve rimanere
> - proviamo con $B\to D$ -> $B^+_{G}=\{ B,\,A \}$, quindi deve rimanere
> - proviamo con $E\to L$ -> $E^+_{G}=\{ E \}$, quindi deve rimanere
> - proviamo con $D\to A$ -> $D^+_{G}=\{ D \}$, quindi deve rimanere
> - proviamo con $B\to A$ -> la chiusura di $B$ rispetto al nuovo schema è $\{B,\,D,\,A \}$ - $A$ compare, quindi la dipendenza può essere eliminata
>
>la *copertura minimale* di $F$ è quindi:
>$$G=\{ BC\to E,\,C\to D,\,B\to D,\,E\to L,\,D\to A \}$$