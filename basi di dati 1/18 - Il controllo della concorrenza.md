In sistemi con una singola CPU, i programmi sono eseguiti concorrentemente in modo **interleaved** (interfogliato), per permettere un uso efficiente della CPU.
La CPU può quindi:
- eseguire alcune istruzioni di un programma
- sospendere quel programma
- eseguire istruzioni di altri programmi
- ritornare ad eseguire il primo

(su una base di dati, se vengono effettuate solo letture, l'accesso concorrente non crea problemi, mentre, se vengono effettuate anche scritture, l'accesso deve essere controllato)
## transazioni
Noi analizziamo le **transazioni**: esecuzioni di una parte di un programma che rappresenta un'unità logica di accesso o di modifica del contenuto sulla base di dati.
### proprietà delle transazioni
ACID
- **Atomicità** --> la transizione è *indivisibile* nella sua esecuzione - deve essere totale o nulla, non può essere parziale (in più, se la transazione viene abortita, bisogna disfare le modifiche che ha fatto)
- **Consistenza** --> quando la transazione finisce, il database deve essere in uno *stato consistente*, ovvero non deve violare eventuali vincoli di integrità (non ci devono essere inconsistenze tra i dati archiviati)
- **Isolamento** --> ogni transazione viene eseguita in modo *isolato e indipendente* dalle altre transazioni (e un suo eventuale fallimetno non deve interferire con le altre transizioni)
	- il risultato non deve dipendere dall'esecuzione di altre transazioni: se ho T1, T2, T3, non posso essere obbligato a eseguirle in un ordine particolare - se ho uno scheduler seriale, quindi, qualunque permutazione di transazione mi dà un risultato corretto.
- **Durabilità** --> (una volta che una transizione ha richiesto un commit work) i cambiamenti *non devono essere più persi*
	- (per evitare che si verifichino perdite di dati, vengono tenuti dei registri di log dove sono annotate tutte le operazioni sul DB)

## schedule

> [!info] def
> Uno schedule di un insieme $T$ di transazioni è un ordinamento delle operazioni nelle transazioni $T$ che *conserva l'ordine che le operazioni hanno all'interno delle singole transazioni*.
> (le operazioni possono essere separate da altre operazioni, ma mai invertite)

### schedule seriale

> [!info] schedule seriale
> Uno schedule seriale corrisponde ad una **esecuzione sequenziale** (non interfogliata) delle transizioni (ogni transazione entra ed esce solo una volta finita).
> (è quindi una permutazione delle transazioni in $T$)

- tutti gli schedule seriali sono corretti
## problemi
Visto che quando un item viene letto, esso viene portato nella memoria centrale in uno *spazio privato* della singola transazione, possono nascere una serie di problemi.
- se un'altra transazione leggerà lo stesso dato, lo porterà nella sua propria zona di memoria - avremmo quindi due copie dello stesso dato che verranno modificate, e potremmo avere dati sbagliati (una sovrascriverà l'altra)

### ghost/lost update
Avviene quando si perde un aggiornamento di un dato.

>[!example] esempio
>Abbiamo due transazioni, $T_{1},\,T_{2}$
>![[transazioni-es.png|center|350]]
>
>Consideriamo il seguente schedule:
>
>![[ghost-update.png|center|200]]
>
>Se il valore iniziale di $X$ è $X_{0}$, quello finale dovrebbe essere $X_{0}+M$ (sia se mandiamo prima $T_{1}$ che se mandiamo prima $T_{2}$).
>Invece, con questo schedule, otteniamo $X_{0}-N+M$.
>- l'aggiornamento di $X$ prodotto da $T_{1}$ viene quindi perso

### dato sporco (rollback a cascata)
Avviene quando un valore è il risultato di una transazione fallita (che va quindi "annullata")

> [!example] esempio
> ![[dato-sporco.png|center|200]]
>  
> A causa dell'atomicità delle transazioni, se $T_{1}$ fallisce, il valore di $X$ deve essere riportato a quello iniziale (quindi il `write` di $T_{2}$ dovrebbe dare risultato $X_{0}+M$ - ma, visto che $T_{2}$ ha usato il dato sporco prima del fallimento di $T_{1}$, il risultato sarà $X_{0}-N+M$

### aggregato non corretto
Avviene quando l'ordine delle operazioni fa sì che alcuni dati vengano processati dopo le operazioni che li richiedono.

>[!example] esempio
>![[aggregato-non-corretto.png|center|200]]
>
> La somma $Y:= Y+N$ viene eseguita dopo $somma := somma + Y$, quindi in $somma$ mancherà $N$.

## serializzabilità
- *tutti gli schedule seriali sono corretti*

Uno schedule non seriale è corretto se è **serializzabile**, ovvero se è *equivalente ad uno seriale*.

### equivalenza
Due schedule sono equivalenti se:
- (per ogni dato modificato) *producono valori uguali*
- e due valori sono uguali solo se sono prodotti dalla *stessa sequenza di operazioni*
	- ovvero se ho lo stesso ordine di accesso agli stessi item di almeno uno schedule seriale

>[!question]- perché non basta che siano uguali?
> 
>![[non-equivalenza-es.png|center|300]]
>
>questi due schedule producono lo stesso valore solo se il valore iniziale di $X$ è 10 - esiste quindi un caso in cui producono lo stesso valore, ma non sono equivalenti
 

>[!tip] schedule seriali ed equivalenza
>Gli schedule seriali possono non essere equivalenti tra loro, ma sono comunque tutti corretti.
>
>>[!example] esempio
>> 
>>![[schedule-seriali-es.png|center|300]]

## testare la serializzabilità
- non possiamo testare tutta una transazione, tutte le sue versioni seriali, e poi, in caso non fosse serializzabile, "buttare tutto" - è impratico
- in più, è praticamente impossibile determinare in anticipo in che ordine le operazioni verranno eseguite (ci sono troppi fattori che lo determinano)

Ci sono quindi dei metodi che *garantiscono la serializzabilità* di uno schedule.
Si può:
- imporre dei **protocolli** (es. lock) alla transazioni, in modo da garantire la serializzabilità di ogni schedule
- usare i **timestamp** delle transazioni - identificatori in base ai quali le operazioni possono essere ordinate in modo da garantire la serializzabilità

## item
Gli "oggetti" della base di dati si chiamano **item** - possono essere tabelle, righe, tuple... e avere quindi dimensioni variabili - e sono le "unità di accesso" delle BD.

- le dimensioni degli item devono essere definite in base all'uso che viene fatto della base di dati in modo tale che, in media, una transazione acceda a pochi item

Le dimensioni degli item utilizzate da un sistema sono dette la sua **granularità**.
- una granularità grande permette una gestione efficiente della concorrenza
- una granularità piccola può sovraccaricare il sistema, ma aumenta il livello di concorrenza (consente l'esecuzione concorrente di molte transizioni)