"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2


@pytest.mark.parametrize(
    ("input_data", "expected_result"),
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ),
)
def test_solution_1(input_data, expected_result):
    assert expected_result == solution_1(input_data)


@pytest.mark.parametrize(
    ("input_data", "expected_result"),
    (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ),
)
def test_solution_2(input_data, expected_result):
    assert expected_result == solution_2(input_data)
