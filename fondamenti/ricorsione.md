si basa su <span style="color:#32a9b8">stack</span> e <span style="color:#32a9b8">queue</span>
##### queue
principio "first in first out"
- enqueue() - come append
- dequeue() - come pop(0)
##### stack
![[Screen Shot 2023-11-28 at 17.45.54.png]]
principio "last in first out"
call_c è la prima ad "uscire", e il risultato viene passato a call_b

usa:
- push()
- pop()

###### fibonacci
```python
def fibonacci(n):
	if n<2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
```

così però fa molto lavoro - sviluppa ogni sottoalbero prima di tornare indietro.

