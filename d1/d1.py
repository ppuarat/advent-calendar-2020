inputFile = open("input", "r")
data = inputFile.read().splitlines()
for num01 in data:
    for num02 in data:

        summ = int(num01) + int(num02)
        if(summ == 2020):
            print(int(num01) * int(num02))
            break
