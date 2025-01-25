Il **timestamp** identifica una transazione.
È assegnato alla transazione al suo inizio dallo scheduler.
Può essere: 
- il valore di un contatore
- l'ora di inizio di una transazione

Il timestamp è crescente: se il timestamp di T1 è minore di quello di T2, la transazione T1 è iniziata prima di T2 (quindi, se fossero eseguite in modo seriale, T1 verrebbe eseguita prima).

## serializzabilità
Uno schedule è serializzabile se è **equivalente allo schedule seriale in cui le transazioni compaiono in base al loro timestamp**. 
Quindi, se per ciascun item acceduto da più di una transazione, l'ordine con cui le transazioni accedono all'item è quello imposto dai timestamp.

>[!example]- esempio
>consideriamo le due transazioni T1 e T2 con i lor timestamp $TS(T_{1})=110$ e $TS(T_{2})=100$.
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

## read e write timestamp
A ciascun item $X$ vengono assegnati due timestamp:
- **read timestamp** `read_TS(X)` --> il **più grande** tra tutti i timestamp di transazioni che hanno letto con successo $X$ 
- **write timestamp** `write_TS(X)` --> il **più grande** tra tutti i timestamp di transazioni che hanno scritto con successo $X$

>[!warning] il "più grande"
>il "più grande timestamp" NON è il timestamp dell'ultima transazione che l'ha letto/scritto - è il timestamp della transazione più "giovane" tra quelle che l'hanno letto/scritto