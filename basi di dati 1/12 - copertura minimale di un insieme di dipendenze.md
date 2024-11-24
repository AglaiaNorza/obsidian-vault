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
>- per ogni dipendenza funzionale in $G$, la *parte destra è un singleton* <small>(ogni attributo nella parte destra è non ridondante)</small>
>- per nessuna dipendenza funzionale $X\to A \in G$ esiste $X'\subset X$ tale che $G\equiv G-\{ X\to A \}\cup \{ X'\to A \}$ <small>(ogni attributo nella parte sinistra non è ridondante)</small>
>- per nessuna dipendenza funzionale $X\to A \in G$, $G\equiv G-\{ X\to A \}$  <small>(ogni dipendenza non è ridondante)</small>
