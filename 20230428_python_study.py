'''
반복문을 이용한 문제풀이

1) 1부터 N까지 홀수 출력하기

2) 1부터 N까지의 합 구하기

3) N의 약수출력하기


# 1) 1부터 N까지 홀수 출력하기
n = int(input())
for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

# 2) 1부터 N까지의 합 구하기
n = int(input())
sum = 0
for i in range(1, n+1):
	sum = sum + i
print(sum)

# 3) N의 약수출력하기
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print()
'''

for i in range(6, 1, -1):
    for j in range(i-1):
        print('*', end=' ')
    print()

for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    print()

a = [12, 13, 7, 9, 19]
# 홀수만 출력하는 함수 짜기
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for y in a:
    if isPrime(y):
        print(y, end = ' ')
print()


def prime(x):
    for i in x:
        if i % 2 != 0:
            print(i, end = ' ')
prime(a)
print()

def plus_one(x):
    return x+1

a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x+1, a)))

# n 번째 원소까지
def solution(num_list, n):
    return num_list[:n]

print(solution([2, 1, 6],1))

# 조건에 맞게 수열 변환하기 1
def solution(arr):
    lst = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            lst.append(i/2)
        elif i <50 and i % 2 == 1:
            lst.append(i*2)
        else:
            lst.append(i)
    return lst
print(solution([1, 2, 3, 100, 99, 98]))



# 부분 문자열
def solution(str1, str2):
    if str2.find(str1) != -1:
        return 1
    else:
        return 0
print(solution('tbt', 'tbbttb'))

str1 = 'acb'
str2 = 'aabcc'
print(str2.find(str1))

# 카운트 다운
def solution(start, end):
    lst = []
    for i in range(start, end-1, -1):
        lst.append(i)
    return lst

# 뒤에서 5등 위로

def solution(num_list):
    num_list.sort()
    return num_list[5:]

print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))

# 부분 문자열인지 확인하기
def solution(my_string, target):
    if my_string.find(target) != -1:
        return 1
    else:
        return 0

s1 = 'bannada'
s2 = 'anna'
print(s2 in s1)

# n번째 원소부터
def solution(num_list, n):
    return num_list[n-1:]

print(solution([2, 1, 6], 3))

# 카운트 업

def solution(start, end):
    lst = []
    for i in range(start, end+1):
        lst.append(i)
    return lst
print(solution(3, 10))

# rny_string
def solution(rny_string):
    return rny_string.replace('m','rn')
print(solution('jerry'))

# 꼬리 문자열
def solution(str_list, ex):
    str = ''
    for i in str_list:
        if ex in i:
            str += ''
        else:
            str += i
    return str
print(solution(["abc", "def", "ghi"],'ef'))

# 특정한 문자를 대문자로 바꾸기

def solution(my_string, alp):
    return my_string.replace(alp, alp.upper())

print(solution('lowercase', 'x'))