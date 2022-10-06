def solution(num):
    answer = 0
    for i in str(num):
        answer += int(i)
    return answer

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
"""
def solution(num)
    return sum([int(i) for i in str(num)])
"""

print(solution(5923)) #19
print(solution(200)) # 2
print(solution(1234567890)) #45
print(solution(2364759387)) #54
