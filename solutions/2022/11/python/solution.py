"""
--- Day 11: Monkey in the Middle ---
"""
import os
import math
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

    inner.__name__ = base_op.__name__
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
    divisible_factor: int
    next_monkey_true: int
    next_monkey_false: int
    inspected_count: int


def parse_monkey(lines: List[str]) -> Monkey:
    id = int(lines[0].split(" ")[1].split(":")[0])
    items = [int(x.strip()) for x in lines[1].split(":")[1].split(",")]
    operation = parse_operation(lines[2])
    test = int(lines[3].split("divisible by ")[1])
    next_monkey_true = int(lines[4].split(" monkey ")[1])
    next_monkey_false = int(lines[5].split(" monkey ")[1])
    return Monkey(
        id,
        items,
        operation,
        test,
        next_monkey_true,
        next_monkey_false,
        inspected_count=0,
    )


def parse_monkeys(input_data: str) -> List[Monkey]:
    return [parse_monkey(data.splitlines()) for data in input_data.split("\n\n")]


def relief_adjuster(worry) -> int:
    return worry // 3


def relief_adjuster_lcm(lcm) -> Callable[[int], int]:
    def relief_adjuster_(worry):
        return worry % lcm

    return relief_adjuster_


def is_divisible_fn(worry, test):
    return worry % test == 0


def process_monkey(monkey: Monkey, relief_adjuster) -> Dict[int, List[int]]:
    "return a dictionary of monkey_id -> outgoing_items"
    if not monkey.items:
        return {}

    destination_monkey = defaultdict(list)
    worry_levels = [relief_adjuster(monkey.operation(item)) for item in monkey.items]

    for new_worry in worry_levels:
        monkey.inspected_count += 1
        is_divisible = is_divisible_fn(new_worry, monkey.divisible_factor)
        destination_monkey[is_divisible].append(new_worry)
    return destination_monkey


def process_round(monkeys: List[Monkey], worry_adjuster: Callable[[int], int]):
    for monkey in monkeys:
        for true_or_false, items_ in process_monkey(monkey, worry_adjuster).items():
            destination_monkey = monkeys[
                monkey.next_monkey_true if true_or_false else monkey.next_monkey_false
            ]
            destination_monkey.items.extend(items_)
            monkey.items = []


def product_two_most_busy(
    monkeys: List[Monkey], rounds: int, worry_adjuster: Callable[[int], int]
):
    for _ in range(rounds):
        process_round(monkeys, worry_adjuster)
    top_two_busy = [
        monkey.inspected_count
        for monkey in sorted(monkeys[:], key=lambda x: x.inspected_count)[-2:]
    ]
    return operator.mul(*top_two_busy)


def solution_1(input_data: str):
    "part 1"
    monkeys = parse_monkeys(input_data)
    return product_two_most_busy(monkeys, 20, relief_adjuster)


def solution_2(input_data: str):
    "part 2"
    monkeys = parse_monkeys(input_data)
    lcm_test_factor = math.lcm(*[monkey.divisible_factor for monkey in monkeys])
    return product_two_most_busy(monkeys, 10000, relief_adjuster_lcm(lcm_test_factor))


year, day = 2022, 11
assert year and day, "year and day must be set"

if __name__ == "__main__":
    input_data = Puzzle(year=year, day=day).input_data
    for _ in range(int(os.getenv("TIMES", "1"))):
        print(solution_1(input_data))
        print(solution_2(input_data))
