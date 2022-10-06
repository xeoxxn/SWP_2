data = input("Enter list of sorted numbers (A): ")
numbers = data.split()
aList = [int(i) for i in numbers]
data = input("Enter list of sorted numbers (B): ")
numbers = data.split()
bList = [int(i) for i in numbers]


print("A =", aList)
print("B =", bList)

aPos = 0
bPos = 0
sortnbrs = []

while aPos < len(aList) and bPos < len (bList):
    if aList[aPos] > bList[bPos]:
        sortnbrs += [bList[bPos]]
        bPos += 1
    else:
        sortnbrs += [aList[aPos]]
        aPos += 1

while aPos < len(aList):
    sortnbrs += [aList[aPos]]
    aPos += 1

while bPos < len(bList):
    sortnbrs += [bList[bPos]]
    bPos += 1

print ("Merged = ", sortnbrs)

cList = sorted(aList + bList)
print("By Sort = ", cList)
