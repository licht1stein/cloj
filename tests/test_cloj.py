import pytest

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


def test_take_while(len_50_list):
    res = take_while(lambda x: x <= 30, len_50_list)
    assert res[-1] == 30

    res_2 = take_while(lambda x: x > 100, len_50_list)
    assert res_2 == []


def test_drop_while(len_50_list):
    res = drop_while(lambda x: x >= 40, len_50_list)
    assert res[0] == 40
    assert len(res) == 11


@pytest.mark.parametrize("coll, keys, default, expected", [
    ({"foo": {"bar": "spam"}}, ["foo", "bar"], None, "spam"),
    ({"foo": {"bar": [1, 2, 3]}}, ["foo", "bar", 1], None, 2),
    ({"foo": {}}, ["foo", "bar"], "default", "default"),
    ({"foo": {"bar": [{"spam": 16}, 2, 3]}}, ["foo", "bar", 0, "spam"], None, 16),
    ({"foo": {"bar": [0, {"spam": "target"}, 1]}}, ["foo", "bar", 1, "spam"], None, "target")
])
def test_get_in(coll, keys, default, expected):
    assert get_in(coll, keys, default) == expected
