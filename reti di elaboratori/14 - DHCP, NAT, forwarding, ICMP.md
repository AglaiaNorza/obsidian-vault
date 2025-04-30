---
created: 2025-04-01
updated: 2025-04-30T17:16
---
# DHCP
L'obiettivo del **Dynamic Host Configuration Protocol** (DHCP) è consentire all'host di ottenere ddinamicamente il suo indirizzo IP dal server di rete.
- è possibile *rinnovare la proprietà* dell'indirizzo in uso
- è possibile il *riuso* degli indirizzi
- supporta anche gli utenti mobili che si vogliono unire alla rete
- è utilizzato nelle reti in cui gli host si aggiungono e rimuovono dalla rete con estrema frequenza

L'assegnazione degli indirizzi ai singoli host o rouoter è **automatizzata**.

>[!tip] nonostante sia un protocollo del livello di rete, DHCP è implementato come un programma client/server di livello applicazione
>in particolare:
>- il *client* è un host appena connesso che desidera ottenere informazioni sulla configurazione della rete (non solo un indirizzo IP)
>- il *server* è ogni sottorete che dispone di un server DHCP, o altrimenti un router che fa da agente di appoggio DHCP


