from queue import LifoQueue
from typing import List

from aocd.models import Puzzle

DAY = 5
YEAR = 2022


class Stack(LifoQueue):
    def peek(self):
        item = self.get_nowait()
        self.put(item)
        return item


class Procedure:
    def __init__(self, line):
        data = [int(x) for x in line.split(" ") if x.isnumeric()]
        self.count = data[0]
        self.source = data[1] - 1
        self.destination = data[2] - 1


def parse_procedures(input_data):
    return [
        Procedure(line)
        for line in input_data.split("\n\n")[1].split("\n")
        if "from" in line
    ]


class CrateStacker:
    def __init__(self, stacks: List[Stack]):
        self.stacks = stacks

    def move(self, move: Procedure):
        source = self.stacks[move.source]
        destination = self.stacks[move.destination]
        for _ in range(move.count):
            if source.peek() is None:
                continue
            item = source.get()
            destination.put(item)

    def top_list(self):
        return [stack.peek() for stack in self.stacks if stack.peek()]

    @classmethod
    def from_input(cls, input_data):
        lines = [x for x in input_data.split("\n\n")[0].split("\n")]
        stack_count = len([x for x in lines[-1].split(" ") if x])
        stacks = [Stack() for _ in range(stack_count)]
        levels = [lines[stack_idx] for stack_idx in range(len(lines) - 2, -1, -1)]
        for level in levels:
            for stack_idx, item_idx in enumerate(range(1, stack_count * 4, 4)):
                column_value = level[item_idx]
                if column_value == " ":
                    continue
                stacks[stack_idx].put(column_value)
        return cls(stacks)


class CrateStackerv9001(CrateStacker):
    def move(self, move: Procedure):
        source = self.stacks[move.source]
        destination = self.stacks[move.destination]
        buffer = Stack()
        for _ in range(move.count):
            buffer.put(source.get())
        for _ in range(move.count):
            destination.put(buffer.get_nowait())


def solution_1(input_data):
    stacks = CrateStacker.from_input(input_data)
    procedures = parse_procedures(input_data)
    for procedure in procedures:
        stacks.move(procedure)
    return "".join(stacks.top_list())


def solution_2(input_data):
    stacks = CrateStackerv9001.from_input(input_data)
    procedures = parse_procedures(input_data)
    for procedure in procedures:
        stacks.move(procedure)
    return "".join(stacks.top_list())


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
