import sys
ask = sys.stdin.readlines()
newAsk = []
multi = 0
other = []
for x in ask:
    new = x.strip("\n")
    newAsk.append(new)
print(newAsk)


for x in newAsk:
    for y in newAsk:
        for z in newAsk:
            if int(x)+int(y)+int(z) == 2020:
                print(int(x)*int(y)*int(z))