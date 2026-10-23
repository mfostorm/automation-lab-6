import pytest

from app import order_total


def test_without_discount():
    assert order_total([100, 200]) == 300


def test_with_discount():
    assert order_total([1990, 2490, 890], 10) == 4833.0


def test_empty_order():
    assert order_total([]) == 0


def test_wrong_discount():
    with pytest.raises(ValueError):
        order_total([100], 150)
