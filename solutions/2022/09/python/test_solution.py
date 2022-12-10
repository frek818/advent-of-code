"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2, Knot


@pytest.fixture
def input_data():
    return """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".lstrip(
        "\n"
    )


def test_solution_1(input_data):
    assert 13 == solution_1(input_data)


def test_solution_2(input_data):
    assert 1 == solution_2(input_data)


def test_solution_2_second():
    input_data = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".lstrip(
        "\n"
    )
    assert 36 == solution_2(input_data)
