'''Unit Tests'''
import pytest

from .solution import solution_1, solution_2

@pytest.fixture
def input_data():
    return """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".rstrip("\n")

def test_solution_1(input_data):
    print(input_data)
    assert 95437 == solution_1(input_data)

def test_solution_2(input_data):
    print(input_data)
    assert 1 == solution_2(input_data)
