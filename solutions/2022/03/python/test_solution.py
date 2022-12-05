"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2, item_value


@pytest.fixture
def input_data():
    return """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


@pytest.mark.parametrize(
    ("item", "expected_point_value"),
    (
        ("a", 1),
        ("z", 26),
        ("A", 27),
        ("Z", 52),
    ),
)
def test_item_value(item, expected_point_value):
    assert expected_point_value == item_value(item)


def test_solution_1(input_data):
    assert 157 == solution_1(input_data)


def test_solution_2(input_data):
    assert 70 == solution_2(input_data)
