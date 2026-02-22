import pytest


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def test_add_positive():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, 2) == 1


@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected
