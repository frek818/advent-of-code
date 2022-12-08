"""
--- Day 8: Treetop Tree House ---
"""
from functools import cache
from typing import List, Dict, Tuple

from aocd.models import Puzzle

class Table:
    def __init__(self, table: List[List[int]]):
        self.table = table
        self.width = len(table[0])
        self.height = len(table)

    def neighbor(self, x, y, direction):
        return getattr(self, direction)(x,y)
    def left(self, x, y): return (x-1, y,)
    def top(self, x, y): return (x, y-1,)
    def right(self, x, y): return (x+1, y,)
    def bottom(self, x, y): return (x, y+1,)
    
    def item(self, x, y):
        return self.table[y][x]

def memoize(visibility_table:dict):
    def outer(function):
        def inner(*args, **kwargs):
            if args in visibility_table:
                return visibility_table[args]
            result = function(*args, **kwargs)
            if result:
                visibility_table[(args[0],args[1])] = result
            return result
        return inner
    return outer

visibility_table = {}
@memoize(visibility_table) 
def is_visible_lt(x, y, table: Table):
    if x == 0 or y == 0 or x+1 == table.width or y+1 == table.height:
        return True
    height = table.item(x, y)
    if height > table.item(*table.left(x,y)) and is_visible_lt(*table.left(x,y),table):
        return True
    if height > table.item(*table.top(x,y)) and is_visible_lt(*table.top(x,y),table):
        return True
    return False

@memoize(visibility_table) 
def is_visible_rb(x, y, table: Table):
    if x == 0 or y == 0 or x+1 == table.width or y+1 == table.height:
        return True
    height = table.item(x, y)
    if height > table.item(*table.right(x,y)) and is_visible_lt(*table.right(x,y),table):
        return True
    if height > table.item(*table.bottom(x,y)) and is_visible_lt(*table.bottom(x,y),table):
        return True
    return False

def can_see(x, y, direction, table: Table):
    if x == 0 or y == 0 or x+1 == table.width or y+1 == table.height:
        return True
    height = table.item(x, y)
    
    # check all direction for being blocked
    for direction in ["left", "top"]:
        coords = table.neighbor(x,y,direction)
        other_height = table.item(*coords)
        if height > other_height and  


    

def solution_1(input_data: str):
    "part 1"
    forest = Table([[int(t) for t in line] for line in input_data.splitlines()])
    for y in range(forest.height):
        for x in range(forest.width):
            is_visible_lt(x, y, forest)
    for y in range(forest.height):
        for x in range(forest.width):
            is_visible_rb(x, y, forest)

    count = 0
    for y in range(forest.height):
        for x in range(forest.width):
            v = visibility_table.get((x,y))
            if v == True:
                count += 1
            print("V" if v else " ", end="")
        print()
    print(count)

                
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
