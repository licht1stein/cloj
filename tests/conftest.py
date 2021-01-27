import pytest


@pytest.fixture
def empty_list():
    return []


@pytest.fixture
def len_50_list():
    lst = list(range(1, 51))
    assert len(lst) == 50
    return lst
