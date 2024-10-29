Torniamo al nostro esempio di base di dati che contiene informazioni su studenti ed esami (soluzione "buona" trovata alla fine)

La base di dati consiste di quattro schemi di relazione:
- Studente (**Matr**, *CF*, Cogn, Nome, Data, Com)
- Corso (**C#**, Tit, Doc)
- Esame (**Matr, C#**, Data, Voto)
- Comune (**Com**, Prov)

#### considerazioni
>[!question] dipendenze funzionali su Studente
>- Studente
>	- $\text{Matr}\to\text{CF}$
>	- $\text{Matr}\to\text{Cogn}$
>	- $\text{Matr}\to\text{Nome}$
>	- $\text{Matr}\to\text{Data}$
>	- $\text{Matr}\to\text{Com}$
>
>quindi, un'istanza legale di Studente deve soddisfare:
>$$\text{Matr}\to\text{CF, Cogn, Nome, Data, Com}$$
>in realtà notiamo che anche CF determina tutte le altre cose:
>$$\text{CF}\to\text{Matr, Cogn, Nome, Data, Com}$$
>Quindi, sia $\text{Matr}$ che $\text{CF}$ sono **chiavi**

- possiamo notare che le istanze di Studente non devono soddisfare $\text{Cogn}\to\text{Nome}$

Con considerazioni analoghe possiamo concludere che le uniche dipendenze funzionali non banali che devono essere soddisfatte da un'istanza legale di Studente sono del tipo: $\text{K}\to\text{X}$ dove K **contiene una chiave** (Matr o CF)

(qui iniziamo a notare che le dipendenze devono tipicamente essere solo da una chiave o superchiave)

>[!question] dipendenze funzionali su esame
>- Esame
>
>uno studente può sostenere l'esame relativo ad un corso una sola volta, quindi per ogni esame esistono:
>- una sola data e un solo voto
>  
>  Quindi, ogni istanza legale di Esame deve soddisfare:
>  $$\text{(Matr, C\#)}\to\text{(Data, Voto)}$$
>  
>  Pertanto, $(Matr, C\#)$ è l'unica chiave per Esame.


### terza forma normale
Uno schema di relazione è 3NF se:
- le uniche dipendenze funzionali non banali che devono essere soddisfatte da ogni istanza legale sono del tipo:
$$\text{K}\to\text{X}$$
dove: 
- **K contiene una chiave** oppure
- **X è contenuto in una chiave**

Ma anche questa condizione deve ancora essere rifinita.

>[!info] definizione
>Dati uno schema di relazione R e un insieme di dipendenze funzionali F su R, R è in 3NF se:
>$$\forall X\to A\in F^+,\,A \not\in X$$
>- **A appartiene ad una chiave** (è *primo*) oppure
>- **X contiene una chiave** (è *superchiave*)
>
>
(Altra definizione: Ogni X->Y appartente a X è tale che X è superchiave e ogni attributo contenuto in Y è primo.)

>[!warning] attenzione
>- è sbagliato scrivere $\forall X\to A \in F$, perché A è singleton e dovremmo escludere tutte quelle del tipo $X \to AB$ (che potrebbero violare la 3NF) (invece, per $X\to AB$, $X \to A$ si trova in $F^+$)
>- è sbagliato anche dire $\forall X\to Y \in F$ (devo specificare che ogni attributo di Y è primo)
>- è importante non dimenticare il $A\not\in X$. Infatti, per riflessività, abbiamo sempre $X\to A$ in $F^A$ e quindi in $F^+$ anche quando A non è primo e X non è superchiave (quindi, nessuno schema sarebbe 3NF)

>[!example] esempio
>$$
>R=ABCD\,\,\,\,\, 
>{F=AB\to CD,\, AC\to BD, \,D\to BC}
>$$
>ha come chiavi:
>- $K_{1}=AB$
>- $K_{2}=AC$
>- $K_{3}=AD$ (per aumento su $D\to BC$, $AD\to ABC$)
>
>
AD -> BC è in F+ e ha come determinante non superchiave (D), BC non sono chiave insieme ma B è nella chiave AB, e C è nella chiave AC (ma non è in forma normale di Boyce Codd (boy's code per gli amici))

### dipendenze parziali e transitive
Siano R uno schema di relazione e F un insieme di dipendenze funzionali su R.
>[!info] dipendenza parziale
>$$X\to A \in F^+ \mid A\not\in X$$
>è una **dipendenza parziale** su R se A non è primo ed X è contenuto propriamente in una chiave di R.

>[!info] dipendenza transitiva
>$$X\to A\in F^+\mid A \not\in X$$
>è una **dipendenza transitiva** su R se A non è primo e per ogni chiave K di R si ha che X non è contenuto propriamente in K (e $K-X\neq \emptyset$)

[considerazioni sulle dipendenze]

>[!tip] definizione alternativa di 3NF
>Dato uno schema R e un insieme di dipendenze funzionali F, R è in 3NF se e solo se *non ci sono attributi che dipendono parzialmente o transitivamente da una chiave*.

#### dimostrazione
- prima parte (solo se)
 $$\text{lo schema R è in 3NF} \implies \forall X\to A\in F^+,\,A\not\in X$$

abbiamo due casi:
- o A appartiene a una chiave (è primo)
- o X contiene una chiave

da qui:
- se A primo, viene a mancare la prima condizione per avere una dipendenza parziale o trainsitiva 
- se A non è primo, allora X è superchiave (contiene una chiave). (se faccio K-X ottengo il vuoto, perché tutti gli elementi di X K sono contenuti in X) Visto che è superchiave, può contenere una chiave ma non essere contenuto propriamente SLIDE
 
dasda

- seconda parte
 
supponiamo per assurdo che R non sia 3NF - allora c'è almeno una dipendenza che viola la 3NF, quindi:
- a non è primo 
- E x non è superchiave

Siccome X non è superchiave, ci sono due casi mutualmente esclusivi:
- per ogni chiave K di R, X non è contenuto propriamente in nessuna chiave e K-X != vuoto - ma questa è la definizione di dipendenza transitiva (contraddizione)
- esiste una chiave che contiene completamente X - ma è una dipendenza parziale (contraddizione)




la decomposizione preserva le dipendenze