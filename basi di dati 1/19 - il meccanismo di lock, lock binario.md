>[!info] lock
>Il **lock** è il privilegio di accesso ad un singolo item, realizzato tramite una variabile associata all'item (*variabile lucchetto*), il cui valore descrive lo stato dell'item rispetto alle operazioni che possono essere effettuate su di esso.

(nella sua forma più semplice) un lock:
- viene **richiesto** da una transazione (`locking`) - se il valore è `unlocked`, la transazione può accedere all'item e alla variabile viene assegnato il valore `locked`
- viene **rilasciato** da una transazione (`unlocking`) - assegna alla variabile il valore `unlocked`

quindi
- il locking agisce come *primitiva di sincronizzazione* (se una transazione richiede un lock su un item su cui un'altra transazione )