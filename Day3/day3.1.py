inputs = open("trees.txt", "r").read().splitlines()


def slope(right,down):
    c = 0
    trees = 0
    for line in inputs[::down]:
        n = c % len(line)
        c +=right
        if line[n] == '#':
            trees += 1
    return trees


print(slope(3,1))