'''Unit Tests'''
import pytest

from solution import solution_1, solution_2, parse_elves_calories

@pytest.fixture
def input_data():
    return """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".rstrip()

def test_parse_elves_calories(input_data):
    assert 5 == len(parse_elves_calories(input_data))

def test_solution_1(input_data):
    assert 24000 == solution_1(input_data)

def test_solution_2(input_data):
    assert 45000 == solution_2(input_data)