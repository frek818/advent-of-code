"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2, Stack, Procedure, parse_procedures


@pytest.fixture
def input_data():
    return """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".lstrip(
        "\n"
    )


def test_solution_1(input_data):
    assert "CMZ" == solution_1(input_data)


def test_solution_2(input_data):
    assert "MCD" == solution_2(input_data)
