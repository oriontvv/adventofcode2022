import re
from pprint import pprint

stacks = [
    [],
    ["S", "L", "W"],
    ["J", "T", "N", "Q"],
    ["S", "C", "H", "F", "J"],
    ["T", "R", "M", "W", "N", "G", "B"],
    ["T", "R", "L", "S", "D", "H", "Q", "B"],
    ["M", "J", "B", "V", "F", "H", "R", "L"],
    ["D", "W", "R", "N", "J", "M"],
    ["B", "Z", "T", "F", "H", "N", "D", "J"],
    ["H", "L", "Q", "N", "B", "F", "T"],
]

pattern = re.compile("move (\d+) from (\d+) to (\d+)")
for line in open("in.txt"):
    num, frm, to = map(int, re.match(pattern, line.strip()).groups())
    values = [stacks[frm].pop() for _ in range(num)]
    stacks[to].extend(values[::-1])

pprint(stacks)
for i in range(1, 10):
    print(stacks[i][-1], end="")
