data = input("Enter list of sorted numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]

target = int(input("Enter the number to find: "))

lower = 0
upper = len(numbers) -1
idx = -1
while (lower <= upper):
    middle = int((lower + upper) // 2)
    if numbers[middle] == target :
        idx = middle
        break
    elif numbers[middle] < target :
        lower = middle + 1
    else:
        upper = middle - 1
if idx == -1:
    print("No such number:", target)
else:
    print("Target %d is at Index %d" %(target, idx))
