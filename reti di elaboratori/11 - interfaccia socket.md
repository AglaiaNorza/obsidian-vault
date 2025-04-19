---
created: 2025-04-19T15:53
updated: 2025-04-19T16:50
---

> [!info] paradigma client-server
> Nel paradigma client/server, la comunicazione a livello applicazione avviene tra due programmi applicativi (processi): un client e un server.
> - un **client** è un programma in esecuzione che inizia la comunicazione inviando una richiesta
> - un **server** è un programma che attende le richieste del client

## API
Per sviluppare un programma capace di comunicare con un altro programma, è necessario un nuovo insieme di istruzioni per chiedere ai primi quattro livelli dello stack TCP/IP di aprire la connessione, inviare e/o ricevere dati, e chiudere la connessione. Un insieme di istruzioni di questo tipo viene chiamato **API** (Application Programming Interface).

![[7 - livello trasporto#API di comunicazione]]

## utilizzo dei servizi di livello di trasporto
Una coppia di processi fornisce **servizi** agli utenti di Internet. Per farlo, deve utilizzare i servizi offerti dal livello trasporto per la comunicazione, perché non vi è una comunicazione fisica a livello applicazione.

In particolare, è centrale la scelta tra TCP e UDP, che si basa sul servizio richiesto dall'applicazione.

> [!tip] possibili requisiti delle applicazioni
> - **perdita di dati** ⟶ alcune aplicazioni (es. audio) possono tollerare qualche perdita, altre (es. file transfer) richiedono affidabilità al 100%
> - **temporizzazione** ⟶ alcune applicazioni (es. giochi) richiedono piccoli ritardi, altre (es. posta) non hanno requisiti di temporizzazione
> - **throughput** ⟶ alcune applicazioni (es. multimediali) richiedono un'ampiezza di banda minima, altre ("applicazioni elastiche") utilizzano quella disponibile
> - **sicurezza**

## programmazione con socket 

>[!info] rappresentazione
>
>![[socket-rappr.png|center|500]]

Per poter contattare il server, esso deve essere sempre attivo, e deve aver creato un socket che dia il benvenuto al contatto con il client.

Per contattarlo, il client deve **creare un socket** TCP, specificando l'indirizzo IP e il numero di porta del processo server. A quel punto, il client TCP **stabilisce una connessione** con il server TCP.

Quando viene contattato dal client, il server TCP **crea un nuovo socket** per il processo server per comunicare con il client. Questo permette al server di comunicare con più client (per distinguere i client si utilizzano i numeri di porta d'origine).

>[!info] interazione client/server TCP
>![[interazioneTCP.png|center|400]]

> [!summary] terminologia
> - **flusso** (stream) ⟶ sequenza di caratteri che fluisce verso/da un processo
> - **flusso d’ingresso** (input stream) ⟶ collegato a un’origine di input per il processo ad esempio la tastiera o la socket
> - **flusso di uscita** (output stream) ⟶ collegato a un’uscita per il processo, ad esempio il monitor o la socket
### package java.net
Il package `java.net` fornisce interfacce e classi per l'implementazione di applicazioni di rete:
- le classi `Socket` e `ServerSocket` per le connessioni TCP
- la classe `DatagramSocket` per le connessioni UDP
- la classe `URL` per le connessioni HTTP
- la classe `InetAddress` per rappresentare gli indirizzi Internet
- la classe `URLConnection` per rappresentare le connessioni a un URL
### programmazione socket TCP
![[client-tcp.png|center|300]]

>[!example] esempio di applicazione client-server
>1. Il client legge un riga dall’input standard (flusso `inFromUser`) e la invia al server tramite la socket (flusso `outToServer`)
>2. il server legge la riga dalla socke
>3. il server ver converte la riga in lettere maiuscole e la invia al client
>4. il client legge nella sua socket la riga modificata e la visualizza (flusso `inFromServer`)

**client java**:
```java
//client TCP 
import java.io.*;
import java.net.*;

class TCPClient {
	public static void main(String argv[]) throws Exception {
		String sentence;
		String modifiedSencence;
		
		// crea un flusso d'ingresso
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
		// crea un socket client, connesso al server
		Socket clientSocket = new Socket("hostname", 6789);
		// crea un flusso di uscita collegato al socket
		DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
		// crea un flusso di d'ingresso collegato alla socket
		BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		
		System.out.print("Inserisci una frase: ");
		sentence = inFromUser.readLine();
		
		// invia la frase inserita dall'utente al server
		outToServer.writeBytes(sentence + '\n');
		// legge la risposta dal server
		modifiedSentence = inFromServer.readLine();
		
		System.out.println("FROM SERVER: " + modifiedSentence);
		
		// chiude socket e connessione con server
		clientSocket.close();
	}
}
```

**server java**:
```java 
//server TCP
import java.io.*;
import java.net.*;

class TCPServer {
	public static void main(String argv[]) throws Exception {
		String clientSentence;
		String capitalizedSentence;
		
		// crea un socket di benvenuto sulla porta 6789
		ServerSocket welcomeSocket = new ServerSocket(6789);
		while(true) {
			// attende, sul socket di benvenuto, un contatto dal client
			Socket connectionSocket = welcomeSocket.accept();
			// crea un flusso d'ingresso collegato al socket
			BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
			// crea un flusso di uscita collegato al socket
			DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
			
			// legge la riga dal socket
			clientSentence = inFromClient.readLine();
			capitalizedSentence = clientSentence.toUpperCase() + '\n';
			
			// scrive la riga sul socket
			outToClient.writeBytes(capitalizedSentence);
		}
	}
}
```

### programmazione socket UDP 
Con UDP, non c'è connessione tra client e server:
- non c'è handshaking
- il mittente allega esplicitamente ad ogni pacchetto indirizzo IP e porta di destinazione
	- il server deve estrarli dal pacchetto ricevuto

![[client-udp.png|center|400]]

**client java**:
```java
//client UDP
import java.io.*;
import java.net.*;

class UDPClient {
	public static void main(String args[]) throws Exception {
		// crea un flusso di ingresso
		BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
		// crea un socket client
		DatagramSocket clientSocket = new DatagramSocket();
		// traduce il nome dell'host nell'indirizzo IP usando DNS
		InetAddress IPAddress = InetAddress.getByName("hostname");
		
		byte[] sendData = new byte[1024];
		byte[] receiveData = new byte[1024];
		String sentence = inFromUser.readLine();
		
		sendData = sentence.getBytes();
		
		// crea il datagramma con i dati da trasmettere, lunghezza
		// indirizzo IP e porta
		DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, 9876);
		// invia il datagramma al server
		clientSocket.send(sendPacket);
		// crea il datagramma con i dati da ricevere, lunghezza
		// indirizzo IP e porta
		DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
		// legge il datagramma dal server
		// il client rimane inattivo fino a quando riceve un pacchetto
		clientSocket.receive(receivePacket);
		
		String modifiedSentence = new String(receivePacket.getData());
		System.out.println("FROM SERVER:" + modifiedSentence);
		clientSocket.close();
```

**server java**:
```java
//server UDP
import java.io.*;
import java.net.*;

class UDPServer {
	public static void main(String args[]) throws Exception {
		// crea un socket per datagrammi sulla porta 9876
		DatagramSocket serverSocket = new DatagramSocket(9876);
		
		byte[] receiveData = new byte[1024];
		byte[] sendData = new byte[1024];
		
		while(true) {
			// crea lo spazio per i datagrammi
			DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
			// riceve i datagrammi
			serverSocket.receive(receivePacket);
			
			String sentence = new String(receivePacket.getData());
			
			// ottiene indirizzo IP e numero di porta del mittente
			InetAddress IPAddress = receivePacket.getAddress();
			int port = receivePacket.getPort();
			
			String capitalizedSentence = sentence.toUpperCase();
			sendData = capitalizedSentence.getBytes();
			
			// crea il datagramma da inviare al client
			DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);
			// scrive il datagramma sulla socket
			serverSocket.send(sendPacket);
		}
	}
}
```