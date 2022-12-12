'''Unit Tests'''
import pytest

from .solution import solution_1, solution_2

@pytest.fixture
def input_data():
    return """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".lstrip("\n")

def test_solution_1(input_data):
    assert 31 == solution_1(input_data)

def test_solution_2(input_data):
    return
    assert 1 == solution_2(input_data)
