inputs = open("trees.txt", "r").read().splitlines()


def slope(right,down):
    c = 0
    tree = 0
    for line in inputs[::down]:
        n = c % len(line)
        c +=right
        if line[n] == '#':
            tree += 1

    return tree


print(slope(1,1)*slope(3,1)*slope(5,1)*slope(7,1)*slope(1,2))