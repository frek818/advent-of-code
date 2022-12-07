"""
Day 7: No Space Left On Device
"""
from typing import List, Union

from aocd.models import Puzzle


class Node:
    def __init__(self, name: str, parent: "Node"):
        self._name = name
        self._parent = parent

    @property
    def name(self):
        return self._name

    def size(self):
        raise NotImplemented()

    def parent(self):
        return self._parent


class File(Node):
    def __init__(self, name: str, size: str, parent: "Directory"):
        self._size = size
        super().__init__(name=name, parent=parent)

    def size(self): return self._size


class Directory(Node):
    def __init__(self, name: str, parent: "Directory",
                 children: List[Union["Directory", File]] = None):
        self._children = [] if children is None else children
        super().__init__(name=name, parent=parent)
        self._cached_size = None
        self._cached_current_path = None

    def add_child(self, child: Union["Directory", File]):
        self._children.append(child)

    def size(self) -> int:
        if self._cached_size is None:
            self._cached_size = sum([child.size() for child in self._children])
        return self._cached_size

    @property
    def children(self):
        return self._children

    def get_children_recursively(self) -> List[Union["Directory", File]]:
        items = []
        for child in self._children:
            items.append(child)
            if isinstance(child, Directory):
                items.extend(child.get_children_recursively())
        return items


class FileSystem:
    def __init__(self, root: Directory = None):
        if root:
            assert root.parent() is None, "Root of file system should not have a parent"
        else:
            root = Directory("/", parent=None)

        self._root = root
        self._current_directory = root
        self._index = {"/": root}

    def cd(self, new_path: str):
        if new_path == "/":
            self._current_directory = self._root
        elif new_path == "..":
            if self._current_directory.parent() is None:
                return
            self._current_directory = self._current_directory.parent()
        else:
            index_key = self._generate_index_key(new_path)
            self._current_directory = self._index.get(index_key)

    def _generate_index_key(self, new_path) -> str:
        if self.current_path_string() == "":
            index_key = new_path
        else:
            index_key = self.current_path_string() + "/" + new_path
        return index_key

    def ls(self, path="/", recursive=False) -> List[Union["Directory", File]]:
        item = self._index.get(path)
        return item.get_children_recursively() if recursive else item.children

    def current_path_string(self) -> str:
        if not self._current_directory._cached_current_path:
            self._current_directory._cached_current_path = get_full_path_string(self._current_directory)
        return self._current_directory._cached_current_path

    def make_dir(self, dirname):
        index_key = self._generate_index_key(dirname)
        new_dir = Directory(name=dirname, parent=self._current_directory)
        self._current_directory.add_child(new_dir)
        self._index[index_key] = new_dir

    def make_file(self, name: str, size: int):
        index_key = self._generate_index_key(name)
        new_file = File(name=name, size=size, parent=self._current_directory)
        self._current_directory.add_child(new_file)
        self._index[index_key] = new_file

    def size(self) -> int:
        return self._root.size()


def get_full_path_nodes(path: Node):
    if path is None:
        return []
    return get_full_path_nodes(path.parent()) + [path]


def get_full_path_string(node: Node):
    path_nodes = get_full_path_nodes(node)
    return "/".join([part.name for part in path_nodes[1:]])


def create_filesystem(input_data):
    filesystem = FileSystem()
    for line in input_data.split("\n"):
        if line.startswith("$ cd "):
            change_path = line.split("$ cd ")[1]
            filesystem.cd(change_path)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            filesystem.make_dir(line.split('dir ')[1])
        elif len(line.split(' ')) == 2:
            size_name = line.split(' ')
            filesystem.make_file(name=size_name[1], size=int(size_name[0]))
    return filesystem

FILESYSTEM = None
DIRECTORY_SIZES = None
def solution_1(input_data: str):
    "part 1"
    global FILESYSTEM
    global DIRECTORY_SIZES
    FILESYSTEM = create_filesystem(input_data)
    DIRECTORY_SIZES = [d.size() for d in FILESYSTEM.ls("/", recursive=True) if isinstance(d, Directory)]
    return sum([s for s in DIRECTORY_SIZES if s < 100000])

def solution_2(input_data: str):
    "part 2"
    total_disk_size = 70000000
    target_free_space = 30000000
    free_space = total_disk_size - FILESYSTEM.size()
    minimum_delete = target_free_space - free_space
    return min([s for s in DIRECTORY_SIZES if s >= minimum_delete])


year, day = 2022, 7
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    for _ in range(500):
        print(solution_1(puzzle.input_data))
        print(solution_2(puzzle.input_data))
