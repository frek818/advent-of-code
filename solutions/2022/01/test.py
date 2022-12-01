'''Unit Tests'''
from solution import solution_1


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
