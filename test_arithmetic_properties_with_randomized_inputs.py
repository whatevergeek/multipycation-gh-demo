from arithmetic import *
import pytest
from hypothesis import given, settings
import hypothesis.strategies as st

@given(st.integers(), st.integers())
@settings(max_examples=200)
def test_commutative_property(factor1, factor2):
    assert multiply(factor1,factor2) == multiply(factor2,factor1)    

@given(st.integers().filter(lambda x: x > 0), st.integers(), st.integers())
def test_associative_property(factor1, factor2, factor3):
    assert multiply(multiply(factor1, factor2), factor3) == multiply(factor1, multiply(factor2,factor3))

@given(st.integers())
def test_identity_property(factor1):
    assert multiply(factor1,1) == factor1 

@given(st.integers(), st.integers(), st.integers())
def test_distributive_property(num1, num2, num3):
    assert multiply(num1,(num2 + num3)) == multiply(num1,num2) + multiply(num1,num3)
