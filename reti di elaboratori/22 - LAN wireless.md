---
created: 2025-04-01
updated: 2025-05-25T12:48
---
Le reti wireless si dividono in:
- LAN wireless, disponibili in campus, uffici, bar, aree pubbliche
- reti cellulari
- bluetooth
- reti di sensori, RFID, smart objects

>[!example] alcuni standard
>
>![[wireless-standard.png|center|450]]
>
>Quello più usato è lo standard IEEE, con le sue diverse versioni:
>
> | Protocol | Release date | Freq.     | Rate (typical) | Rate (max) | Range (indoor) |
> | -------- | ------------ | --------- | -------------- | ---------- | -------------- |
> | Legacy   | 1997         | 2.4 GHz   | 1 Mbps         | 2 Mbps     | ?              |
> | 802.11a  | 1999         | 5 GHz     | 25 Mbps        | 54 Mbps    | ~30 m          |
> | 802.11b  | 1999         | 2.4 GHz   | 6.5 Mbps       | 11 Mbps    | ~30 m          |
> | 802.11g  | 2003         | 2.4 GHz   | 25 Mbps        | 54 Mbps    | ~30 m          |
> | 802.11n  | 2008         | 2.4/5 GHz | 200 Mbps       | 540 Mbps   | ~50 m          |

# LAN wireless
## elementi 

![[network-infrastructure.png|center|350]]

Una LAN wireless è composta da:
- **wireless hosts** ⟶ usati per eseguire applicazioni; possono essere fissi o mobili
- **base stations** ⟶ sono dei *relay* (ripetitori) tipicamente connessi a reti cablate, che si occupano di mandare pacchetti tra reti cablate e host wireless nella loro area
- **wireless links** ⟶ tipicamente usati per connettere gli host alle base station, ma possono anche essere usati come collegamenti per il backbone; variano in data rate e distanza di trasmissione
	- i [[19 - livello di collegamento#protocolli di accesso multiplo|protocolli di accesso multiplo]] regolano l'accesso ai lnink

## caratteristiche
Il mezzo trasmissivo delle LAN wireless è l'**aria**
