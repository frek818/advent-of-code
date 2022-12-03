"""Day 2: Rock Paper Scissors"""
from aocd.models import Puzzle


OBJECT_MAP = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSOR",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSOR",
}
OBJECT_POINTS = {"ROCK": 1, "PAPER": 2, "SCISSOR": 3}
OUTCOME_SCORE = {"WIN": 6, "DRAW": 3, "LOSE": 0}

EXPECTED_OUTCOME_MAP = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}
REVERSE_OBJECT_MAP = {y: x for x, y in OBJECT_MAP.items()}


def play_score_expected_outcome(p1, expected_outcome):
    match (OBJECT_MAP[p1], EXPECTED_OUTCOME_MAP[expected_outcome]):
        case ("ROCK", "WIN"):
            p2 = REVERSE_OBJECT_MAP["PAPER"]
        case ("ROCK", "LOSE"):
            p2 = REVERSE_OBJECT_MAP["SCISSOR"]
        case ("SCISSOR", "WIN"):
            p2 = REVERSE_OBJECT_MAP["ROCK"]
        case ("SCISSOR", "LOSE"):
            p2 = REVERSE_OBJECT_MAP["PAPER"]
        case ("PAPER", "WIN"):
            p2 = REVERSE_OBJECT_MAP["SCISSOR"]
        case ("PAPER", "LOSE"):
            p2 = REVERSE_OBJECT_MAP["ROCK"]
        case _:
            p2 = p1
    return play_score(p1, p2)


def play_score(p1, p2):
    obj1 = OBJECT_MAP[p1]
    obj2 = OBJECT_MAP[p2]
    choice_points = OBJECT_POINTS[obj2]
    outcome_points = 0
    match (obj1, obj2):
        case ("ROCK", "PAPER"):
            outcome_points = OUTCOME_SCORE["WIN"]
        case ("ROCK", "SCISSOR"):
            outcome_points = OUTCOME_SCORE["LOSE"]
        case ("SCISSOR", "ROCK"):
            outcome_points = OUTCOME_SCORE["WIN"]
        case ("SCISSOR", "PAPER"):
            outcome_points = OUTCOME_SCORE["LOSE"]
        case ("PAPER", "ROCK"):
            outcome_points = OUTCOME_SCORE["LOSE"]
        case ("PAPER", "SCISSOR"):
            outcome_points = OUTCOME_SCORE["WIN"]
        case _:
            outcome_points = OUTCOME_SCORE["DRAW"]
    return outcome_points + choice_points


def solution_1(input_data):
    total_score = 0
    for play in input_data.split("\n"):
        if not play:
            continue
        total_score += play_score(*play.split(" "))
    return total_score


def solution_2(input_data):
    total_score = 0
    for play in input_data.split("\n"):
        if not play:
            continue
        total_score += play_score_expected_outcome(*play.split(" "))
    return total_score


if __name__ == "__main__":
    puzzle = Puzzle(year=2022, day=2)
    print(solution_1(puzzle.input_data))
    print(solution_2(puzzle.input_data))
