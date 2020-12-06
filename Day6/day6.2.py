myFile = open("questions.txt", "r")
content = myFile.read().split("\n\n")
result = 0

for x in content:
    questions = "abcdefghijklmnopqrstuvwxyz"
    spaces = x.replace("\n", " ")
    splits = spaces.split()
    for x in splits:
        all = ""
        questions = all.join(set(questions).intersection(set(x)))
    result += len(questions)
print(result)