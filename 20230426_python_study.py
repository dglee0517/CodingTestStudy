# 정수 찾기
def solution(num_list, n):
    for i in range(len(num_list)):
        if num_list[i] == n:
            return 1
    return 0

print(solution([1, 2, 3, 4, 5, 6], 9))

# 조건에 맞게 수열 변환하기

def solution(arr, k):
        for i in range(len(arr)):
            if k % 2 == 0:
                arr[i] = arr[i] + k
            else:
                arr[i] = arr[i] * k
        return arr

print(solution([1, 2,5234,123], 3))

# 문자열 섞기

def solution(str1, str2):
    s1, s2 = list(str1), list(str2)
    answer = ''
    for i in range(len(s1)):
        answer = answer + s1[i] + s2[i]
    return answer

print(solution('aaaaa', 'bbbbb'))

# 더 크게 합치기

def solution(a, b):
    s1, s2 = str(a), str(b)
    if int(s1 + s2) > int(s2 + s1):
        return int(s1 + s2)
    else:
        return int(s2 + s1)

print(solution(9, 91))

# 두 수의 연산값 비교하기

def solution(a, b):
    s1, s2 = str(a), str(b)
    if int(s1 +s2) >= 2 * a * b:
        return int(s1 + s2)
    else:
        return 2 * a * b

print(solution(91, 2))


# 공배수

def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0

print(solution(55, 10, 5))

# 홀짝에 따라 다른 값 반환하기

def solution(n):
    sum = 0
    if n % 2 == 0:
        for i in range(1, n+1):
            if i % 2 == 0:
                sum = sum + i**2
    else:
        for i in range(1, n+1):
            if i % 2 != 0:
                sum = sum + i
    return sum

print(solution(10))

# 조건 문자열
ineq = "<"
eq = "="
def solution(ineq, eq, n, m):
    if ineq == "<" and eq == "=":
        if n <= m:
            return 1
        else: return 0
    elif ineq == ">" and eq == "=":
        if n >= m:
            return 1
        else: return 0
    elif ineq == ">" and eq == "!":
        if n > m:
            return 1
        else: return 0
    elif ineq == "<" and eq == "!":
        if n < m:
            return 1
        else: return 0

print(solution(ineq, eq, 10, 10))

# eval을 쓴 경우
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))

print(solution(ineq, eq, 10, 9))

# 길이에 따른 연산

def solution(num_list):
    result = 0
    multiple = 1
    if len(num_list) >= 11:
        for i in range(len(num_list)):
            result = result + num_list[i]
        return result
    else:
        for i in range(len(num_list)):
            multiple = multiple * num_list[i]
        return multiple

print(solution([2, 3, 4, 5]))

# 문자열의 앞의 n글자

def solution(my_string, n):
    return my_string[:n]

print(solution('ProgrammerS123', 11))

# 문자열 정수의 합

def solution(num_str):
    sum = 0
    for i in num_str:
        sum = sum + int(i)
    return sum

print(solution('123456789'))