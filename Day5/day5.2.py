myFile = open("seats.txt","r")
content = myFile.read().split("\n")
idlist = []
trans = str.maketrans("FBRL", "0110")

for lines in content:
    idlist.append(int(lines.translate(trans), 2))

idsort = sorted(idlist)

for i in range(idsort[0], idsort[-1]):
    if i not in idsort:
        print(i)



