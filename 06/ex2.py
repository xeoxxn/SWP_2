upper = int(input("Enter a number: "))
sumval = 0
for i in range(1, upper + 1):
    sumval += i
print("Sum of 1 to", upper, "=", sumval)

def RecursiveSum(n):
    return 1 if n == 1 else RecursiveSum(n - 1) + n
print("Recursive Sum of 1 to", upper, "=", RecursiveSum(upper))

data = input("Enter list of numbers: ")
numbers = data.split()
numbers = [int(i) for i in numbers]

def RecursiveArraySum(nbrs, k):
    if k == 0:
        return nbrs[0]
    return RecursiveArraySum(nbrs, k - 1) + nbrs[k]

print("Recursive Array Sum:", RecursiveArraySum(numbers, len(numbers) - 1))
