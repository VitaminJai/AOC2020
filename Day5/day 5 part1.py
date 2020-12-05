myFile = open("seats.txt","r")
content = myFile.read().split("\n")
idlist = []
trans = str.maketrans('FBRL', '0110')

for line in content:
    idlist.append(int(line.translate(trans), 2))

print(max(idlist))