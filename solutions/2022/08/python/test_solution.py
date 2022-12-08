'''Unit Tests'''
import pytest

from .solution import solution_1, solution_2

@pytest.fixture
def input_data():
    return """
30373
25512
65332
33549
35390
""".lstrip("\n")

def test_solution_1(input_data):
    assert 21 == solution_1(input_data)

def test_solution_2(input_data):
    print(input_data)
    assert 1 == solution_2(input_data)
