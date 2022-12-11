"""
--- Day 10: Cathode-Ray Tube ---
"""
import os
from typing import List, Tuple

from aocd.models import Puzzle

from computer import CPU, CRT, Sprite


def parse_instruction(line) -> Tuple[str, List[int]]:
    parts = line.split(" ")
    op = parts[0]
    params = [int(x) for x in parts[1:]]
    return (op, params)


def parse_instructions(input_data: str) -> List[Tuple[str, List[int]]]:
    return [parse_instruction(line) for line in input_data.splitlines()]


def solution_1(input_data: str):
    "part 1"
    cpu = CPU()
    cpu.queue_instructions(parse_instructions(input_data))
    cpu.set_cycles_to_sample([20, 60, 100, 140, 180, 220])
    cpu.set_stages_to_sample(["during"])
    while True:
        cpu.tick()
        if cpu.done():
            break
    return sum(cpu.power_samples("during"))


def solution_2(input_data: str):
    "part 2"
    cpu = CPU()
    cpu.queue_instructions(parse_instructions(input_data))
    sprite = Sprite(3, cpu.during)
    crt = CRT(width=40, height=6, sprite=sprite)
    while True:
        cpu.tick()
        crt.set_position_sprite(cpu.during)
        crt.draw(cpu.cycle_number)
        if cpu.done():
            break
    return crt.paint()


year, day = 2022, 10
assert year and day, "year and day must be set"

if __name__ == "__main__":
    puzzle = Puzzle(year=year, day=day)
    for _ in range(int(os.getenv("TIMES", "1"))):
        print(solution_1(puzzle.input_data))
        print(solution_2(puzzle.input_data))
