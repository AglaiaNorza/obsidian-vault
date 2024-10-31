### cosa vogliamo ottenere?

Quando si decompone uno schema di relazione R su cui è definito un insieme di dipendenze funzionali F, oltre ad ottenere **schemi 3NF** occorre:
- **preservare le dipendenze**
- poter **ricostruire tramite join** tutta e sola l'informazione originaria.

Le dipendenze funzionali che si vogliono preservare sono tutte quelle che sono **soddisfatte da ogni istanza legale di R** - le dipendenze funzionali in $F^+$