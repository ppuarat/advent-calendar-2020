inputFile = open("input", "r")
data = inputFile.read().splitlines()
#The locations you'd check in the above example are marked here 
# with O where there was an open square and X where there was a tree:

#start by counting all the trees you would encounter for the slope right 3, down 1
def appendPath(pathArray, currentPos):
    while currentPos + 1 >= len(pathArray):
        pathArray += pathArray
    return pathArray

currentPosition = 0
startingPosition = 0
numberOfTree = 0

for index, path in enumerate(data):
    pathArray = appendPath(list(path), currentPosition)
    
    if(currentPosition > 0 and pathArray[currentPosition] == '#'):
        numberOfTree +=1

    currentPosition = currentPosition + 3

print(numberOfTree)
