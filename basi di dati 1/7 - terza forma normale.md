Torniamo al nostro [[4 - base di dati relazionale|esempio di base di dati]] che contiene informazioni su studenti ed esami (soluzione "buona" trovata alla fine)

La base di dati consiste di quattro schemi di relazione:
- Studente (Matr, CF, Cogn, Nome, Data, Com)
- Corso (C#, Tit, Doc)
- Esame (Matr, C#, Data, Voto)
- Comune (Com, Prov)
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

- possiamo notare che le istanze di Studente non devono soddisfare $\text{Cogn}\to\text{Nome}$ o $\text{Cogn}\to\text{Data}$ o $\text{Cogn}\to\text{Com}$ ecc.

Con considerazioni analoghe possiamo quindi concludere che *le uniche dipendenze funzionali non banali* che devono essere soddisfatte da un'istanza legale di Studente sono del tipo: $\text{K}\to\text{X}$ dove K **contiene una chiave** (Matr o CF)

(qui iniziamo a notare che le dipendenze devono tipicamente essere solo da una chiave o superchiave)

>[!question] dipendenze funzionali su esame
>- Esame (Matr, C#, Data, Voto)
>
>(in questo universo) uno studente può sostenere l'esame relativo ad un corso una sola volta, quindi per ogni esame esistono:
>- una sola data e un solo voto
>  
>  Quindi, ogni istanza legale di Esame deve soddisfare:
>  $$\text{(Matr, C\#)}\to\text{(Data, Voto)}$$
>  
>  Pertanto, $(Matr, C\#)$ è l'unica chiave per Esame.

>[!summary] conclusione
>Il nostro schema di relazione è quindi:
>- Studente (**Matr**, *CF*, Cogn, Nome, Data, Com)
>- Corso (**C#**, Tit, Doc)
>- Esame (**Matr, C#**, Data, Voto)
>- Comune (**Com**, Prov)
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
>- **X contiene una chiave** (è *superchiave*) oppure
>- **A appartiene ad una chiave** (è *primo*) 
>
>(notiamo quel $A \not\in X$ - quelle dipendenze non vanno considerate quando si cerca di capire se uno schema è in 3NF)
>
Altra definizione - se si vuole usare un insieme (Y) invece del singleton A:
> - $\forall X\to Y \in F$  appartente a X è tale che *X è superchiave* e *ogni attributo contenuto in Y è primo*.

>[!warning] attenzione
>- è sbagliato scrivere $\forall X\to A \in F$, (invece di $F^+$) perché A è singleton e dovremmo escludere tutte quelle del tipo $X \to AB$ (che potrebbero violare la 3NF) (invece, per $X\to AB$, $X \to A$ si trova in $F^+$)
>- è sbagliato anche dire solo $\forall X\to Y \in F$ (devo specificare che ogni attributo di Y è primo)
>- è importante non dimenticare il $A\not\in X$. Infatti, per riflessività, abbiamo sempre $X\to A$ in $F^A$, e quindi in $F^+$, anche quando A non è primo e X non è superchiave (quindi, nessuno schema sarebbe 3NF) (per esempio, se avessi $R=AB$ e $F=\{A\to B\}$, all'interno di $F^+$ avrei anche $B\to B$, con $B$ che non è né chiave né primo)

>[!example]- esempio 1
>$$R=ABCD \;\;\;\; F=\{A\to B,\;B\to CD\}$$
>- la chiave è A (per ogni istanza legale, se $t_{1}[A]=t_{2}[A]$ allora $t_{1}[B]=t_{2}[B]$ e, se $t_{1}[B]=t_{2}[B]$ allora $t_{1}[CD]=t_{2}[CD]$ - quindi se $t_{1}[A]=t_{2}[A]$ allora $t_{1}[CD]=t_{2}[CD]$ ($A\to B$ e $B\to CD$, quindi $A\to CD$)
>- ed è anche l'unica chiave, perché B non determina A, e sia C che D non determinano altri attributi
>
>ma è 3NF? valutiamo le dipendenze in $F$:
>- $A\to B$ è ok (A è superchiave)
>- $B\to CD$? dobbiamo controllare $B\to C$ e $B\to D$ - entrambe **violano la 3NF** perché B non è superchiave e né C né D sono primi - quindi *lo schema R non è in 3NF*

>[!example]- esempio 2
>$$R=ABCD\;\;\;\;F=\{AB\to CD,\, BC\to A, \,D\to AC\}$$
> 
>le chiavi sono:
>- $AB$ ($\to CD$) 
>- $BD$ (ho $D\to AC$ - per aumento, aggiungo $B$ e ho $BD\to AC$)
>- $BC$ (ho $BC\to A$ - per aumento, aggiungo $B$ a sinistra - ho $BC\to AB$, e $AB\to CD$, quindi, per transitività, ho anche $BC\to CD$)
>
>è 3NF? controlliamo le dipendenze in $F$.
>- $AB\to CD$ è ok, $AB$ è chiave
>- $BC\to A$ è ok, $BC$ è chiave
>- $D\to AC$ va decomposto: $D\to A$ è ok perché $A$ è primo, e la stesa cosa vale per  $D\to C$
>
>quindi lo schema *è 3NF*
### dipendenze parziali e transitive
Siano R uno schema di relazione e F un insieme di dipendenze funzionali su R.
>[!info] dipendenza parziale
>$$X\to A \in F^+ \mid A\not\in X$$
>è una **dipendenza parziale** su $R$ se $A$ non è primo ed $X$ è contenuto propriamente in una chiave di $R$.
>(quindi, invece di $X$ superchiave ho $X$ primo - è contenuto invece di contenere - non è rispettata la 3NF)
>>[!example]- esempio
>> 
>>Per esempio, nella relazione 
>> 
>>$$\text{Curriculum(Matr, CF, Cogn, Nome, DataN, Com, Prov, C\#, Tit, Doc, DataE, Voto)}$$ 
>> 
>>(con $Matr, C\#$ chiave), abbiamo $Matr\to Cogn$. 
>> 
>>Quindi, ad una coppia numero di matricola-codice corso, corrisponde un solo cognome: $(Matr, C\#)\to Cogn$ - l'attributo $Cogn$ *dipende parzialmente* dalla chiave $Matr, C\#$, perché è la conseguenza di $Matr\to Cogn$ (e $Matr$ è contenuto propriamente in una chiave)

>[!info] dipendenza transitiva
>$$X\to A\in F^+\mid A \not\in X$$
>è una **dipendenza transitiva** su $R$ se $A$ non è primo e per ogni chiave $K$ di $R$ si ha che $X$ non è contenuto propriamente in $K$ (e $K-X\neq \emptyset$)
>(quindi, $X$ non è superchiave - magari una parte di $X$ lo è, ma non tutto $X$ - non è rispettata la 3NF)
>>[!example]- esempio
>> 
>>$$\text{Studente (Matr, CF, Cogn, Nome, Data, Com, Prov)}$$
>> 
>>con $Matr$ chiave
>>
>>Abbiamo $Matr\to Com$ e $Com\to Prov$.
>>Per transitività, $Matr\to Prov$. Ma $Com$ non è contenuto propriamente nella chiave.
>
>> [!error] attenzione
> >- la dipendenza transitiva non è quella che si trova per transitività, ma quella che "permette di usare la transitività" - $A\to B,\,B\to C$ implica $A\to C$, ma la dipendenza transitiva è $B\to C$.

>[!tip] definizione alternativa di 3NF
>Dato uno schema R e un insieme di dipendenze funzionali F, R è in 3NF se e solo se *non ci sono attributi che dipendono parzialmente o transitivamente da una chiave*.

#### dimostrazione
- prima parte
 $$\text{lo schema R è in 3NF} \implies \text{non esistono dipendenze parziali o transitive}$$

(per ipotesi, lo schema è 3NF, quindi) 
Per quanto riguarda $\forall X\to A \in F^+,\, A \not\in X$, abbiamo due casi:
- o *$X$ contiene una chiave* (è superchiave)
- o *$A$ appartiene a una chiave* (è primo)

da qui:
1) se *$A$ primo*, viene a mancare la prima condizione per avere una dipendenza parziale o transitiva (entrambe vogliono $A$ non primo)
2) se *$A$ non primo*, allora $X$ è *superchiave* (contiene una chiave) - non può quindi essere contenuto *propriamente* in una chiave, e non è neanche possibile che $K-X\neq \emptyset$ (in quanto contiene tutta la chiave)

ora passiamo alla

- seconda parte
 $$\text{lo schema R è in 3NF} \impliedby \text{non esistono dipendenze parziali o transitive}$$
  
(per ipotesi, non esistono dipendenze parziali o transitive)
supponiamo per assurdo che $R$ non sia 3NF - allora c'è almeno una dipendenza che viola la 3NF, quindi: $X\to A\in F^+$ tale che:
- *$A$ non è primo* **E**
- *$X$ non è superchiave*

Siccome *$X$ non è superchiave*, ci sono due casi mutualmente esclusivi:
1) per ogni chiave $K$ di $R$, $X$ non è contenuto propriamente in nessuna chiave e $K-X\neq \emptyset$ -  ma questa è la *definizione di dipendenza transitiva* (contraddizione)
2) $X\subset K$ - esiste una chiave che contiene completamente $X$ (e non è uguale a $X$) - in questo caso, $X\to A$ è una *dipendenza parziale* (contraddizione)
### cosa vogliamo ottenere?
- un obiettivo da tenere presente quando si progetta una base di dati è quello di produrre uno schema in cui **ogni relazione sia in 3NF** 
	- in caso non lo sia, è sempre possibile trovare una *decomposizione* che sia in 3NF, e che rispetti altre due proprietà:

Abbiamo uno schema $ABC$ con dipendenze funzionali 
$$F=\{A\to B, \,B\to C\}$$ lo schema non è in 3NF perché in $F^+$ è presente $B\to C$ (la chiave è $A$).

- $R$ può essere decomposto in:
	- $R_{1}=AB\text{ con }\{A\to B\}$
	- $R_{2}=AB\text{ con }\{B\to C\}$
- oppure
	- $R_{1}=AB\text{ con }\{A\to B\}$
	- $R_{2}=AC\text{ con }\{A\to C\}$

entrambi sono in 3NF, ma il secondo *non è soddisfacente*.

> [!question] perché?
 > Consideriamo due istanze legali degli schemi ottenuti:
 > 
> ![[3nf-non-basta.png|center|350]]
> 
> - l'istanza dello schema originario R che posso ricostruire (con il join naturale) è:
> 
> ![[3nf-non-basta2.png|center|300]]
> 
> - questa non è però un'istanza legale di R, perché non soddisfa la dipendenza funzionale $B\to C$

>[!warning] join senza perdita
>deve essere preservato il join senza perdita (devono essere mantenute *tutte le dipendenze originarie*) - una "perdita" non significa tuple in meno, ma presenza di tuple estranee alla realtà di interesse.

>[!example]- esempio 
>consideriamo lo schema
> 
>$$\text{R = (Matricola, Comune, Provincia)}$$
> 
>$$F=\{Matricola\to Comune,\, Comune\to Provincia\}$$
> 
>(con chiave $Matricola$)
>non è in 3NF a causa della dipendenza transitiva $Comune\to Provincia$.
>
>Può essere scomposto in:
>- $R_{1}=(Matricola, Comune)$ con $\{Matricola\to Comune\}$
>- $R_{2}=(Comune, Provincia)$ con $\{Comune\to Provincia\}$
> 
>oppure
>- $R_{1}=(Matricola, Comune)$ con $\{Matricola\to Comune\}$
>- $R_{2}=(Matricola, Provincia)$ con $\{Matricola\to Provincia\}$
>
>entrambi sono in 3NF, ma la seconda soluzione non è soddisfacente.
>
>Consideriamo le istanze legali degli schemi ottenuti:
>
>![[decomposizione-3NF1.png|center|500]]
>
>L'istanza dello schema originario $R$ che ricostruisco tramite join naturale è la seguente:
>
>![[decomposizione-3NF2.png|center|400]]
>
>- ma questa **non è un'istanza legale** di $R$ !! perché non soddisfa la dipendenza funzionale $Comune\to Provincia$

In conclusione, quando si decompone uno schema per ottenerne uno 3NF, occorre tenere presente altri due *requisiti* per lo schema decomposto:
- deve **preservare le dipendenze funzionali** che valgono su ogni istanza legale dello schema originale
- deve permettere di **ricostruire tramite join naturale** ogni istanza legale dello schema originario senza aggiunta di informazione estranea.
### forma normale di Boyce-Codd
>[!info] definizione
>Una relazione è in forma normale di Boyce-Codd (BCNF) se in essa **ogni determinante è una superchiave** (ricordiamo che ogni chiave è superchiave).

(boy's code per gli amici)

> Ogni relazione in Boyce-Codd è anche in 3NF, ma non vale il contrario

- **può non essere possibile** decomporre uno schema non BCNF ottenendo sottoschemi BNCF e preservando allo stesso tempo tutte le dipendenze - invece, è **sempre possibile** per la 3NF

## domande orale
>[!question] possibili domande orale:
>- definizione 3NF
>- definizione dipendenze parziali e transitive
>- 3NF $\iff$ no dipendenze parziali e transitive
>- perché nella 3NF prendiamo $F^+$ e non $F$?
>- perché $A\not\in X$?
>- cosa si fa quando si ha uno schema non in 3NF?
>- (non credo abbia mai chiesto cosa sia la forma Boyce Codd)