---
sticker: lucide//folder-closed
---
- un file è una *collezione di dati* salvata su supporto di memorizzazione di massa.
- non è parte del codice sorgente di un programma
- il programma deve conoscere il formato dei dati nel file
- è importante distinguere tra *file di testo* e *file binari*

>[!Info]- tipi di file
>**file di testo**
>- contiene linee di testo, che terminano con un carattere newline (`\n`) o con un carriage return (`\r`) concatenato con una nuova linea
> 
>**file binari**
>- contiene qualsiasi informazione come concatenazione di byte
>- diversi programmi potrebbero interpretare lo stesso file in modo diverso

#### stream
astrazioni derivate da dispositivi di i/o sequenziale.
- uno stream di input *riceve uno stream di caratteri* "uno alla volta"
- uno stream di output *produce uno stream di caratteri*
- un file può essere trattato come uno stream di input o output

>[!info] classi per leggere/scrivere
>- per **caratteri**:
>	- `java.io.Reader` / `java.io.Writer`
>- per **byte**
>	- `java.io.InputStream` / `java.io.OutputStream`
>- per **file di testo**
>	- `java.util.Scanner` (più lenta perché più potente)

