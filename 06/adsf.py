import random

def makeList(n):
    list = []
    for i in range(n):
        list.append(random.randint(1, 100))

    return list


def binarySearch(list, key):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = (low + high) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def recbinSearch(list, low, high, key):
    mid = (low + high) // 2
    if list[mid] == key:
        return mid
    elif list[mid] < key:
        return recbinSearch(list, mid + 1, high, key)
    else:
        return recbinSearch(list, low, mid - 1, key)



def linearSearch(list, key):
    size = len(list)

    for i in range(size):
        if(list[i] == key):
            return i


n = int(input('n : '))
list = makeList(n)
list = sorted(list)
print(list)
key = int(input('key : '))
idx = recbinSearch(list, 0, n-1, key)
if idx == -1:
    print("No Exist")
else:
    print("In %d index" % idx)
