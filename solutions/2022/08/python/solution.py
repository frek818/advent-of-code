"""
--- Day 8: Treetop Tree House ---
"""
from typing import List

from aocd.models import Puzzle

class Table:
    def __init__(self, table: List[List[int]]):
        self.table = table
        self.width = len(table[0])
        self.height = len(table)

    def left(self, x, y):
        if x == 0 or y == 0:
            return 0
        return self.table[y][x-1] 

    def top(self, x, y):
        if x == 0 or y == 0:
            return 0
        return self.table[y-1][x] 

    def right(self, x, y):
        if x+1 == self.width or y+1 == self.height:
            return 0
        return self.table[y][x+1]

    def bottom(self, x, y):
        if x+1 == self.width or y+1 == self.height:
            return 0
        return self.table[y+1][x]


def top_left(x, y, table: Table):
    return min(table.top(x,y), table.left(x,y))

def bottom_right(x, y, table: Table):
    return min(table.bottom(x,y), table.right(x,y))

def solution_1(input_data: str):
    "part 1"
    forest = Table([[int(t) for t in line] for line in input_data.splitlines()])
    #tl = [[0]*forest.width]*forest.height
    tl = [[0 for _ in range(forest.width)] for _ in range(forest.height)]
    br = [[0 for _ in range(forest.width)] for _ in range(forest.height)]
    for y in range(forest.height):
        for x in range(forest.width):
            tl[y][x] = top_left(x, y, forest)
            br[y][x] = bottom_right(x, y, forest)

    from pprint import pprint
    pprint(forest.table)
    pprint(tl)
    pprint(br)



    return 0


def solution_2(input_data: str):
    "part 2"
    return 0


year, day = 2022, 8
assert year and day, "year and day must be set"

if __name__ == '__main__':
    puzzle = Puzzle(year=year, day=day)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
