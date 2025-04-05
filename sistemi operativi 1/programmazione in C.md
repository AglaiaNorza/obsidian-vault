---
created: 2025-04-05T19:49
updated: 2025-04-05T20:10
---
# introduzione

## ambiente di sviluppo ed esecuzione
Le fasi di *sviluppo* di un programma C sono quattro (ognuna svolta da un programma diverso):
1) il programmatore scrive un programma in un *editor di testo* e lo salva su disco
2) il **pre-processore** processa il codice
3) il **compilatore** compila il codice producendo un **file oggetto**, e lo salva su disco
4) il **linker** collega il file oggetto alle librerie, e crea un file eseguibile

>[!tip] Il programma **gcc** (Gnu Compiler Collection) è in grado di svolgere tutte le fasi necessarie alla creazione di un file eseguibile.

Le fasi di *esecuzione* sono invece:
5) il **loader** preleva il programma dal disco e lo carica in memoria principale
6) la **CPU** prende ogni istruzione e la esegue, salvando in memoria,se necessario, nuovi dati durante l'esecuzione 

