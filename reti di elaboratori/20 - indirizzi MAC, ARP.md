---
{}
---

>[!info] indirizzi MAC
>Gli **indirizzi MAC** sono indirizzi a **48bit** (6 byte in esadecimale) utilizzati a livello collegamento. Indirizzo MAC di sorgente e destinazione del frame vengono aggiunti al momento dell'incapsulamento di un datagramma del livello rete.
>- ciascun adattatore LAN ha il suo MAC address

>[!example] esempio 
>
>![[MAC-es.png|center|450]]

- La IEEE sovrintende la gestione degli indirizzi MAC.
- La comunicazione tra MAC address è peer-to-peer (tra le stazioni)
- Gli indirizzi MAC sono "orizzontali": non serve nessun server centralizzato, e non vanno aggiornati se spostati

## protocollo ARP
Il protocollo di **Address Resolution** permette di determinare l'indirizzo MAC di un nodo conoscendone solo l'indirizzo IP.
- ogni nodo IP nella LAN ha una **tabella ARP** contenente record del tipo:

$$
<\text{indirizzo IP; indirizzo MAC; TTL}>
$$

in cui $\text{TTL}$ (Time To Live) indica quando bisognerà eliminare una voce nella tabella.

>[!example] ARP nella stessa sottorete
>$A$ vuole inviare un datagramma a $B$, ma non possiede il suo indirizzo MAC.
>- $A$ trasmette in un *pacchetto broadcast* (ovvero con indirizzo MAC del destinatario = `FF-FF-FF-FF-FF-FF`) il messaggio di richiesta ARP contentente l'indirizzo IP di $B$
>- solo il nodo con l'indirizzo IP corretto risponderà, fornendo il proprio indirizzo MAC (in *unicast*)
>
>![[ARP-es.png|center|450]]
>
>>[!tip] la tabella ARP di un nodo si costituisce automaticamente e non deve essere configurata dall'amministratore di sistema

### pacchetti
I pacchetti ARP vengono incapsulati direttamente all'interno di frame di livello di collegamento.

>[!info] pacchetto ARP
>
>![[ARP-pacchetto.png|center|350]]
>
>- `Hardware Type` ⟶ **protocollo del livello collegamento** 
>- `Protocol Type` ⟶ **protocollo del livello di rete**
>- `Hardware length` e `Protocol length` fanno riferimento rispettivamente a `Source hardware address` e `Source protocol address`
>- `Destination hardware address` è **vuoto nelle richieste**
>- `Protocoll address` ⟶ **indirizzo IP**
