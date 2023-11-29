dati dei punti che formano i rettangoli, disegnare il minimo rettangolo che li contiene tutti

minimo e massimo delle coordinate x e y.
```python
list_rect = [(210, 210, 210, 210 ,(255, 0, 0)),
             (50, 100, 100, 200, (255, 255, 0)),
             (220, 50, 250, 99, (255, 0, 255)),
             (150, 80, 150, 190, (0, 128, 0))
             ]

m, M = list(zip(*map(lambda *items: (min(items), max(items)), *list_rect)))
#prende il minimo e il massimo di ogni colonna
#map itera 5 volte
#prima iterazione:items sono i valori della colonna1, poi della colonna2...


```
