---
created: 2025-04-01
updated: 2025-04-17T12:01
---
## stop-and-wait
Lo stop-and-wait è un meccanismo orientato alla connessione, che implementa controllo del flusso e controllo degli errori.
- mittente e destinatario usano una **finestra di scorrimento di dimensione 1**
- il mittente invia un pacchetto alla volta e ne **attende** l'ACK prima di spedire il successivo
- quando il pacchetto arriva al destinatario, viene calcolato il checksum 
	- se il pacchetto è corrotto, viene scartato *senza informare il mittente*
- per capire se un pacchetto è andato perso, il mittente usa un **timer** (in quanto non può aspettare all'infinito di ricevere un ACK)
	- se il timer scade e non ha ricevuto un ACK, il pacchetto viene rinviato
	- il mittente deve quindi tenere una *copia* del pacchetto spedito fino a quando non riceve il riscontro

Il **controllo degli errori** viene implementato quindi tramite il numero di sequenza e l'utilizzo di ACK e timer. Il **controllo del flusso** è intrinseco, in quanto non si spedisce più di un pacchetto alla volta.

### numeri di sequenza e riscontro
Per gestire pacchetti duplicati, stop-and-wait utilizza i numeri di sequenza $0$ e $1$. 
- Il numero di riscontro (ACK) indica quindi, in *aritmetica modulo 2*, il numero di sequenza del prossimo pacchetto atteso dal destinatario.
- (se il destinatario ha ricevuto correttamente il pacchetto $0$, invia un ACK con valore $1$)

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
>- una volta inviato un pacchetto, il mittente si blocca e aspetta finché non riceve un ACK
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
- L'ACK indica il numero di sequenza del *prossimo pacchetto atteso*
- L'ACK è **cumulativo**: se si invia un ack, vuol dire che tutti i pacchetti fino al numero di sequenza indicato nell'ACK sono stati ricevuti correttamente
	-  (esempio: ack# = 7 significa che i pacchetti fino al 6 sono stati ricevuti correttamente, e il destinatario attende il 7)

#### finestre di invio e ricezione
La <u>finestra di invio</u> definisce una porzione immaginaria di dimensione massima $2^m-1$ con tre variabili: $S_{f},\,S_{n},\,S_{\text{size}}$
- $S_{f}$ rappresenta il **primo pacchetto non riscontrato** (primo = più vecchio)
- $S_{n}$ rappresenta il **prossimo pacchetto da inviare**
- $S_{\text{size}}$ rappresenta la **dimensione della finestra di invio**

![[finestrai-gbn.png|center|550]]

La finestra di invio può **scorrere** di una o più posizioni quando viene ricevuto un riscontro privo di errori con $S_{n}> \text{ack\#}\geq S_{f}$ (in aritmetica modulo $2^m$).
- (ovvero si riceve un ACK per un pacchetto con un numero minore di quelli ancora da inviare, e maggiore del primo inviato e non riscontrato (ovvero parte di quelli in sospeso))

>[!example] esempio di scorrimento
>
>![[scorrimento-fin.png|center|500]]

>[!tip] dimensione della finestra di invio
>La dimensione della finestra di invio deve essere $2^m-1$ perché:
> 
> Consideriamo $m=2$. I numeri di sequenza dei pacchetti sono $0,\,1,\,2,\,3$. 
>
>Se il mittente ha una finestra di dimensione $2^m-1=2^2-1=3$, allora:
>- può inviare al massimo 3 pacchetti prima di ricevere un ACK (es. $0,\,1,\,2$).
>- non potrà mai inviare un pacchetto "nuovo" con lo stesso numero di sequenza di un pacchetto vecchio che è ancora in attesa di ACK, quindi il destinatario saprà sempre distinguere se un pacchetto è nuovo o una copia
>
>Invece, con una finestra di dimensione $2^m=4$:
>- il mittente può inviare i pacchetti $0,1,2,3$ e poi ritrasmettere $0$. Ma il destinatario, che riceve $0$, non può sapere se sia il vecchio pacchetto $0$ mai arrivato o un nuovo pacchetto $0$.
>
>![[dim-finestra-gbn.png|center|400]]

---- 

La <u>finestra di ricezione</u> ha **dimensione 1**, perché il destinatario è sempre in attesa di uno specifico pacchetto. Qualsiasi pacchetto arrivato fuori sequenza viene scartato.

![[finestrar-gbn.png|center|550]]

La finestra può scorrere di una sola posizione: $R_{n}=(R_{n}+1)mod\; 2^m$
 
> [!tip] timer e rispedizione
> Il mittente mantiene un **timer** per il più vecchio pacchetto non riscontrato. Allo scadere del timer si ha il "go bACK N", ovvero **tutti i pacchetti in attesa di riscontro vengono rispediti** (poiché la finestra di ricezione ha dimensione 1, il destinatario non può bufferizzare i pacchetti fuori sequenza)

#### schemi
>[!info] FSM mittente
>
>![[gbn-FSM1.png|center|500]]

>[!info] FSM destinatario
>
>![[gbn-FSM2.png|center|500]]

>[!example]- go-back-N in azione (perso pacchetto dati):
>
>![[gbn-perso.png|center|400]]

### ripetizione selettiva
Il problema principale di go-back-n è che, se si perde un solo pacchetto, è necessario ritrasmettere tutti i successivi già inviati. Nella **ripetizione selettiva**, il mittente ritrasmette soltanto i **pacchetti per cui non ha ricevuto un ACK**.
- il mittente mantiene un timer per ogni pacchetto non riscontrato

Il ricevente invia riscontri specifici per tutti i pacchetti ricevuti correttamente (in ordine o anche fuori sequenza) e, se necessario, mantiene un buffer dei pacchetti per eventuali consegne in sequenza al livello superiore.

>[!info] schema generale
>
>![[ripetizione-selettiva.png|center|500]]
#### invio e ricezione
Le finestre di invio e di ricezione hanno la **stessa dimensione**.

![[sel-rep-finestrainvio.png|center|500]]
 
- la finestra di invio può muoversi solo quando c'è una *sequenza in ordine di pacchetti confermati* (quindi, in questo esempio, aspetta almeno $0$ e $1$)
- c'è un **timer per ogni pacchetto** in attesa di riscontro - quando scade, si rinvia solo quel pacchetto

![[sel-rep-finestraric.png|center|500]]

- l'ACK non è cumulativo ma **individuale**: indica il numero di sequenza di un pacchetto ricevuto correttamente (e non il prossimo atteso: non avrebbe senso per questo modello)

>[!info] FSM mittente
>
>![[FSM-selrep-mit.png|center|500]]


>[!info] FSM destinatario
>
>![[FSM-selrep-dest.png|center|500]]

#### dimensione delle finestre
Per questo meccanismo, la dimensione delle finestre non può essere $2^m-1$, ma deve essere $2^{m-1}$.

> [!example] esempio esplicativo
> Infatti, se si usasse una finestra con dimensione $2^m-1$, potrebbe accadere una situazione come questa:
> - il mittente spedisce i pacchetti $0,\,1,\,2$, che vengono ricevuti correttamente (quindi la finestra di accettazione scorre)
> - gli ACK vengono però persi, quindi il mittente pensa di doverli rispedire
> - il mittente rispedisce quindi il pacchetto $0$, che viene erroneamente accettato come il primo della sequenza successiva
>
> ![[dim-fin1.png|center|400]]
> 
> Invece, con una finestra di dimensione $2^{m-1}$, anche se la finestra scorresse, il pacchetto verrebbe correttamente scartato:
> 
> ![[dim-fin2.png|center|350]]

### go-back-n vs selective-repeat
Se il prodotto banda-ritardo della rete è grande, l'affidabilità è buona e il ritardo è basso, conviene utilzzare il protocollo go-back-n, che permette di usare più della capacità della rete.

Se invece il prodotto banda-ritardo è piccolo, la rete non è molto affidabile, o introduce lunghi ritardi, conviene usare il selective-repeat.
## protocolli bidirezionali: piggybacking
In realtà, i pacchetti non viaggiano in maniera unidirezionale, ma in entrambe le direzioni. Per migliorare l'efficienza dei protocolli bidirezionali, viene usata la tecnica del **piggybacking**: quando un pacchetto trasporta dati da $A$ a $B$, può trasportare anche i riscontri relativi ai pacchetti ricevuti da $B$ e viceversa.

## riassunto dei meccanismi
| Meccanismo                      | Uso                               |
| ------------------------------- | --------------------------------- |
| checksum                        | per gestire errori nel canale     |
| acknowledgement                 | per gestire errori nel canale     |
| timeout                         | ACK con errori, perdita pacchetti |
| finestra scorrevole, pipelining | maggior utilizzo della rete       |
