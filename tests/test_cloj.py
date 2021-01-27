from cloj import *


def test_nth__empty(empty_list):
    for i in range(100):
        assert nth(i, empty_list) is None


def test_nth__len_50(len_50_list):
    for i in range(50):
        assert nth(i, len_50_list) == len_50_list[i]
    for i in range(51, 100):
        assert nth(i, len_50_list) is None


def test_partials(len_50_list):
    partials = "first second third fourth fifth".split()
    for i, name in enumerate(partials):
        assert eval(name)(len_50_list) == len_50_list[i]
    assert forty_second(len_50_list) == len_50_list[41]
    assert last(len_50_list) == len_50_list[-1]
