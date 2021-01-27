import functools
from collections import Callable, Iterable, Sized
from contextlib import suppress


def some(fn: Callable, collection: Iterable):
    for i in collection:
        result = fn(i)
        if result:
            return result


def nth(i: int, collection: Sized):
    with suppress(IndexError):
        return collection[i]


first = functools.partial(nth, 0)
second = functools.partial(nth, 1)
third = functools.partial(nth, 2)
fourth = functools.partial(nth, 3)
fifth = functools.partial(nth, 4)
forty_second = functools.partial(nth, 41)
last = functools.partial(nth, -1)


def take(n, coll):
    return coll[:n]


def drop(n, coll):
    return coll[n:]


def take_while(fn: Callable, coll):
    last_index = None
    for i, item in enumerate(coll):
        if not fn(item):
            last_index = i
            break
    if last_index:
        return coll[:last_index]
    return drop(len(coll) + 1, coll)


def drop_while(fn: Callable, coll):
    keep_index = None
    for i, item in enumerate(coll):
        if fn(item):
            keep_index = i
            break
    if not keep_index:
        return drop(len(coll) + 1, coll)
    return coll[keep_index:]
