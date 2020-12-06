import re
my_File = open("passports.txt", 'r')
checks = {
'byr':r'byr:((19[2-9]\d)|(200[0-2]))',
'iyr':r'iyr:((201\d)|2020)',
'eyr':r'eyr:((202\d)|2030)',
'hgt':r'hgt:(((1(([5-8]\d)|(9[0-3])))cm)|((59)|(6\d)|(7[0-6])in))',
'hcl':r'hcl:#(\d|[a-f]){6}',
'ecl':r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
'pid':r'pid:\d{9}\D'
}
validCheck = 1
counter = 0
for line in my_File:
    for x in checks.keys():
        if re.search(checks[x], line) != None:
            counter += 1
    if line == '\n':
        if counter == 7:
            validCheck += 1
        counter = 0
print(validCheck)