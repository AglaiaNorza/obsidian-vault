Il **timestamp** identifica una transazione.
È assegnato alla transazione al suo inizio dallo scheduler.
Può essere: 
- il valore di un contatore
- l'ora di inizio di una transazione

Il timestamp è crescente: se il timestamp di T1 è minore di quello di T2, la transazione T1 è iniziata prima di T2 (quindi, se fossero eseguite in modo seriale, T1 verrebbe eseguita prima).

## serializzabilità
Uno schedule è serializzabile se è **equivalente allo schedule seriale in cui le transazioni compaiono in base al loro timestamp**. 
Quindi, se per ciascun item acceduto da più di una transazione, l'ordine con cui le transazioni accedono all'item è quello imposto dai timestamp.

>[!example]- esempio 1
>consideriamo le due transazioni T1 e T2 con i loro timestamp $TS(T_{1})=110$ e $TS(T_{2})=100$.
>
>![[serial-es1.png|center|400]]
>
>quindi, uno schedule è serializzabile se è equivalente allo schedule seriale $T_{2}T_{1}$.
>
>![[serial-es2.png|center|250]]
>
>Per esempio, questo schedule non è serializzabile, perché $T_{1}$ legge $X$ prima che $T_{2}$ l'abbia scritto:
>
>![[serial-es3.png|center|250]]

>[!example]- esempio 2
>Consideriamo invece queste due transazioni con timestamp $TS(T_{1})=110$ e $TS(T_{2})=100$:
>
>![[serializ-es1.png|center|400]]
>
>
>Uno schedule serializzabile deve essere equivalente allo schedule seriale $T_{2}T_{1}$ $T_{2}T_{1}$
>
>![[serializ-es2.png|center|250]]
>
>quindi, questo schedule è serializzabile solo se *non viene eseguita* la scrittura di $X$ da parte di $T_{2}$:
>
>![[serializ-es3.png|center|250]]
## read e write timestamp
A ciascun item $X$ vengono assegnati due timestamp:
- **read timestamp** `read_TS(X)` --> il **più grande** tra tutti i timestamp di transazioni che hanno letto con successo $X$ 
- **write timestamp** `write_TS(X)` --> il **più grande** tra tutti i timestamp di transazioni che hanno scritto con successo $X$

>[!warning] il "più grande"
>il "più grande timestamp" NON è il timestamp dell'ultima transazione che l'ha letto/scritto - è il timestamp della transazione più "giovane" tra quelle che l'hanno letto/scritto

>[!example]- tornando all'esempio 2
>![[serializ-es4.png|center|400]]

## controllo della serializzabilità
Ogni volta che una transazione $T$ cerca di eseguire un `read(X)` o un `write(X)`, occorre confrontare il timestamp $TS(T)$ con il read timestamp e il write timestamp di $X$ per assicurarsi che sia rispettato l'ordine.

### algoritmo

###### scrittura:
T cerca di eseguire una `write(X)`.
1. se $read\_TS(X)>TS(T)$ (ovvero se una transazione più giovane l'ha già letta) $X$ viene rolled back
2. se $write\_TS(X)>TS(T)$, invece di fare un rollback, semplicemente non si effettua l'operazione di scrittura <small>(ignorando l'atomicità)</small>
3. se nessuna delle condizioni precedenti è soddisfatta, allora:
	- si esegue `write(X)` e si sovrascrive il write timestamp di $X$: $write\_TS(X):= TS(T)$

###### lettura:
T cerca di eseguire una `read(X)`.
1. se $write\_TS(X)>TS(T)$, $T$ viene rolled back
2. se $write\_TS(X)\leq TS(T)$, allora:
	- si esegue `read(X)` e, se $read\_TS(X)<TS(T)$, si sovrascrive: $read\_TS(X):= TS(T)$

>[!example] esempio 1
>Analizziamo questo schedule: 
> 
>![[timestamp-es.png|center|400]]
>
>Le transazioni hanno i seguenti timestamp: $TS(T1)=110,\,TS(T2)=100,\,TS(T3)=105$.
>Assumiamo che all'inizio tutti i read e write timestamp siano azzerati.
>
>![[timestamp-es2.png|center|500]]
>
>Al passo 9 la transazione $T2$ verrà abortita - cercherà di scrivere $X$, ma il suo timestamp sarà minore del read timestamp di $X$ (dato da $T1$ al passo 4): questo significa che $T1$ ha letto il valore errato di $X$: quello non ancora modificato da $T2$. 
>Per questo bisogna eseguire il rollback.

#### osservazioni
Notiamo che lo schedule delle transazioni superstiti è equivalente allo schedule seriale delle transazioni eseguite in ordine di arrivo.

>[!question] cosa provoca il rollback di una transazione?
>- se la transazione voleva *leggere* --> trovare un'altra transazione più giovane che ha già scritto i dati
>- se la transazione voleva *scrivere* --> trovare un'altra transazione più giovane che ha già letto i dati
>
>>[!tip] ricorda
>>Se invece una transazione vuole scrivere e trova una transazione più giovane che ha già *scritto* i dati, non è necessario il rollback (basta non eseguire la scrittura).

>[!bug] ignorare l'atomicità
>Perché possiamo **ignorare l'[[18 - Il controllo della concorrenza#transazioni|atomicità]]** saltando l'operazione di scrittura di una transazione $T$? 
>L'atomicità serve a garantire la *coerenza* in una base di dati. 
>Le transazioni che potrebbero trovare una situazione incoerente (a causa della non-scrittura) sono quelle che avrebbero dovuto leggere i dati scritti da $T$ (e si sarebbero ritrovate invece i dati di una transazionie più giovane $T'$) 
> - ma non esiste una transazione $T''$ arrivata dopo $T$ ma prima di $T'$ (con $TS(T')>TS(T'')>TS(T)$) che ha letto il dato: altrimenti, $T$ sarebbe stata rolled-back <small>(avrebbe cercato di scrivere quando una transazione più giovane aveva già letto)</small>.
> - se poi dovesse arrivare una transazione $T''$ che vuole leggere il valore di $X$, questa sarebbe rolled back per il primo passo dell'algoritmo di controllo della lettura (troverebbe $write\_TS(X)$ maggiore del proprio)

>[!question]- perché non il timestamp dell'ultima transazione?
>![[timestamp-domanda.png|center|400]]
>
>Prendiamo come esempio questo caso, con i timestamp $T1<T2<T3$.
>Se il write timestamp e il read timestamp fossero quelli dell'ultima transazione anziché della più giovane, $T2$ scriverebbe il valore di un item già letto da $T3$, quando $T3$ avrebbe dovuto leggere il valore di $T2$.