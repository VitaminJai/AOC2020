myFile = open('day9.txt','r')
data = [int(line) for line in myFile.read().split("\n")]


def numsum(num, numList):
    left = 0
    right = len(numList)-1
    while left < right:
        sum = numList[right] + numList[left]
        if sum == num:
            return True
        if sum > num:
            right -= 1
        else:
            left += 1
    return False


preamble = 24
for i in range(preamble, len(data)):
    num = data[i+1]
    numList = sorted(data[i-preamble:i+1])
    if not numsum(num, numList):
        break

left = 0
right = len(data)-1
for i in range(len(data)):
    for j in range(len(data) - 1):
        if sum(data[i:j]) == num:
            if i == j-1 : continue
            print(min(data[i:j]) + max(data[i:j]))