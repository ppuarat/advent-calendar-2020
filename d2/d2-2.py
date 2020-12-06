from collections import Counter

inputFile = open("input_d2.txt", "r")
data = inputFile.read().splitlines()
passwordMatched = 0
for row in data:
    #0: range 
    #1: char
    #2: sentence
    rowData = row.split()
    #0: first position
    #1: second position
    positions = rowData[0].split('-')

    sentenceArray = list(rowData[2])

    char = rowData[1].replace(':','')
    pos1 = int(positions[0])-1
    pos2 = int(positions[1])-1
    if(sentenceArray[pos1] == char or sentenceArray[pos2] == char):
        if(not sentenceArray[pos1] == sentenceArray[pos2] ):
            passwordMatched += 1
    

print(passwordMatched)