my_file = open("passports.txt")
lines = my_file.read().split("\n\n")
checks = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
count = 0

for line in lines:
    keys = set(map(lambda x: x.split(':')[0], line.split()))
    if keys.issuperset(checks):
        count += 1

print(count)