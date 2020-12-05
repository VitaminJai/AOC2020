myFile = open("seats.txt","r")
content = myFile.read().split("\n")
newlist = []

trans = str.maketrans('FBRL', '0110')

for line in content:
    newlist.append(int(line.translate(trans), 2))
print(max(newlist))
