from collections import Counter

inputFile = open("input", "r")
data = inputFile.read().splitlines()
passwordMatched = 0
for row in data:
    rowData = row.split()
    counter = Counter(rowData[2])
    char = rowData[1].replace(':','')
    stringCounted = counter[char]
    numberRange = rowData[0].split('-')
    if(int(numberRange[0]) <= stringCounted and int(numberRange[1]) >= stringCounted):
        passwordMatched += 1

print(passwordMatched)