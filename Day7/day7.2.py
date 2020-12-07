myFile = open("day7.txt", "r")
content = myFile.read().split('\n')
allBags = {}


for line in content:
    line = line.replace("bags", "").replace("bag", "").strip(".")
    line = line.split("contain")
    allBags[line[0].strip()] = line[1].strip().split(',')


def getBag(bags):
    total = 1
    if "no other" in allBags[bags]:
        return 1
    for colours in allBags[bags]:
        each = colours.split()
        total += int(each[0]) * getBag(" ".join(each[1:]))
    return total


print(getBag("shiny gold")-1)