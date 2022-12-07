'''Unit Tests'''
import pytest

from .solution import solution_1, solution_2, get_full_path_string, Directory, File, get_full_path_nodes


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
""".lstrip("\n")


def test_get_full_path_nodes():
    root = Directory("/", parent=None)
    assert [root] == get_full_path_nodes(root)
    sub_1 = Directory("sub_1", parent=root)
    assert [root, sub_1] == get_full_path_nodes(sub_1)


def test_get_full_path_string():
    root = Directory("/", parent=None)
    assert "" == get_full_path_string(root)
    sub_1 = Directory("sub_1", parent=root)
    assert "sub_1" == get_full_path_string(sub_1)
    sub_2 = Directory("sub_2", parent=sub_1)
    assert "sub_1/sub_2" == get_full_path_string(sub_2)


def test_solution_1(input_data):
    assert 95437 == solution_1(input_data)


def test_solution_2(input_data):
    assert 24933642 == solution_2(input_data)
