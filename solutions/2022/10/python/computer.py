from dataclasses import dataclass
from typing import List, Union, Callable, Dict


@dataclass
class Sprite:
    width: int
    position: int

    def is_covering_position(self, position: int) -> bool:
        return position in range(self.position, self.position + self.width)


class CRT:
    def __init__(self, width: int, height: int, sprite: Sprite):
        self._width = width
        self._height = height
        self._sprite = sprite
        self._bits = [[None for _ in range(width)] for _ in range(height)]

    def position_sprite(self, position: int):
        self._sprite.position = position

    def paint(self):
        return "\n".join(["".join([str(self._bits[y - 1][x - 1])
                         for x in range(self._width)]) for y in range(self._height)])

    def draw(self, cycle_number: int):
        x_position, y_position = cycle_to_coords(cycle_number, self._width)
        if self._sprite.is_covering_position(x_position):
            self._bits[y_position][x_position] = "#"
        else:
            self._bits[y_position][x_position] = "."


def cycle_to_coords(cycle, width):
    x = (cycle - 1) % width
    y = (cycle - 1) // width
    return (x, y)


@dataclass
class Instruction:
    cycles_left: str
    parameter_count: int
    parameters: List[any]
    func: Union[Callable[[int], None], Callable[[], None]]

    def execute(self):
        if self.parameter_count > 0:
            self.func(*self.parameters)
        else:
            self.func()

    def decrement_cycles_left(self):
        self.cycles_left -= 1


class CPU():
    def __init__(
            self,
            registers: Dict[str, any] = None,
            ticks_per_cycle=1):
        self._cycle_number = 0
        self._registers = registers if registers else {'X': 1}
        self._during = self._registers.get('X')
        self._ticks_per_cycle = ticks_per_cycle
        self._instructions = {
            "addx": {
                "func": self.addx,
                "cycles": 2,
                "params": 1,
            },
            "noop": {
                "func": self.noop,
                "cycles": 1,
                "params": 0,
            }
        }
        self._instruction_queue: List[Instruction] = []
        self._cycles_to_sample = set()
        self._stages_to_sample = set()
        self._samples = []

    def set_cycles_to_sample(self, cycles_to_sample):
        self._cycles_to_sample = cycles_to_sample

    def set_stages_to_sample(self, stages_to_samples):
        self._stages_to_sample = stages_to_samples

    def power_samples(self, phase):
        return [sample[1] * sample[2]
                for sample in self._samples if sample[0] == phase]

    @property
    def signal_strength(self):
        return self._cycle_number * self._registers["X"]

    def addx(self, value):
        self._registers["X"] += value

    def noop(self):
        pass

    def queue_instruction(self, instruction_name, parameters=None):
        inst = self._instructions.get(instruction_name)
        cycles_left = inst.get("cycles")
        param_count = inst.get("params")
        func = inst.get("func")
        self._instruction_queue.append(
            Instruction(cycles_left, param_count, parameters, func)
        )

    @property
    def cycle_number(self):
        return self._cycle_number

    @property
    def during(self):
        return self._during

    def increment_cycle_count(self):
        self._cycle_number += 1

    def queue_instructions(self, instructions):
        for instruction, params in instructions:
            self.queue_instruction(instruction, params)

    def collect_sample(self, stage):
        if stage in self._stages_to_sample and self.cycle_number in self._cycles_to_sample:
            self._samples.append(
                (stage, self.cycle_number, self._registers.get('X')))

        if "during" == stage:
            self._during = self._registers.get('X')

    def done(self):
        return len(self._instruction_queue) == 0

    def tick(self):
        self.increment_cycle_count()
        self.collect_sample("during")
        if len(self._instruction_queue) == 0:
            return
        inst = self._instruction_queue[0]
        inst.decrement_cycles_left()
        if inst.cycles_left != 0:
            return
        inst.execute()
        self.collect_sample("after")
        self._instruction_queue = self._instruction_queue[1:]
