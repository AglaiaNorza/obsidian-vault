ci sono tre macrocategorie di IO:
- leggibili da utente - leggibili dall'utente
- leggibili dalla macchina - comunicazione con materiale elettronico (es. dischi, USB)
- di comunicazione (input: tastiera, mouse, output: scheda di rete)

è importante notare che sono molto diversi tra loro, il che causa problemi al sistema: bisogna gestirli tutti e pensare come tener conto delle diversità

### funzionamento
in generale, i dispositivi di input hanno un sistema che permette al Sistema Operativo di interrogarli per un valore che identifica l'input

In generale, un processo che effettua una syscall su IO vuole leggere quel tipo di dato:
- al processo non interessa che tipo di macchina sia, ma solo il valore

Un dispositivo output prevede di poter cambiare il valore di una certa grandezza fisica al suo interno


Il kernel si interpone tra processo utente e dispositivo fisico 


driver - moduli di sistema che implementano delle funzionalità specifiche in base al dispositivo

a trasferimento completato arriva l'interrupt (si termina l'operazione e il processo ritorna ready)
- ci possono essere dei problemi: es. un disco si è smagnetizzato