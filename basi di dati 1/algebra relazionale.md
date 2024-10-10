---
sticker: lucide//plus-square
---
h(la prima parte dello scritto comprende due query di algebra relazionale)

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

### unione
Consente di costruire una relazione contenente tutte le ennuple che appartengono ad almeno uno dei due operandi.
Si denota con il simbolo:
$$ r_{1} \cup r_{2} $$

>[!important] quando si può applicare l'unione
>le operazioni di unione può essere applicata solo a operandi *union compatible*, ovvero:
>- hanno **lo stesso numero di attributi**
>- gli attributi corrispondenti sono ordinatamente definiti sullo **stesso dominio** e hanno lo stesso significato

>[!example] esempio di unione
![[es-unione.png|250]] ![[es-unione-2.png|300]]

- spesso, per applicare un'unione, è necessario applicare prima un'altra operazione (es. usare una proiezione per filtrare gli attributi in più

>[!example] esempio incompatibile
>![[es-unione-3.png|450]] 
>qui non si può fare un'unione - gli amministrativi hanno un attributo in più.
>è necessario effettuare una proiezione su un sottoinsieme di attributi comuni:
>Personale =
>$$ \pi_{Nome, CodDoc, Dip} (Docenti) \cup \pi_{Nome, CodAmm, Dip} (Amministrativi) $$
>(la proiezione sui docenti non serve)

### differenza
Si applica a *operandi union compatible*. Consente di costruire una relazione contenente tutte le tuple che **appartengono al primo operando ma non al secondo**.
Si denota con:
$$ r_{1} - r_{2} $$

>[!example] esempio
>![[es-diff.png|255]] ![[es-diff-2.png|257]]

### intersezione
Si applica a *operandi union compatible*. Consente di costruire una relazione contenente tutte le tuple che appartengono **ad entrambi gli operandi**.
Si denota con:
$$ r_{1} \cap r_{2}$$

### prodotto cartesiano, ridenominazione
Consente di costruire una relazione contenente tutte le ennuple che si ottengono concatenando tutte le ennuple del primo operando con tutte le ennuple del secondo.
Si denota con:
$$ r_{1} \times r_{2} $$
- si usa quando le informazioni che occorrono a rispondere ad una query si trovano in relazioni diverse

per poter distinguere gli attributi con lo stesso nome nello schema possiamo usare l'operazione di **RIDENOMINAZIONE**, denotata con: 
$$ \rho_{CC\#<-C\#}(Ordine) $$
(C# diventa CC#)

>[!example] esempio
>![[es-cart.png|500]]
>
>con risultato: 
> 
>![[es-cart-2.png|500]]
>

AGGIUNGI ALTRI PEZZI SLIDE
### join naturale
Consente automaticamente di selezionare le tuple del prodotto cartesiano dei due operandi che soddisfano la condizione
$$ R_{1}.A_{1}=R_{2}.A_{1} \space\land\space ... \space\land R_{1}.A_{k}=R_{2}.A_{k} $$
vengono unite le tuple i cui attributi con lo stesso nome hanno lo stesso valore.

$$ r_{1} \bowtie \space r_{2} = \pi_{XY}(\sigma_{C}(r_{1}\times r_{2}))$$

Essenzialmente, le **colonne duplicate vengono eliminate automaticamente** e vengono unite solo le tuple con **stesso valore negli attributi con lo stesso nome**.

>[!tip] query più corretta
se ci sono duplicati e si fa una proiezione su un attributo con duplicati, questi vengono eliminati - conviene *aggiungere una chiave*

>[!warning] casi limite join naturale
>- le relazioni contengono attributi con lo stesso nome ma non esistono ennuple per tali attributi in entrambe le relazioni
>	- risultato: il *join è vuoto*
>- le relazioni non contengono attributi con lo stesso nome
>	- risultato: si degenera nel *prodotto cartesiano*
> - perché il join abbia senso, gli attributi con lo stesso nome devono anche avere lo stesso significato.

> [!example] esempio
> query: nomi e città dei clienti che hanno ordinato più di 100 pezzi per almeno un articolo con prezzo superiore a 2.
> - join naturale tra cliente e ordine: rimangono Nome, C#, Città, O#, A#, N-pezzi
> - join naturale con articolo: rimangono Nome, C#, Città, O#, A#, N-pezzi, Denom., Prezzo
> - 
> ![[es-query.png]]
> $$ \pi_{Nome, Città}(\sigma_{N-pezzi>100 \land Prezzo>2})((Cliente\bowtie Ordine)\bowtie Articolo) $$
> 
Se noi sappiamo che una selezione riguarda solo un attributo, possiamo anticipare una condizione:
es.  $$ \sigma_{N-pezzi>100}(Ordine)$$
e poi $$Cliente\bowtie \sigma_{N-pezzi>100}(Ordine)$$
ecc., fino ad arrivare a
$$ Cliente \bowtie \sigma$$

### θ join
![[es-thetajoin.png]]
perché l'unione tra queste tabelle abbia senso, bisogna stare attenti ai due C#: in artista, rappresenta il codice dell'artista ("Artista" in Quadro) mentre in Quadro rappresenta il codice del quadro.
Quindi, o bisognerebbe rinominare gli attributi così che Artista.C# == Quadro.Artista, o si può effettuare un **theta join**

Consente di selezionare le tuple del prodotto cartesiano dei due operandi che soddisfano una condizione del tipo:
$$A \theta B$$

dove:
- θ è un operatore di confronto (`∈{<, <=, >, >=, =}`)
- A è un attributo dello schema del primo operando
- B è un attributo dello schema del secondo operando
- `dom(A)=dom(B)`
Si denota con:
$$r_{1}\bowtie r_{2} = \sigma_{A\theta B}(r_{1}\times r_{2}$$

### join SQL-style
Serve quando si vogliono effettuare query che chiedono di confrontare campi di tuple della stessa relazione.
>[!example]
>![[es-joinsql.png|400]]
>(anche il capo è un impiegato - associazione riflessiva asimmetrica in questo caso)
> 1) creiamo una copia dell'istanza (assegnata a una variabile relazionale)
> 2) *theta join* - per associare i capi ai dipendenti corrispondenti, usiamo il theta join su `C# = Capo`
> 	![[es-joinsql2.png|300]]
> 3) ![[es-joinsql3.png|300]]

>[!Tip] come gestire gli attributi su un join SQL-style
>- si può fare finta che, nel join, gli attributi abbiano mantenuto il nome dell'istanza di provenienza (`ImpiegatiC.Capo e Impiegati.Capo`), ma non è ideale perché non funziona così
>- si possono rinominare tutti gli attributi (necessari) 

---
### problemi con quantificatori diversi
>[!tip] fino ad ora
>fino ad ora abbiamo visto query che implicavano condizioni equivalenti al *quantificatore esietenziale* `∃`
>- infatti, in qualunque posizione appaiano, la valutazione delle condizioni avviene in sequenza

Quando si cerca qualcosa che succede **sempre** o **mai**, non si può semplicemente eliminare con una selezione i casi necessari - per esempio, se cerco gli equipaggi che non hanno mai volato nel 2018, se escludo gli equipaggi con voli nel 2018, non posso sapere che gli stessi equipaggi non ricompariranno con un altro volo.

