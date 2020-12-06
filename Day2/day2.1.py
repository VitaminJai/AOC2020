my_file = open("passwords.txt")
paslist = my_file.readlines()
correct = 0

for i in paslist:
	count = 0
	string1 = i.split(" ")
	times = string1[0]
	min, max = times.split ("-")
	letter = string1[1].strip(":")
	lastString = string1[2].strip()
	for i in lastString:
		if i == letter:
			count += 1
	if int(min) <= count <= int(max):
		correct+=1

print(correct)