myFile = open("questions.txt", "r")
content = myFile.read().split("\n\n")
part1 = 0

for x in content:
    part1 += len(set(x.replace("\n", "")))

print(part1)