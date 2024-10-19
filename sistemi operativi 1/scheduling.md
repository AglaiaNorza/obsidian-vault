Un sistema operativo deve allocare risorse tra diversi processi che ne fanno richiesta contemporaneamente: tra le risorse, c'è il processore (e quindi il tempo di esecuzione). Questa risorsa viene allocata tramite lo **scheduling**.

>[!question] qual è lo scopo dello scheduling?
>- *assegnare ad ogni processore i processi* da eseguire, man mano che questi vengono creati e distrutti
>- va fatto *ottimizzando* vari aspetti:
>	- tempo di risposta
>	- throughput (portare a termine più processi nella stessa unità di tempo)
>	- efficienza del processore
>- non fare favoritismi tra processi (con stessa priorità) ma *gestire la priorità* dei processi quando necessario
>- evitare la starvation dei processi
>- usare il processore in modo efficiente
>- avere un **overhead** basso (overhead = lavoro fatto in più - lo scheduler deve essere veloce ed efficiente)

#### tipi di scheduling
Ci sono diversi tipi di scheduling (a seconda di quanto spesso vengono eseguiti)
- **long-term** (eseguito molto di rado) - decide l'aggiunta ai processi da essere eseguiti
- **medium-term** (eseguito ogni tanto)- decide l'aggiunta ai processi in memoria principale
- **short-term** - decide quale processo va eseguito tra quelli pronti
- **I/O** - decide a quale processo assegnare un dispositivo I/O, tra quelli che lo stanno richiedendo

### stati dei processi e scheduling
molte delle transizioni del [[processi#stato di un processo|modello a sette stati]] sono dovute a uno scheduler.
 
![[transizioni-scheduler.png|500]]

![[code-scheduling.png]] 

#### long-term scheduling
spesso è **FIFO**. 
Altrettanto spesso, è FIFO con delle condizioni: pirorità, requisiti I/O, o tempo di esecuzione atteso.
- controlla il grado di multiprogrammazione (e decide se mettere un processo in RAM o su disco)
- può essere chiamato in causa anche quando non ci sono nuovi processi (es. quando termina un processo o quando processi sono idle da troppo tempo)

tipiche strategie:
- i lavori *batch* (non interattivi) vengono accodati e il LTS li prende man mano che ritiene giusto
- i lavori *interattivi* vengono ammessi fino a che non si satura il sistema
- se si sa quali sono *I/O-bound* e quali *CPU-bound* (usano molto I/O o CPU), può mantenere un mix tra i due tipi

#### medium-term scheduling
è parte della funzione di **swapping** dei processi (passaggio da memoria secondaria a principale e viceversa)
- l'obiettivo principale è gestire il grado di multiprogrammazione

#### short-term scheduler
chiamato anche **dispatcher**.
Eseguito più frequentemente, sulla base di eventi (interruzioni di clock o I/O, syscalls, segnali).
Il suo scopo è *allocare tempo di esecuzione* su un processore per ottimizzare il comportamento dell'intero sistema, in base a determinati indici prestazionali.

>[!tip] criteri utente e sistema
>Occorre distinguere i criteri per lo short term scheduling in utente e di sistema.
>
>I criteri per l'*utente* sono quelli che un singolo utente può apprezzare (es. tempo di risposta), mentre quelli per il *sistema* sono legati all'uso efficiente di un procesore.