# 코드 처리하기

# 원소들의 곱과 합
def solution(num_list):
    multiple = 1
    sum = 0
    for i in range(len(num_list)):
        multiple = multiple * num_list[i]
        sum = sum + num_list[i]

    if multiple < sum**2:
        return 1
    else:
        return 0

print(solution([5, 7, 8, 3]))

# 공백으로 구분하기 1

s = "i love you"
s1 = "programmers"
print(s.split())
print(s1.split())

# 등차수열의 특정한 항만 더하기

def solution(a, d, included):
    list = []
    sum = 0
    result = 0
    for i in range(len(included)):
        if i ==0:
            sum = sum + a
        else:
            sum = sum + d
        list.append(sum)
    for i in range(len(included)):
        if included[i]:
            result = result + list[i]
    return result

# 코드 개선 버전
# 리스트 컴프리헨션을 사용하여 코드를 줄인다.
# 파이썬에선 sum과 list의 함수가 있으므로 변수명으로 사용하지 않는것이 좋다.

def solution(a, d, included):
    lst = [a + d * i for i, inc in enumerate(included) if inc]
    return sum(lst)

boolean = [True, False, False, True, True]
print(solution(3, 4, boolean))

# 주사위 게임 2
# 오답
def solution(a , b, c):
    if 1 <= a <= 6 and 1 <= b <= 6 and 1 <= c <= 6:
        if a != b != c:
            return a + b + c
        elif a == b != c or a != b == c:
            return (a + b + c) * (a**2 + b**2 + c**2)
        elif a == b == c:
            return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
# 정답
def solution(a, b, c):
    if a == b == c:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    elif a == b or b == c or c == a:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return a + b + c
print(solution(5, 3, 3))

# 이어 붙인 수
def solution(num_list):
    odd = ''
    even = ''
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
    return int(odd) + int(even)

print(solution([5, 7, 8, 3]))


def solution(num_list):
    if num_list[len(num_list) - 1] > num_list[len(num_list) - 2]:
        num_list.append(num_list[len(num_list) - 1] - num_list[len(num_list) - 2])
        return num_list
    else:
        num_list.append(num_list[len(num_list) - 1] * 2)
        return num_list

print(solution([5, 2, 1, 7, 5]))

# 수 조작하기 1

def solution(n, control):
    for i in control:
        if i == 'w':
            n = n + 1
        elif i == 's':
            n = n - 1
        elif i == 'd':
            n = n + 10
        elif i == 'a':
            n = n - 10

    return n
print(solution(0, 'wsdawsdassw'))

# 수 조작하기 2
def solution(numLog):
    n = numLog[0]
    control = ''
    for i in range(1, len(numLog)):
        if numLog[i] == (n+1):
            control += 'w'
            n += 1
        elif numLog[i] == (n-1):
            control += 's'
            n -= 1
        elif numLog[i] == (n+10):
            control += 'd'
            n += 10
        elif numLog[i] == (n-10):
            control += 'a'
            n -= 10
    return control
print(solution([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))

# 주사위 게임 1

def solution(a, b):
    if a % 2 != 0 and b % 2 != 0:
        return a**2 + b**2
    elif (a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2!= 0):
        return 2 * (a + b)
    else:
        return abs(a - b)
print(solution(3, 4))
