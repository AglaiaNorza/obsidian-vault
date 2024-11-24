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

