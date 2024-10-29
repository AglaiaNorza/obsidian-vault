#### optional
`java.util.Optional` è un contenitore di un riferimento che potrebbe essere o non essere null.
- un metodo può restituire un `Optional` invece di restituire un riferimento potenzialmente null.
- serve a evitare i `NullPointerException`

>[!Info] creare e verificare:
>un Optional *senza riferimento* (contenitore vuoto):
>- `Optional.empty()`
> 
>un Optional *non nullo*:
>- `Optional.of("bumbumghigno")`
> 
>un Optional di un riferimento che *può non essere nullo*:
>-  `Optional<String> optional = Optional.ofNullable(s);`
> 
> controllo della presenza di un valore non null:
> - `Optional.of("...").isPresent()`

>[!Tip] ottenere il valore di un Optional
>mediante **orElse**:
>- `Optional<String> op = Optional.of("eccomi") op.orElse("fallback")`

