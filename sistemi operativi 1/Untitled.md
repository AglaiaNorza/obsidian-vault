


Basi di Dati-Modulo I-Canale M-Z
Prof. De Marsico
07 novembre 2018
1) Sia data la seguente base di dati relativa ad una compagnia aerea
AEREO (<u>ID</u>, Costruttore, Modello, NPosti, AnnoC, AnnoR)
VOLO(<u>Sigla</u>, Partenza, Arrivo, Orario)
AEROPORTO(<u>Sigla</u>, Città)
VIAGGIO(<u>ID</u>, SiglaVolo, Aereo, Data)
PERSONALE(<u>CF</u>, ID, Nome, Cognome, Data Nascita) 
EQUIPAGGIO(<u>Viaggio, Pers, Data</u>)

NOTE
• AEREO.AnnoC e AEREO.AnnoR sono rispettivamente l'anno di costruzione e l'anno di ultima revisione di un aereo (se l'aereo non è stato mai revisionato AnnoR-0000/00)
• VOLO.Sigla è la sigla di un volo
• VOLO.Partenza e VOLO.Arrivo sono sigle di aeroporti
• Le città più grandi possono avere più aeroporti
• Un volo viene effettuato sempre alla stessa ora in più date
- VIAGGIO.SiglaVolo è la sigla di un volo effettuato in data VIAGGIO.Data
• VIAGGIO.Aereo è l'ID di un aereo
EQUIPAGGIO.Viaggio è l'ID di un viaggio
-  EQUIPAGGIO,Pers è l'ID di un membro del personale
• Un membro del personale può partecipare a più viaggi in date diverse.


1a) Trovare le date del 2018 in cui sono stati effettuati voli diretti a Roma con aerei mai revisionati
1b) Trovare i dati completi di membri del personale che non hanno mai volato a gennaio 2018.


2) Siano dati lo schema R=ABCDE e l'insieme di dipendenze funzionali
F=(AB->CD, BC->AE, D->AC, A->E)
2a) Determinare le tre chiavi dello schema
26) Dire se lo schema è 3NF e giustificare l'affermazione
2c) Trovare una decomposizione dello schema tale che:
- ogni sottoschema è 3NF
- la decomposizione preserva le dipendenze
- la decomposizione ha un join senza perdita.


1) E' dato un file di 134.800 record. Ogni record occupa 257 byte, di cui 57 per la chiave. Un blocco contiene 2048 byte. Un puntatore a blocco occupa 4 byte. Si utilizza una organizzazione hash con record distribuiti uniformemente tra 250 bucket.
3a) Calcolare l'occupazione della bucket directory e dei bucket
3b) Calcolare il costo medio di una ricerca considerando chiavi di hash univoche
3c) Quanti bucket occorrerebbero per avere un costo medio di ricerca minore o uguale a 20 accessi?
