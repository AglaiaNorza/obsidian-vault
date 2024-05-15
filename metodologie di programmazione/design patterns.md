---
sticker: lucide//pencil
---
## MVC
- **model** - dati e metodi che si usano per lavorarci
- **view** - interfaccia
- **controller** - coordina le interazioni tra view e model

- in Main istanzio un Frame
- Frame crea la finestra, aggiunge i vari componenti dentro e ha i listener degli eventi che poi vengono mandati al controller per updateare il model
- Controller aspetta che il Frame gli passi qualcosa e updatea il "Database", permette anche di fare il getter dal DB
- nel model ci stanno tutte quelle cose che contengono dati
## singleton
- costruttori privati
- getInstance