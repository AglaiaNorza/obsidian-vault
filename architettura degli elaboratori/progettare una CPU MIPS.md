La CPU è una *macchina sequenziale* - è formata da:
- uno **stato** (elementi che, se rimessi nella stessa condizione, fanno comportare la macchina allo stesso modo).
- un **circuito combinatorio**.

### cpu senza pipeline
1) definire come viene elaborata un'istruzione - **fasi di esecuzione**
2) scegliere le **istruzioni da realizzare**
3) scegliere le **unità funzionali necessarie**
4) **collegare** le unità funzionali
5) **costruire la Control Unit** (CU), che controlla il funzionamento della CPU
6) calcolare il massimo tempo di esecuzione delle istruzioni - che ci fornisce il **periodo di clock**

##### fasi di esecuzione di un'istruzione
1) **fetch** - *caricamento* di un'istruzione da memoria a CU
2) **decodifica** - *decodifica* dell'istruzione e *lettura argomenti* dai registri
3) **esecuzione** - *attivazione* delle unità necessarie
4) **memoria** - accesso alla memoria
5) **write back** - scrittura dei *risultati nei registri*
6) **aggiornamento program counter** - normale/salti condizionati/salti non condizionati

##### unità funzionali necessarie

| unità                  | descrizione                                             |
| ---------------------- | ------------------------------------------------------- |
| **PC**                 | registro che contiene <br>l'*indirizzo dell'istruzione* |
| **memoria istruzioni** | contiene le *istruzioni*                                |
| **adder**              | per *calcolare il PC* (successivo o salto)              |
| **registri**           | contengono gli *argomenti* delle istruzioni             |
| **ALU**                | fa *operazioni* aritmetico-logiche, confronti           |
| **memoria dati**       | da cui *leggere/scrivere* i dati                        |

Queste unità sono collegate da **datapath** - interconnessioni che definiscono il flusso delle informazioni nella CPU.
 
Se un'unità funzionale può ricevere *dati da più sorgenti*, è necessario inserire un **MUX** per selezionare la sorgente necessaria.

## finisci slide
