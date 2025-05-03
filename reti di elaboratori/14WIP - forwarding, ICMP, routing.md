---
created: 2025-04-01
updated: 2025-05-03T10:03
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

