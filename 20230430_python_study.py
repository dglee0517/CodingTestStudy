# 배열의 길이에 따라 다른 연산하기

def solution(arr, n):
    if len(arr) % 2 == 1:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] = arr[i] + n
        return arr
    else:
        for i in range(len(arr)):
            if i % 2 == 1:
                arr[i] = arr[i] + n
        return arr

print(solution([444, 555, 666, 777], 100))

# 글자 이어 붙여 문자열 만들기

def solution(my_string, index_list):
    str1 = ''
    for i in index_list:
        str1 = str1 + my_string[i]
    return str1

print(solution('cvsgiorszzzmrpaqpe', [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))


# 문자열 바꿔서 찾기

def solution(myString, pat):
    lst = list(myString)
    for i in range(len(myString)):
        if myString[i] == 'A':
            lst[i] = 'B'
        else:
            lst[i] = 'A'
    myString = ''.join(lst)
    if pat in myString:
        return 1
    else:
        return 0

print(solution('ABBAA', 'AABB'))

# 배열에서 문자열 대소문자 변환하기

def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 == 0:
            strArr[i] = strArr[i].lower()
        else:
            strArr[i] = strArr[i].upper()
    return strArr

print(solution(["AAA","BBB","CCC","DDD"]))

# 홀수 vs 짝수

def solution(num_list):
    sum1, sum2 = 0, 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            sum1 = sum1 + num_list[i]
        else:
            sum2 = sum2 + num_list[i]
    if sum1 >= sum2:
        return sum1
    else:
        return sum2

print(solution([4, 2, 6, 1, 7, 6]))