inputFile = open("input", "r")
data = inputFile.read().splitlines()
def appendPath(pathArray, currentPos):
    while currentPos + 1 >= len(pathArray):
        pathArray += pathArray
    return pathArray

def tree(step, skip = 1):
    currentPosition = 0
    numberOfTree = 0
    
    for index, path in enumerate(data):
        
        if(skip > 1 and index % skip != 0):
            continue
        pathArray = appendPath(list(path), currentPosition)
        
        if(currentPosition > 0 and pathArray[currentPosition] == '#'):
            numberOfTree += 1

        currentPosition = currentPosition + step

    return numberOfTree

result = [tree(1),tree(3),tree(5), tree(7), tree(1,2)]
total = 1
for num in result:
    total = total*num
print("Tree in each slopes: ", result)
print("Number of trees multiply together: ",total)
