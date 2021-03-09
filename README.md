# Clojure inspired helper functions for Python

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cloj)
![PyPI - License](https://img.shields.io/pypi/l/cloj)
![PyPI](https://img.shields.io/pypi/v/cloj?color=blue)

This is a small library with Clojure inspired helper functions. It uses only the standard library, without any external dependencies.

The goal is to implement replicas of the Clojure funcs that I admire.

## Installation

With [poetry](https://python-poetry.org/) (always recommended):
```bash
poetry add cloj
```

With pip:
```bash 
pip install cloj
```

Implemented:
* take/drop
* take_while/drop_while
* some
* nth, first, second, third, fourth, fifth, forty_second, last
* get-in

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

```python
from cloj import get_in

sample = {"foo": {"bar": [0, {"spam": "target"}, 1]}}
get_in(sample, ["foo", "bar", 1, "spam"])
>>> "target"
```
