def _ord(ch: str) -> int:
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a') + 1
    if 'A' <= ch <= 'Z':
        return ord(ch) - ord('A') + 27
    raise ValueError(f"invalid character '{ch}'")

def sol(s: str) -> int:
    middle = len(s) // 2
    s1, s2 = set(s[:middle]), set(s[middle:])
    return sum(_ord(common) for common in s1.intersection(s2))

# print(sum(sol(line) for line in open("input.txt")))
#######
lines = open("input.txt").readlines()
it = iter(lines)
total = 0
while True:
    try:
        g1, g2, g3 = set(next(it)), set(next(it)), set(next(it))
        common = g1.intersection(g2).intersection(g3) - {'\n'}
        total += sum(_ord(ch) for ch in common)
    except StopIteration:
        break
print(total)
