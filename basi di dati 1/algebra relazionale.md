(la prima parte dello scritto comprende due query di algebra relazionale)

L'algebra relazionale è un *linguaggio formale* che ci permette di interrogare una base di dati relazionale. Consiste di:
- un insieme di **operatori** che possono essere applicati a una (unari) o due (binari) istanze di relazione, e forniscono come risultato:
- una nuova istanza di relazione (che si può salvare in una variabile)

L'algebra relazionale è un **linguaggio procedurale**

### proiezione
La proiezione consente di effettuare un taglio verticale su una relazione, ovvero di **selezionare solo alcune colonne**
Si denota con il pi greco:
$$\pi_{A_1, A_2, \ldots, A_K}(r)$$
- seleziona le colonne di r che corrispondono agli attributi A1, A2,...,AK

> [!example]
> ![[query1.png|400]]
>  N.B.: nell'algebra relazionale si seguono le regole insiemistiche, quindi nel risultato *non ci sono duplicati*
>  Se per esempio si volessero tenere i duplicati (es. per conservare i clienti omonimi), si può aggiungere una chiave alla query: il codice.

### selezione
Consente di effettuare un taglio orizzontale, ovvero di selezionare **solo le righe** che soddisfano una data condizione
Si denota con il sigma:
$$\sigma_{C}(r)$$
- seleziona le tuple di r che soddisfano la condizione C.

La condizione di selezione è un'espressione booleana composta (tramite AND, OR, NOT) in cui i termini semplici sono del tipo:
- `A θ B`, in cui A e B sono due *attributi con lo stesso dominio* e θ è un operatore di confronto
