---
created: 2025-04-01
updated: 2025-05-10T17:25
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

 