def solution(lst):
    answer = []
    dict = {}
    for i in lst:
        if dict.get(i) is None:
            dict[i] = 1
        else:
            dict[i] += 1
    most = max(dict.values())

    for key, value in dict.items():
        if value == most:
            answer.append(key)
    if len(answer) == len(lst):
        answer = []
    return answer

print(solution([1, 2, 3, 4, 5, 5])) #[5]
print(solution([12, 17, 19, 17, 23])) #[17]
print(solution([26, 37, 26, 37, 91])) #[26, 37]
print(solution([28, 30, 32, 34, 144])) #[]