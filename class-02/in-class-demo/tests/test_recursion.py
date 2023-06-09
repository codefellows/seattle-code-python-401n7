import pytest
from recursion_package.recursion_module import factorial


# @pytest.mark.skip()
def test_factorial_exists():
    assert factorial


def test_factorial_one():
    actual = factorial(1)
    expected = 1
    assert actual == expected


# What's a factorial?
# factorial of 3:
# 3 * 2 * 1 = 6
def test_factorial_three():
    actual = factorial(3)
    expected = 6
    assert actual == expected


# factorial of 4:
# 4 * 3 * 2 * 1 = 24
def test_factorial_four():
    actual = factorial(4)
    expected = 24
    assert actual == expected


def test_factorial_default():
    actual = factorial()
    expected = 24
    assert actual == expected
