"""Unit Tests"""
import pytest

from .solution import solution_1, solution_2
from .computer import cycle_to_coords, CRT, Sprite


def f(sheet: str):
    return "".join(sheet.splitlines())


@pytest.fixture
def input_data():
    return """
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".lstrip(
        "\n"
    )


def ttest_solution_1(input_data):
    assert 13140 == solution_1(input_data)


def test_sprite():
    sprite = Sprite(3, 1)
    assert sprite.is_covering_position(0)
    assert sprite.is_covering_position(1)
    assert sprite.is_covering_position(2)
    assert not sprite.is_covering_position(3)
    assert not sprite.is_covering_position(4)


def test_crt():
    sprite = Sprite(3, 1)
    crt = CRT(40, 6, sprite)
    crt.set_position_sprite(1)

    assert sprite.is_covering_position(0)
    assert sprite.is_covering_position(1)
    assert sprite.is_covering_position(2)
    assert not sprite.is_covering_position(3)
    assert not sprite.is_covering_position(4)

    crt.draw(1)
    assert crt.paint()[0] == "#"
    crt.draw(2)
    assert crt.paint()[1] == "#"
    crt.draw(3)
    assert crt.paint()[2] == "#"

    crt.set_position_sprite(16)

    crt.draw(4)
    assert crt.paint()[3] == "."

    crt.set_position_sprite(5)

    crt.draw(5)
    assert crt.paint()[4] == "#"


def test_solution_2(input_data):
    expected = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""".lstrip(
        "\n"
    )
    assert expected == solution_2(input_data)


@pytest.mark.parametrize(
    ("cycle", "width", "expected"),
    [
        (1, 40, (0, 0)),
        (40, 40, (39, 0)),
        (41, 40, (0, 1)),
    ],
)
def test_cycle_to_coords(cycle, width, expected):
    assert expected == cycle_to_coords(cycle=cycle, width=width)
