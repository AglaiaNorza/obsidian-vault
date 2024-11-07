Ricordiamo le condizioni per essere chiave:
un sottoinsieme $K$ di uno schema di relazione $R$ è una chiave di $R$ se 
- $K\to R\in F^+$
- non esiste un sottoinsieme proprio $K'$ di $K$ tale che $K'\to R\in F^+$ 

>[!tip] tips per trovare una chiave
>1) coviene partire da quelli con **cardinalità maggiore** - se la loro chiusura non contiene R, non ha senso calcolare la chiusura dei loro sottoinsiemi.
>2) **attributi che non appaiono mai come dipendenti devono essere per forza in una chiave** - la chiave li determinerà per riflessività
>3) un attributo che compare **sempre solo come dipendente** non sarà nella chiave
>4) un attributo che **non compare in F** dovrà essere nella chiave - come quelli che non ci sono come dipendenti
>5) non è detto che una chiave debba apparire come determinante - è possibile che un determinante con un pezzo aggiunto sia chiave
>6) aver trovato una chiave **non è sufficiente** - in uno stesso schema possiamo avere più chiavi

>[!example] esempio
>$R=(A,B,C,D,E,H)$ 
>$F=\{AB\to D,\,\, G\to A,\,\, G\to B, H\to E,\,\, H\to G,\,\, D\to H\}$
>
>cose da tenere a mente in questo caso: in tutte le chiavi ci deve essere $C$, perché non è in $F$, e in nessuna ci sarà $E$, perché non determina niente.
>
>le chiavi sono quindi:
>- $GC$ ($G\to A, \,G\to B,\,AB\to D,\,D\to H,\,H\to E$ e si aggiunge $C$)
>- $ABC$
>	- per questa dobbiamo verificare che $AC$ e $BC$ non siano chiavi
>- $DC$
>- $CH$

> [!example]- esempio 2
> ![[esempio-3nfchiavi.png|300]]
> (trovare dipendenze, chiave/i, se è 3NF)
> 
> le dipendenze sono:
> - $\text{O\#}\to\text{C\#}$ (un cliente può fare più di un ordine ma ogni ordine ha un cliente solo)
> - $\text{O\#, C}\to\text{N-pezzi}$
> 
> la chiave è: $(O\#, A\#)$
> 
> non è 3nf (es: $\text{O\#}\to\text{C\#}$ non la rispetta - $\text{O\#}$ è sottochiave e non superchiave, e $\text{C\#}$ non è primo)

#### metodo alternativo
- in alternativa, si può anche cominciare dagli insiemi individuati dalle dipendenze funzionali: data una dipendenza funzionale $V\to W \in F$ , calcoliamo la chiusura dell'insieme di attributi $X=R-(W-V)$
	- la differenza interna evita di considerare dipendenze vuote dovute alla riflessività
	- la differenza esterna esclude gli attributi "solo" dipendenti nella dipendenza in esame

#### test di unicità di una chiave
dati uno schema di relazione $R$ e un insieme di dipendenze funzionali $F$, calcoliamo l'intersezione degli insiemi $X=R-(W-V)$ con $V\to W\in F$.
- se l'intersezione di questi insiemi determina tutto $R$, allora questa è l'unica chiave di $R$
- se invece non determina tutto $R$, allora esistono più chiavi

[questa verifica non può essere usata all'esame per trovare le chiavi]