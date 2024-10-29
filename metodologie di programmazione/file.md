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

### stream
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

#### leggere
 
>[!Tip] metodi dell'interfaccia reader
![[metodi reader java.png|center|500]]

##### BufferedReader
`BufferedReader` permette una lettura bufferizzata dei caratteri forniti da `FileReader`
 
```java
BufferedReader br = null;
try
{
	br = new BufferedReader(new FileReader(filename));
	while(br.ready())
	{
		String line = br.readLine();
		//...
	}
	catch(IOException e)
	{
		//gestione eccezione
	}
	finally
	{
		if (br != null)
			try {br.close();} catch(IOException e) { /*gestione*/}
	}
}
```

##### try with resources
è possibile specificare tra le parentesi dopo `try` un elenco di istruzioni separate da `;` che definiscono le **risorse da chiudere automaticamente**

```java
try(BufferedReader br = new BufferedReader(new FileReader(fileName)); 
	BufferedReader br2 = new BufferedReader(new FileReader(fileName2)))
{
	while(br.ready()){
		String line = br.readLine();
	}
}
catch(IOException e) {}
```

##### chiudere automaticamente uno stream
è possibile per tutti gli oggetti di classi che implementano `java.lang.Autoclosable` (estesa dall'interfaccia `java.io.Closeable`)

```java
public interface AutoCloseable
{
	void close() throws Exception;
}
```

#### scrivere

>[!Tip] metodi dell'interfaccia Writer
>![[metodi java writer.png|center|500]]
 

