"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2, actual_index


@pytest.fixture
def input_data():
    return """
30373
25512
65332
33549
35390
""".lstrip(
        "\n"
    )


def test_index_flipper():
    assert [2, 1] == actual_index([0, 1], 3, "right")
    assert [4, 3] == actual_index([0, 1], 5, "right")


def test_solution_1(input_data):
    assert 21 == solution_1(input_data)


def test_solution_2(input_data):
    assert 8 == solution_2(input_data)
