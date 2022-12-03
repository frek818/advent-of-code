from functools import reduce
from typing import List, FrozenSet

from aocd.models import Puzzle

DAY = 3
YEAR = 2022


class Rucksack:
    def __init__(self, content):
        assert len(
            content) % 2 == 0, f"Compartment aren't equal size {len(content)}"
        self._content = content

    @property
    def content(self):
        return self._content[:]

    @property
    def compartment_1(self):
        half = len(self.content) // 2
        return self.content[:half]

    @property
    def compartment_2(self):
        half = len(self.content) // 2
        return self.content[half:]

    def common_item_between_compartments(self):
        common_item = set(self.compartment_1).intersection(
            set(self.compartment_2))
        assert len(
            common_item) == 1, f"Multiple common items between compartments: {common_items}"
        return list(common_item)[0]


def common_item_in_group(group) -> List[FrozenSet[str]]:
    common_badge = reduce(lambda x, y: x.intersection(y), group)
    assert len(
        common_badge) == 1, f"Too many common item in group: {common_badge}"
    return list(common_badge)[0]


def item_value(item):
    ascii_code = ord(item)
    offset = 38 if (ascii_code < ord('Z') + 1) else 96
    return ascii_code - offset


def solution_1(input_data):
    answer = 0
    rucksacks = [Rucksack(line) for line in input_data.split('\n') if line]
    for rucksack in rucksacks:
        answer += item_value(rucksack.common_item_between_compartments())
    return answer


def solution_2(input_data):
    answer = 0
    rucksacks = [Rucksack(line) for line in input_data.split('\n') if line]
    group_size = 3
    group = []
    for idx, rucksack in enumerate(rucksacks):
        group.append(set(rucksack.content))
        if idx % group_size == (group_size - 1):
            answer += item_value(common_item_in_group(group))
            group = []
    return answer


if __name__ == '__main__':
    puzzle = Puzzle(year=YEAR, day=DAY)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
