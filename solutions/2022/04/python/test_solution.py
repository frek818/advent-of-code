'''Unit Tests'''
import pytest

from .solution import solution_1, solution_2

@pytest.fixture
def input_data():
    return """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()

def test_solution_1(input_data):
    assert 2 == solution_1(input_data)

def test_solution_2(input_data):
    assert 4 == solution_2(input_data)
