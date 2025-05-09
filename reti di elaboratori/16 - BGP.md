---
created: 2025-04-01
updated: 2025-05-09T10:41
---
## struttura di Internet

> [!summary] recap
> Internet è composta da:
> - dorsali, gestite da società private ⟶ forniscono la connettività globale
> - network provider ⟶ usati dalle dorsali per avere connettività globale, forniscono connettività ai clienti Internet
> - customer network ⟶ usano i servizi dei network provider

Fino ad ora, abbiamo seguito una visione omogenea della rete, vista come una collezione di router interconnessi (in cui ciascun router era indistinguibile dagli altri).

Nella pratica, però, ci sono 200 milioni di destinazioni, e archiviare le informazioni d’instradamento su ciascun host richiederebbe un’enorme quantità di memoria. In più, il traffico generato dagli aggiornamenti link state non lascerebbe banda per i pacchetti di dati, e il distance vector non convergerebbe mai.

Per questi motivi è necessaria **autonomia amministrativa**: ciascuno dovrebbe essere in grado di amministrare la propria rete, pur mantenendo la possibilità di connetterla alle reti esterne.
- in particolare, ogni ISP è un’autorità amministrativa autonoma: usa le sottoreti che vuole e impone politiche specifiche sul traffico

### instradamento gerarchico
Ogni ISP è un **sistema autonomo** (Autonomous System) e può eseguire un protocollo di routing che soddisfa le sue esigenze.

Tutti i router di uno stesso autonomous system eseguono lo stesso algoritmo di routing, chiamato protocollo di routing interno al sistema autonomo o intradominio (*intra-AS*), o Interior Gateway Protocol (*IGP*).

Deve invece esserci un unico protocollo inter-dominio che gestisce il routing tra i vari sistemi autonomi, chiamato inter-dominio (*inter-AS*) o Exterior Gateway Protocol (*EGP*)

