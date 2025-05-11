---
created: 2025-04-01
updated: 2025-05-11T15:12
---
# routing unicast, broadcast, multicast

> [!info] unicast
> Il routing **unicast** prevede la comunicazione tra **una sorgente e una destinazione**.
> 
> ![[unicast-es.png|center|400]]
> 

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
>forwarda il pacchetto solo se è arrivato 

