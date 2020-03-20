- Favor Object Composition over Class Inheritance means you can use inheritance but should use composition from the beginning if possible.

- There are 2 mechanisms of code reuse:-

1. White-Box Reuse --> Class Inheritance
2. Black-Box Reuse --> Object Composition

It is prefer to use black-box. Black-Box usually means that you have your object, you only see the external part which happens to be the interface and the internal details of implementation is
something that is actually kept as a secret not because we don't want people to know how it's done but it's irrelevant on how we all the information that we need to know in order to use the
object successfully.
ex-> if we drive a car we don't need to be some sort of mechanical engineer wizard to know how internal car actually works, we can just basically interacts with the interface of the car.


Inheritance does have its advantages:-

1. Easy way to reuse code.
2. Allows changing inherited implementation -> Derived classes either add the behavior that doesn't exist in Parent class or modify the behavior of Parent Class.


Disadvantages of Inheritance:-

1. The relation between a base class and a derived class is statically fixed  --> this is really not true in Python as Python is dynamic in nature so it is possible to actually create some
inheritance relationships at runtime that are decided at the very moment.
2. Inheritance supports weak encapsulation and fragile structures.
3. A Derived class inherits everything even things it doesn't need or want.
4. Changes in a base class interface impact all its derived classes.




