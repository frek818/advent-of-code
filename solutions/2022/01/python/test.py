'''Unit Tests'''
from solution import solution_1, solution_2, parse_elves_calories

def test_parse_elves_calories():
    input_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".rstrip()
    assert 5 == len(parse_elves_calories(input_data))


def test_solution_1():
    input_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".rstrip()
    assert 24000 == solution_1(input_data)

def test_solution_2():
    input_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".rstrip()
    assert 45000 == solution_2(input_data)