score = int(input("Enter score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score:
    grade = 'B'
elif 70 <= score:
    grade = 'C'
else:
    grade = 'F'

print(f"Your score is {score}, Grade is {grade}.")
