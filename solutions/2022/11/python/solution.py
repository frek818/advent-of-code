"""
--- Day 11: Monkey in the Middle ---
"""
import os
from collections import defaultdict
from dataclasses import dataclass
import operator
from typing import Callable, List, Dict

from aocd.models import Puzzle


def make_operation(base_op, other=None) -> Callable[[int], int]:
    if other is None:

        def inner(old):
            return base_op(old, old)

    else:

        def inner(old):
            return base_op(old, other)

    return inner


def parse_operation(op_str) -> Callable[[int], int]:
    op_table = {"*": operator.mul, "+": operator.add}
    a, op, b = op_str.split("=")[1].split(" ")[1:]
    op = op_table[op]
    return make_operation(op, None) if a == b else make_operation(op, int(b))


@dataclass
class Monkey:
    id: int
    items: List[int]
    operation: Callable[[int], int]
    test: Callable[[int, int], bool]
    next_monkey_true: int
    next_monkey_false: int
    inspect_count: int


def parse_monkey(lines: List[str]) -> Monkey:
    id = int(lines[0].split(" ")[1].split(":")[0])
    items = [int(x.strip()) for x in lines[1].split(":")[1].split(",")]
    operation = parse_operation(lines[2])
    test = int(lines[3].split("divisible by ")[1])
    next_monkey_true = int(lines[4].split(" monkey ")[1])
    next_monkey_false = int(lines[5].split(" monkey ")[1])
    return Monkey(
        id, items, operation, test, next_monkey_true, next_monkey_false, inspect_count=0
    )


def parse_monkeys(input_data: str) -> List[Monkey]:
    return [parse_monkey(data.splitlines()) for data in input_data.split("\n\n")]


def relief_adjuster(worry) -> int:
    return worry // 3


def process_monkey(monkey: Monkey) -> Dict[int, List[int]]:
    "return a dictionary of monkey_id -> outgoing_items"
    item_allocation = defaultdict(list)
    worry_levels = [relief_adjuster(monkey.operation(item)) for item in monkey.items]
    for new_worry in worry_levels:
        monkey.inspect_count += 1
        is_divisible = (new_worry % monkey.test) == 0
        destination = (
            monkey.next_monkey_true if is_divisible else monkey.next_monkey_false
        )
        item_allocation[destination].append(new_worry)
    monkey.items = []
    return item_allocation


def process_round(monkeys: List[Monkey]):
    for monkey in monkeys:
        for monkey_id, items in process_monkey(monkey).items():
            monkeys[monkey_id].items.extend(items)


def solution_1(input_data: str):
    "part 1"
    monkeys = parse_monkeys(input_data)
    for _ in range(20):
        process_round(monkeys)
    top_two_busy = [
        m.inspect_count for m in sorted(monkeys[:], key=lambda x: x.inspect_count)[-2:]
    ]
    return operator.mul(*top_two_busy)


def solution_2(input_data: str):
    "part 2"
    return 0


year, day = 2022, 11
assert year and day, "year and day must be set"

if __name__ == "__main__":
    puzzle = Puzzle(year=year, day=day)
    for _ in range(int(os.getenv("TIMES", "1"))):
        print(solution_1(puzzle.input_data))
        print(solution_2(puzzle.input_data))
