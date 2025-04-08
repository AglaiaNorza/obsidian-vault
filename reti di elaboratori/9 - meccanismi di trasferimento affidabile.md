---
created: 2025-04-01
updated: 2025-04-08T21:50
---
## stop-and-wait
Lo stop-and-wait è un meccanismo orientato alla connessione, che implementa controllo del flusso e controllo degli errori.
- mittente e destinatario usano una **finestra di scorrimento di dimensione 1**
- il mittente invia un pacchetto alla volta e ne **attende** l'ack prima di spedire il successivo
- quando il pacchetto arriva al destinatario, viene calcolato il checksum 
	- se il pacchetto è corrotto, viene scartato *senza informare il mittente*
- per capire se un pacchetto è andato perso, il mittente usa un **timer** (in quanto non può aspettare all'infinito di ricevere un ack)
	- se il timer scade e non ha ricevuto un ack, il pacchetto viene rinviato
	- il mittente deve quindi tenere una *copia* del pacchetto spedito fino a quando non riceve il riscontro

Il **controllo degli errori** viene implementato quindi tramite il numero di sequenza e l'utilizzo di ack e timer. Il **controllo del flusso** è intrinseco, in quanto non si spedisce più di un pacchetto alla volta.

### numeri di sequenza e riscontro
Per gestire pacchetti duplicati, stop-and-wait utilizza i numeri di sequenza $0$ e $1$. 
- Il numero di riscontro (ack) indica quindi, in *aritmetica modulo 2*, il numero di sequenza del prossimo pacchetto atteso dal destinatario.
- (se il destinatario ha ricevuto correttamente il pacchetto $0$, invia un ack con valore $1$)

> [!example] situazioni possibili
> Supponiamo che il mittente abbia inviato il pacchetto con numero di sequenza
> $x$. Si possono verificare 3 casi:
> 1. Il pacchetto **arriva correttamente** al destinatario, che invia un riscontro ⟶ il riscontro arriva al mittente, che *invia il pacchetto successivo* numerato $1-x$
> 2. Il pacchetto risulta corrotto o **non arriva** al destinatario ⟶ il mittente, allo scadere del timer, *invia nuovamente il pacchetto* $x$
> 3. Il pacchetto arriva correttamente al destinatario, ma il **riscontro viene perso** o corrotto ⟶ scade il timer e il mittente *rispedisce* $x$. 

>[!info] rappresentazione tramite FSM
>**mittente**:
>
>![[snw-FSM-mit.png|center|500]]
>
>- una volta inviato un pacchetto, il mittente si blocca e aspetta finché non riceve un ack
>
>**destinatario**:
>
>![[snw-FSM-dest.png|center|500]]
>
>- il destinatario è sempre nello stato *ready*

**diagramma di comunicazione**:

![[diagramma-snw.png|center|450]]

>[!error] Lo stop-and-wait è inefficiente quando il prodotto $\text{rate} \cdot\text{ritardo}$ (ovvero il numero di bit che il mittente può inviare prima di ricevere un ack) è elevato
>>[!example] esempio
>>Se per esempio:
>>- rate = $1\text{Mbps}$
>>- ritardo di andata e ritorno di 1 bit = $20\text{ms}$
>>- pacchetti di dimensione $1000\text{bit}$
>>
>>$\text{rate} \cdot\text{ritardo}=(1\times 10^6)\times(20 \times 10^{-3})=20000\text{bit}$
>>
>>Il mittente potrebbe quindi inviare $20000\text{bit}$ nel tempo necessario per andare dal mittente al ricevente, ma ne invia solo $1000$ (un solo pacchetto)
>>
>>Il coefficiente di utilizzo del canale è $\frac{1000}{20000}=5\%$

## protocolli con pipeline
Con il **pipelining**, il mittente ammette *più pacchetti* in transito, ancora da notificare.
- l'intervallo dei numeri di sequenza deve essere incrementato
- i pacchetti devono essere memorizzati in un buffer presso mittente e/o ricevente

Ci sono due forme generiche di protocolli con pipeline: **go-back-N** e **ripetizione selettiva**.

### go-back-N
- I **numeri di sequenza** sono calcolati modulo $2^m$ con $m$ dimensione del campo "numero di sequenza" in bit.
- L'ack indica il numero di sequenza del *prossimo pacchetto atteso*
- L'ack è **cumulativo**: se si invia un ack, vuol dire che tutti i pacchetti fino al numero di sequenza indicato nell'ack sono stati ricevuti correttamente
	-  (esempio: ack# = 7 significa che i pacchetti fino al 6 sono stati ricevuti correttamente, e il destinatario attende il 7)

#### finestre di invio e ricezione
La <u>finestra di invio</u> definisce una porzione immaginaria di dimensione massima $2^m-1$ con tre variabili: $S_{f},\,S_{n},\,S_{\text{size}}$
- $S_{f}$ rappresenta il **primo pacchetto non riscontrato** (primo = più vecchio)
- $S_{n}$ rappresenta il **prossimo pacchetto da inviare**
- $S_{\text{size}}$ rappresenta la **dimensione della finestra di invio**

![[finestrai-gbn.png|center|550]]

La finestra di invio può **scorrere** di una o più posizioni quando viene ricevuto un riscontro privo di errori con $S_{n}> \text{ack\#}\geq S_{f}$ (in aritmetica modulo $2^m$).
- (ovvero si riceve un ack per un pacchetto con un numero minore di quelli ancora da inviare, e maggiore del primo inviato e non riscontrato (ovvero parte di quelli in sospeso))

>[!example] esempio di scorrimento
>
>![[scorrimento-fin.png|center|500]]

La <u>finestra di ricezione</u> ha dimensione 1.

> [!info] schema generale
>  
> ![[go-back-n.png|center|500]]

