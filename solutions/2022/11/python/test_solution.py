"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2, parse_operation


@pytest.fixture
def input_data():
    return """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip(
        "\n"
    )


def test_solution_1(input_data):
    assert 10605 == solution_1(input_data)


def test_solution_2(input_data):
    assert 2713310158 == solution_2(input_data)


@pytest.mark.parametrize(
    ("line", "input_value", "expected"),
    [
        ("Operation: new = old * old", 2, 4),
        ("Operation: new = old * 7", 2, 14),
        ("Operation: new = old + 3", 2, 5),
    ],
)
def test_parse_operation(line, input_value, expected):
    assert expected == parse_operation(line)(input_value)
