with open("day10.txt") as file:
    data = [int(x) for x in file.read().splitlines()]

def part1(adapters):
    adapters.append(0)
    adapters.sort()
    difference = [adapters[i + 1] - x for i, x in enumerate(adapters[:-1])]
    return difference.count(1) * (difference.count(3) + 1)


def part2(adapters):
    possibilities = {adapters[-1]: 1}
    for a in reversed(adapters[:-1]):
        possibilities[a] = sum(possibilities.get(x, 0) for x in (a+1, a+2, a+3))
    return possibilities[0]

part1(data)
print(part2(data))