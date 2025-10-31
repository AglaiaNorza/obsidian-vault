

### Elapsed parallel time
```C
double MPI_Wtime(void);
```

rturns the # of seconds that have elapsed since ?? in the past

>[!question] measuring
> What time do we consider when we have to calculate how much time a program takes? Each rank might finish at different times.


>[!question] is every rank going to start at the same time?
> not necessarily.
> se non partono insieme, un processo ci puo' mettere piu' tempo per esempio per aspettare (receive) (la send di) un altro processo che e' partito dopo

Per far si' che i processi inizino qualcosa allo stesso tempo, si puo' usare una `MPI_Barrier` (ma comunque potrebbero uscire dalla barriera in tempi diversi).

(I tempi non sono deterministici) ⟶ **noise**

Examples:
- se lancio un'applicazione sul mio portatile, ci sono altri processi che stanno essendo eseguiti - in base alle decisioni dello scheduler, i tempi saranno diversi 
- le risorse di calcolo sono separate ma la rete di calcolo e' condivisa, quindi altre applicazioni potrebbero utilizzarla (es. due processi fanno una send x due processi di 2 utenti diversi, che pero' attraversano lo stesso link fisico della rete)
- 