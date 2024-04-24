#### Predicate\<T>
funzione a valori booleani a un solo argomento generico T

| Modifier and Type         | Method                                                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default Predicate<T>`    | **`and(Predicate<? super T> other)`**  <br>Returns a composed predicate that represents a short-circuiting logical AND of this predicate and another |
| `static <T> Predicate<T>` | **`isEqual(Object targerRef)`**  <br>Returns a predicate that tests if two arguments are equal according to `Object.equals(Object, Object)`          |
| `default Predicate<T>`    | **"`negate()`**  <br>Returns a predicate that represents the logical negation of this predicate                                                      |
| `default Predicate<T>`    | **`or(Predicate<? super T> other)`**  <br>Returns a composed predicate that represents a short-circuiting logical OR of this predicate and another   |
| `boolean`                 | **`test(T t)`**  <br>Evaluates this predicate on the given argument                                                                                  |

```java
Predicate<String> predicate = s-> s.length() > 0;

Predicate<String> predicate2 = s-> s.startsWith("f")
```

esiste anche `BiPredicate`, con due valori in input.
```java
BiPredicate<String, Integer> bp2_4_3 = (s, i) -> s.length() == i;
```

- `Function<T, R>` - argomenti T d'ingresso e R di ritorno entrambi generici
```java
Function<String, Integer> toInteger = Integer::valueOf;
```

- `Supplier<T>` - funzione senza argomenti in input

```java
Supplier<String> stringSupplier = () -> "ciao";

Supplier<Person> personSupplier = Person::new;
personSupplier.get(); // new Person();
```

- `Consumer<T>` - argomento di tipo generico T e nessun tipo di ritorno
```java
Consumer<Person> greeter1 = p-> System.out.println("hello"+p);
```