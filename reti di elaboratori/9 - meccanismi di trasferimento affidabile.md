---
created: 2025-04-01
updated: 2025-04-08T12:44
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
### efficienza

