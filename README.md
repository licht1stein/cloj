# Clojure inspired helper functions

This is a small library with Clojure inspired helper functions. It uses only the standard library, without any external dependencies.

The goal is to implement replicas of the Clojure funcs that I find useful.

Implemented:
* take/drop
* some
* nth, first, second, third, fourth, fifth, forty_second, last

Some examples:

```python
from cloj import take, drop

take(3, [1, 2, 3, 4, 5])
>> [1, 2, 3]

drop(3, [1, 2, 3, 4, 5])
>> [4, 5]

drop (100, [1, 2, 3, 4, 5])
>> []
```

```python
from cloj import first, second, third, fourth, fifth, forty_second, last

first([1, 2, 3])
>> 1

last([1, 2, 3])
>> 3

first([])
>> None
```
