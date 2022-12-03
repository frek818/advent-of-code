"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2


@pytest.fixture
def input_data():
    return """
A Y
B X
C Z
""".rstrip()


def test_solution_1(input_data):
    assert 15 == solution_1(input_data)


def test_solution_2(input_data):
    assert 12 == solution_2(input_data)
