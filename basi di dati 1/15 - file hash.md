il file è suddiviso in **bucket** numerati da 0 a $B-1$.
- ciascun bucket è costituito da uno o più blocchi collegati tramite puntatori, ed è organizzato com un heap

L'accesso ai bucket avviene attraverso la bucket directory, che contiene $B$ elementi




il numero del bucket in cui deve trovarsi un record con chiave v è calcolato tramite una **funzione hash** (che restituisce un valore da 0 a $B-1$ - sicuramente si userà quindi $\%B$)



ogni ricerca richiede:
- la valutazione di h(v) per individuare il bucket
- l'esecuzione dell'operazione sul bucket che è organizzato come un heap





75 campo chiave è una trappola - mentre pr altre strutture dati quanto è grave una chiave conta, nel caso dell'heap/hash, quanto è grande una chiave non conta