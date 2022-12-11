from __future__ import annotations
from itertools import islice
from typing import Iterator


def task1(lines: list[int], cycles: set[int]) -> int:
    X = 1
    cycle = 0
    total_signal_strength = 0
    for line in lines:
        line = line.strip()
        cycle += 1
        if cycle in cycles:
            total_signal_strength += cycle * X
        if line == "noop":
            continue
        else:
            _, arg = line.split()
            cycle += 1
            if cycle in cycles:
                total_signal_strength += cycle * X
            X += int(arg)
    return total_signal_strength


def grouper(iterable: Iterator, n: int) -> Iterator[list]:
    for i in range(0, len(iterable), n):
        yield iterable[i : i + n]


task1_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()

cycles = set(range(20, 221, 40))
assert task1(task1_input, cycles) == 13140

# print(task1(open("input.txt"), cycles))

# print(task2(task1_input))
