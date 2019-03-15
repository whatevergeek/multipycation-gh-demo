from arithmetic import *
import pytest

def test_example1():
    actual_output = multiply(2,3)
    expected_output = 6
    assert actual_output == expected_output

def test_example2():
    actual_output = multiply(4,5)
    expected_output = 20
    assert actual_output == expected_output

@pytest.mark.parametrize("factor1, factor2, expected_output", [
    (2, 3, 6),
    (4, 5, 20),
])
def test_example2and3(factor1, factor2, expected_output):
    actual_output = multiply(factor1,factor2)
    assert actual_output == expected_output    
