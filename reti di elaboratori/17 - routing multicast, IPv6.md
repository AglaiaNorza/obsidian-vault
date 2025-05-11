---
created: 2025-04-01
updated: 2025-05-11T15:40
---
# unicast

> [!info] unicast
> Il routing **unicast** prevede la comunicazione tra **una sorgente e una destinazione**.
> 
> ![[unicast-es.png|center|400]]
> 
# broadcast
>[!info] broadcast
>Il routing **broadcast** prevede l'invio di un pacchetto da un nodo sorgente **a tutti i nodi della rete** (IP sorgente ⟶ indirizzo broadcast).


Il broadcast può essere eseguito in due modi: attraverso *uncontrolled* o *controlled* flooding.
## uncontrolled flooding
Nell'uncontrolled flooding, quando un nodo riceve un pacchetto broadcast, lo duplica e lo **invia a tutti i nodi vicini** eccetto quello da cui lo ha ricevuto.
- se il grafo ha cicli, una o più copie del pacchetto cicleranno all'infinito nella rete

## sequence number controlled flooding
Nel sequence number controlled flooding, **non vengono forwardati pacchetti già ricevuti** ed inoltrati. Ogni nodo tiene una lista di `(IP, #sequenza)` dei pacchetti già ricevuti, duplicati e inoltrati. Quando riceve un pacchetto, controlla nella lista e: se è già stato inoltrato, lo scarta, altrimenti lo inoltra.

## reverse path forwarding
Nel reverse path forwarding, un pacchetto viene forwardato solo se è arrivato dal link che è **sul suo shortest path** (unicast)

>[!example] esempio
>
>![[controlled-flood-es.png|center|300]]
>

RPF elimina il problema dell'invio di troppi pacchetti sulla rete, ma non elimina completamente la ridondanza nella trasmissione
- per esempio, nel grafo sopra, $B,\,C,\,D ,\,E$ ed $F$ ricevono uno o due pacchetti ridondanti

La soluzione è costruire uno **spanning tree** prima di inviare i pacchetti broadcast.

>[!summary] costruzione dello spanning tree (center-based)
>- Si prende un nodo come centro (esempio: $E$)
>- ogni nodo invia un messaggio di join in unicast verso il centro
>- i messaggi vengono inoltrati finché arrivano alla radice o a un nodo che appartiene già all'albero
>
>![[spanning-tree-centerbased-reti.png|center|400]]

Quindi i pacchetti vengono inoltrati **solo sui link dell'albero**, e ogni nodo riceve solo una copia del pacchetto.

# multicast

> [!info] multicast
> Il routing **multicast** prevede la comunicazione tra **una sorgente** e **un gruppo di destinazioni**.
> 
> ![[multicast.png|center|450]]
> 
> Viene usato da applicazioni come streaming audio/video a gruppi di persone, trasferimenti di aggiornamenti software su un gruppo di macchine...

Si differenzia dall'**unicast multiplo** per i fatto che viene inviato un solo datagramma, che verrà poi duplicato dai router.
- il multicast, quindi, elimina i ritardi causati dall'invio di multipli pacchetti dell'unicast multiplo

Per poter comunicare con host che partecipano a un gruppo pur appartenendo a reti diverse 



