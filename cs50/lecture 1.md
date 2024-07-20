### generic simple stuff

>[!tip] how to write, compile and run
>```C
>code hello.c
>make hello
>./hello
>```

- to include a library - `#include <stdio.h

- comment syntax `//`

- variables need to be **declared**
- some functions (like `printf`) need *format codes:

| format code | used for                   |
| ----------- | -------------------------- |
| %d / %i     | decimal integer            |
| %f          | float                      |
| %lf / %li   | long double / long integer |
| %c          | character                  |
| %s          | string                     |
| %p          | pointer                    |

-  **conditionals** follow this syntax:

```C
if(x<y){
	//code
} else if (x>y){
	//code
} else {
	//code
}
```

- **loops** follow this syntax:

```C
while(i<5){
	//code
}

for(int i=0; i<5; i++){
	//code
}
```

### functions

>[!important] function prototypes
> in C, before being able to use a function, i need to declare its *prototype* just like a variable
> 
> ```C
> void function(int x);
> 
> void function(int x){
> }
>```

- **syntax**
```
return name(type parameter){}
```


### types

- `bool`
- `char`
- `double`
- `float`
- `int`
- `long`
- `string`
