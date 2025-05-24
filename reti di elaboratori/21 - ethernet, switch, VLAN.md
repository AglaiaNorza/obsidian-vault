---
created: 2025-04-01
updated: 2025-05-24T11:32
---
>[!info]- standard IEEE 802
>IEEE ha prodotto diversi standard per le LAN (collettivamente noti come IEEE 802), che includono:
> - specifiche generali del progetto (802.1)
> - logical link control (LLC, 802.2)
> - CSMA/CD (802.3)
> - token bust (802.4, destinato a LAN per automazione industriale)
> - token ring (802.5)
> - DQDB (802.6, destinato alle MAN)
> - WLAN (802.11)
> 
> I vari standard differiscono a livello fisico e nel sottolivello MAC, ma sono **compatibili a livello data link**.

Ethernet è la tecnologia di rete che consente la comunicazione tra dispositivi in una LAN, e detiene una posizione dominante nel mercato delle LAN cablate (è stata la prima LAN cablata ad alta velocità con vasta diffusione).

![[ethernet-standard.png|center|450]]

### formato dei frame
>[!info] frame




>![[frame-ethernet.png|center|500]]

> - `Preambolo` ⟶ 7 byte con valore `10101010`: servono per **attivare le NIC** (schede di rete) dei riceventi e **sincronizzare** i loro orologi con quello del trasmittente (fa parte dell'header a livello fisico)
> - `SFD` (Start Frame Delimiter) ⟶ 1 byte con valore `10101011`: definisce l'**inizio del frame** (è l'ultima possibilità di sincronizzazione); gli ultimi due bit (`11`) indicano che inizia l'header MAC
> -`Indirizzi sorgente e destinazione` ⟶ 6 byte; quando una NIC riceve