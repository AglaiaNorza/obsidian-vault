> [!info]- index
> - [[#Predicate\<T>|Predicate\<T>]]
> - [[#Function\<T, R>|Function\<T, R>]]
> - [[#Supplier\<T>|Supplier\<T>]]
> - [[#Consumer\<T>|Consumer\<T>]]
> - [[#Comparator|Comparator]]


#### Predicate\<T>
funzione a *valori booleani* a un solo argomento generico T
(in un certo senso controlla qualcosa)

| Modifier and Type         | Method                                                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default Predicate<T>`    | **`and(Predicate<? super T> other)`**  <br>Returns a composed predicate that represents a short-circuiting logical AND of this predicate and another |
| `static <T> Predicate<T>` | **`isEqual(Object targerRef)`**  <br>Returns a predicate that tests if two arguments are equal according to `Object.equals(Object, Object)`          |
| `default Predicate<T>`    | **`negate()`**  <br>Returns a predicate that represents the logical negation of this predicate                                                       |
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

#### Function\<T, R>
argomenti T d'ingresso e R di ritorno entrambi generici

| Modifier and Type           | Method                                                                                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `default <V> Function<T,V>` | **`andThen(Function<? supper R,? extends V> after)`**  <br>Returns a composed function that first applies this function to its input, and then applies the `after` function to the result. |
| `R`                         | **`apply(T t)`**  <br>Applies this function to the given argument                                                                                                                          |
| `default <V> Function<V,R>` | **`compose(Function<? super V,? extends T> before`**  <br>Returns a composed function that first applies the `before` function to its input, and then applies this function to the result. |
| `static <T> Function<T,T>`  | **`identify()`**  <br>Returns a function that always returns its input arguments                                                                                                           |


```java
Function<String, Integer> toInteger = Integer::valueOf;
```

#### Supplier\<T>
funzione senza argomenti in input

```java
Supplier<String> stringSupplier = () -> "ciao";

Supplier<Person> personSupplier = Person::new;
personSupplier.get(); // new Person();
```

#### Consumer\<T>
argomento di tipo generico T e nessun tipo di ritorno
```java
Consumer<Person> greeter1 = p-> System.out.println("hello"+p);
```

#### Comparator
[[strutture dati#ordinamento naturale]]
