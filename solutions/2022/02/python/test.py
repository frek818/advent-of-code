"""Unit Tests"""
from solution import solution_1, solution_2


def test_solution_1():
    input_data = """
A Y
B X
C Z
""".rstrip()
    assert 15 == solution_1(input_data)


def test_solution_2():
    input_data = """
A Y
B X
C Z
""".rstrip()
    assert 12 == solution_2(input_data)
