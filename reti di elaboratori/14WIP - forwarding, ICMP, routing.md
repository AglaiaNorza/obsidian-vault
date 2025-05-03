---
created: 2025-04-01
updated: 2025-05-03T20:31
---
# forwarding di datagrammi IP
>[!info] forwarding
>Inoltrare significa **collocare il datagramma sul giusto percorso** (*porta di uscita del router*) che lo farà avanzare verso la destinazione.
>- ovvero, inviare il datagramma al *prossimo hop*

In particolare, quando un host ha un datagramma da inviare, lo invia al router della rete locale; quando un router riceve un datagramma da inoltrare, accede alla tabella di routing per trovare il successivo hop a cui inviarlo.
- l'inoltro richiede una riga nella tabella per ogni blocco di rete

>[!example] esempio 
>
>![[forw-es.png|center|450]]
>
>>[!summary] altra rappresentazione della tabella di inoltro
>>
>>![[tabella-inoltro.png|center|500]]
>>- la prima colonna contiene i bit che identificano il blocco di indirizzi (lunghezza inferiore a 32 bit)
>>- un datagramma contiene però l'indirizzo IP dell'host di destinazione (lungo 32 bit) e non indica la lunghezza del prefisso di rete ⟶ per l'**instradamento**, si lavora così:
>>	- si controllano le corrispondenze con le diverse righe della tabella in ordine: la prima corrispondenza sarà quella corretta (sono ordinate per lunghezza, quindi se i primi x bit combaciano con la prima riga, quella corretta sarà quella, altrimenti si confronta un numero $\leq$ di bit con la seconda riga, e così via)
>>
>>>[!example] esempio
>>>
>>>![[tabella-inoltro.png|center|450]]
>>>
>>>Per esempio, il processo di inoltro di un datagramma con indirizzo di destinazione `180.70.65.140` (`10110100 01000110 01000001 10001100`) è questo:
>>>- la prima maschera (`/26`), ovvero `10110100 01000110 01000001 11` è applicata all'indirizzo di destinazione
>>>
>>>![[mask-es.png|center|450]]
>>>
>>>- il risultato è `180.70.65.128`, che non combacia con l'indirizzo di rete corrispondente
>>>- la seconda maschera `/25` è applicata all'indirizzo di destinazione; il risultato è `180.70.65.128`, che combacia ⟶ l'indirizzo del salto successivo e il numero di interfaccia `m0` vengono estratti dalla tabella e riusati per inoltrare il datagramma

## aggregazione degli indirizzi
Inserire nella tabella una riga per ogni bloco può portare alla creazione di tabelle molto lunghe (in cui la ricerca impiega molto tempo). Una possibile soluzione è l'**aggregazione degli indirizzi**: si combinano più reti specifiche in una rete più generale quando queste hanno lo stesso next hop, senza perdere le informazioni di routing.

>[!example] esempio
> 
>![[aggreg-indirizzi.png|center|500]]
> - in questo caso, gli indirizzi delle società 1, 2 e 3 (tutti indirizzi del tipo `140.24.7.xx/26`) vengono aggregati da $\text{R2}$ in una sola rete più ampia (`140.24.7.0/24`)

# ICMP
>[!summary]- overview del livello di rete
>
>![[rete-overview.png|center|450]]

**Internet Control Message Protocol** è il protocollo che si occupa della **notifica degli errori**. Infatti, ci sono errori che IP non gestisce, come:
- caso in cui un router deve scartare un datagramma perché non riesce a trovare un percorso per la destinazione finale
- caso in cui un datagramma ha il campo `TTL == 0`
- caso in cui un host di destinazione non ha ricevuto tutti i frammenti di un datagramma entro un limite di tempo

ICMP viene quindi usato da host e router per *scambiarsi informazioni a livello di rete*.

>[!tip] ICMP viene considerato parte di IP anche se usa IP per inviare i suoi messaggi

>[!example] esempio
>
>![[ICMP.png|center|450]]
>
> Un tipico use-case di ICMP è fornire un meccanismo di **feedback per i messaggi IP** inviati. 
> 
> In questo esempio, $A$ sta cercando di mandare un datagramma IP a $B$. Tuttavia, quando arriva al router $\text{R3}$, viene rilevato un problema di qualche tipo e il datagramma viene scartato. Allora $\text{R3}$ invia un messaggio ICMP ad $A$ per avvisarlo, se possibile con abbastanza informazioni da permettergli di correggere il problema. 
> - $\text{R3}$ può inviare il messaggio ICMP solo ad $A$ (non a $\text{R2}$ o $\text{R1}$)

## messaggi ICMP
I messaggi ICMP hanno un campo `tipo` e un campo `codice` e contengono l'intestazione e i primi 8 byte del datagramma IP che ha provocato la generazione del messaggio.