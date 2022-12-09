'''Unit Tests'''
import pytest

from .solution import solution_1, solution_2, control_b, Thing

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
""".lstrip("\n")

def test_control_b():
    thing_a = Thing(0,0,"1")
    thing_b = Thing(0,0,"2")
    thing_a_moves = [
        ("R", 4),
        ("U", 4),
    ]
    expected_b_positions = [
        (0,0),
        (0,0),
        (1,0),
        (2,0),
        (3,0), # end ("R", 4)
        (3,0),
        (4,1),
        (4,2),
        (4,3), # end ("U", 4)
    ]
    b_positions = [thing_b.position()]
    for move, steps in thing_a_moves:
        for _ in range(steps):
            thing_a.move(move)
            control_b(thing_b, thing_a.position())
            b_positions.append(thing_b.position())

    assert expected_b_positions == b_positions
        
            
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
""".lstrip("\n")
    assert 36 == solution_2(input_data)