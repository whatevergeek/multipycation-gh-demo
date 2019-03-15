from arithmetic import *
import pytest

@pytest.mark.parametrize("factor1, factor2", [
    (2, 3),
    (4, 5),
])
def test_commutative_property(factor1, factor2):
    assert multiply(factor1,factor2) == multiply(factor2,factor1)    

@pytest.mark.parametrize("factor1, factor2, factor3", [
    (2, 3, 4),
    (4, 5, 6),
])
def test_associative_property(factor1, factor2, factor3):
    assert multiply(multiply(factor1, factor2), factor3) == multiply(factor1, multiply(factor2,factor3))

@pytest.mark.parametrize("factor1", [2,4])
def test_identity_property(factor1):
    assert multiply(factor1,1) == factor1

@pytest.mark.parametrize("factor1", [
    i for i in range(1, 101)
])
def test_identity_property(factor1):
    assert multiply(factor1,1) == factor1

@pytest.mark.parametrize("num1, num2, num3", [
    (2, 3, 4),
    (4, 5, 6),
])
def test_distributive_property(num1, num2, num3):
    assert multiply(num1,(num2 + num3)) == multiply(num1,num2) + multiply(num1,num3)
