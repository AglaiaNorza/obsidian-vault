


`random()` non ci piace

### generare numeri casuali:
1) istanzia random device

```Cpp
std::random_device device_randomness_source
```

2) usalo per generare un seed
```Cpp
auto seed = device_randomness_source();
```
- (`auto` detecta il type)
3) fai una random engine (generatori di numeri random)
```Cpp
std::default_random_engine pseudo_random_engine(seed);
```




```

```
