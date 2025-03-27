Stop-and-wait è un meccanismo 




### numeri di sequenza e riscontro
I numeri di sequenza 0 e 1 sono sufficienti per far funzionare correttamente lo stop-and-wait.
Si usa una convenzione: il numero di riscontro (ack) indica il numero di sequenza del prossimo pacchetto atteso dal destinatario (modulo 2) (se ha ricevuto correttamente 0, ).

Si chiama stop-and-wait perché il mittente si bllocca dopo aver inviato un pacchetto e aspetta fino a quando non riceve l'ack.

>[!info] FSM
>![[FSM-mittente-SW.png|center|500]]




riassunto

checksum - errori all'interno dei pacchetti (a livello di bit)
ack, numero di sequenza, timeout - errori a livello di pacchetto
finsetra scorrevole - migliorare le prestazioni della rete

 più costaosa rispetto al go back n e speidsce meno pacchetti- funziona meglio in situazioni di ocngestinoe mentre go back n funziona meglio quando la rete funziona come dovrebbe


