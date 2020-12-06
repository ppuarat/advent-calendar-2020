inputFile = open("input", "r")
data = inputFile.read().splitlines()


def findNumber():
    for num01 in data:
        for num02 in data:
            for num03 in data:
                if(num01 != num02 != num03):
                    summ = int(num01) + int(num02) + int(num03)
                    if(summ == 2020):
                        total = int(num01) * int(num02) * int(num03)
                        print(total)

findNumber()