def decideNumber(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"
a = int(input("Enter the number: "))
print(decideNumber(a))