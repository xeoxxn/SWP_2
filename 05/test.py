def selectionSort(list):
    n = len(list)
    for i in range(n - 1):
        minIdx = i
        for j in range(i+1, n):
            if(list[j] < list[minIdx]):
                minIdx = j
        list[i], list[minIdx] = list[minIdx], list[i]

        printStep(list, i+1)

def printStep(A, val):
    print("     Step %d = " %val, end=' ')
    print(A)

list = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Before Sort : ", list)

selectionSort(list)
print("After Sort : ", list)

