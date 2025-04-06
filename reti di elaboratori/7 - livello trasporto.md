---
created: 2025-03-20T14:18
updated: 2025-04-06T12:37
---
## connessione logica
I protocolli di trasporto forniscono la **comunicazione logica** tra processi applicativi di host differenti.

Per stabilire una comunicazione tra due processi, è necesario un metodo per individuare:
- host locale
- host remoto
- processo locale
- processo remoto

La coppia numero di porta-indirizzo IP si chiama **socket**.


- i primi 1024 numeri sono assegnati]

Come gestiamo i numeri di porta? C'è un API di comunicazione: socket API - interfaccia tra livello di comunicazione e livello di trasporto (ci permette di passare pacchetti al livello di trasporto).

Una socket appare come un terminale/file, ma è in realtà una struttura dati creata e utilizzata dal programma applicativo. 
Comunicare tra 