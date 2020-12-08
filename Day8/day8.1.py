myFile = open("day8.txt").readlines()


def part1(lines):
    acc = 0
    lineNum = 0
    repeat = set()
    while True:
        if lineNum in repeat:
            return False, acc
        line = lines[lineNum].strip().split()
        command = line[0]
        num = int(line[1])
        repeat.add(lineNum)
        if command == 'acc':
            acc += num
        if command == 'jmp':
            lineNum += num
        else:
            lineNum += 1
        if lineNum >= len(lines):
            return True, acc


print(part1(myFile)[1])