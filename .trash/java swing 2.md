---
sticker: lucide//image
---
### parte uno
formata da **components** e **containers**:
- components: offrono interazioni con l'utente (derivano dalla classe astratta `Component`)
- containers - contengono i components e li posizionano e ridimensionano in base al layout manager
![[java swing frame content.png]]
non possiamo aggiungere componenti al contenitore principale (tranne barra menu), ne serve uno intermedio (content pane)

### parte due: creare un JFrame


```java
package ep2;  
  
import javax.swing.*;  
  
//versione vecchia senza classe separata  
public class TutorialFrameV1 {  
  
    public static void main(String[] args) {  
        //creo finestra  
        JFrame frame = new JFrame("finestra");  
  
        //setto grandezza in pixel  
        frame.setSize(800, 500);  
  
        frame.setVisible(true);  
  
        //angolo alto sx a 200,200 dall'angolo  
        //alto sx del monitor        
        frame.setLocation(200, 200);  
  
        //al centro dello schermo  
        frame.setLocationRelativeTo(null);  
  
        frame.setResizable(false);  
  
        //faccio in modo che il programma finisca di runnare  
        //quando chiudo la finestra
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
  
        //rendo visibile la finestra  
        frame.setVisible(true);  
  
    }  
}
```

---
è preferibile creare un'altra **classe che estende jFrame** dove si crea il jFrame personalizzato.

```java
public class PrimoFrame extends JFrame{  
  
    public PrimoFrame(){  
        super("finestra");  
  
        setSize(800, 500);  
  
        setVisible(true);  
  
        setLocation(200, 200);  
  
        setLocationRelativeTo(null);  
  
        setResizable(false);  
  
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);  
  
        setVisible(true);  
    }
```

### parte tre: aggiungere componenti
è necessario usare un **Layout Manager**

*borderlayout*:
![[borderlayout.png]]

nel costruttore:
`setLayout(new BorderLayout());`

i componenti si possono sia dichiarare come campi, sia creare nel costruttore - la differenza è che, se si dichiarano come campi, verranno creati alla creazione della classe, mentre, se si creano nel costruttore, alla creazione dell'oggetto.

per aggiungere un componente, questo va creato (`textArea = new JTextArea();`) e successivamente aggiunto (`add(textArea, BorderLayout.CENTER);` - va specificato dove va aggiunto)

### parte quattro: action listener
`button.addActionListener` - chiede l'interfaccia ActionListener -> si può implementare nella classe oppure usare una classe anonima che overrida il metodo `actionPerformed`, eseguito ogni volta che il bottone viene premuto:
```java
button.addActionListener(new ActionListener() {  
    @Override  
    public void actionPerformed(ActionEvent e) {  
  
        textArea.append("Testo aggiunto \n");  
  
    }  
});
```

per far sì che, al cliccare del bottone venga aggiunta all'area la scritta del textField (e che esso venga poi resettato):
```java
button.addActionListener(new ActionListener() {  
    @Override  
    public void actionPerformed(ActionEvent e) {  
  
        String testoTextField = textField.getText();  
  
        if (!testoTextField.equals(""))  
            textArea.append(testoTextField + "\n");  
  
        textField.setText("");  
  
    }  
});
```

### parte 5: componenti personalizzati
