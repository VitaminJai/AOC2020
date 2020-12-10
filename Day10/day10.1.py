with open("day10.txt") as file:
    data = [int(x) for x in file.read().splitlines()]


def part1(adapters):
    adapters.append(0)
    adapters.sort()
    difference = [adapters[i + 1] - x for i, x in enumerate(adapters[:-1])]
    return difference.count(1) * (difference.count(3) + 1)

print(part1(data))
