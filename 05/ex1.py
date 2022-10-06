data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]
minval = 99999999
for val in numbers:
    if (minval > val):
        minval = val
print("Minimum value:", minval)

minval = numbers[0]
for val in numbers:
    if (minval > val):
        minval = val
print("Minimum value2:", minval)

minval = numbers[0]
minidx = 0
for i in range(1, len(numbers)):
    if (minval > numbers[i]):
        minval = numbers[i]
        minidx = i
print("Min Val:", minval, "Min Index:", minidx)

maxval = numbers[0]
maxidx = 0
for i in range(1, len(numbers)):
    if (maxval < numbers[i]):
        maxval = numbers[i]
        maxidx = i
print("Max Val:", maxval, "Max Index:", maxidx)


currentsum = 0
for i in numbers:
    currentsum += i

print("Sum value:", currentsum)
print("Average value:", currentsum / len(numbers))
print("Min,Built-in:", min(numbers))
print("Max,Built-in:", max(numbers))
print("Sum,Built-in:", sum(numbers))

scoredb = [ {'Name':'Lee', 'Score':30},
    {'Name':'Kim', 'Score':40},
    {'Name':'Park', 'Score':50},
    {'Name':'Choi', 'Score':90} ]

print("Min:", min(scoredb, key=lambda person: person['Score']))
print("Max:", max(scoredb, key=lambda person: person['Score']))
