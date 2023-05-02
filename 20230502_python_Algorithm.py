# 20230502 파이썬 알고리즘 공부
# 자릿수의 합
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10 # 만약 125가 넘오왔다면 나머지는 5이고 5를 sum에 더한다
        x = x // 10 # 125를 10으로 나눈 몫은 12이고 12를 x에 더한다 이것을 반복한다.
    return sum
max = -2147000000
for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x

print(res)

# 파이썬 str함수 사용해서 풀이
def digit_sum(x):
    sum = 0
    for x in str(x):
        sum+=int(i)
    return sum
max = -2147000000
for x in a:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x

print(res)

# 소수(에라토스테네스 체)

import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)

# 뒤집은 소수
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
def reverse(x):
    res = 0
    while x >0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end= ' ')

# 주사위 게임
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int, tmp)
    if a == b and b == c:
        money = 10000 + a * 1000
    elif a == b or a == c:
        money = 1000 + (a * 100)
    elif b == c:
        money = 1000 + (b * 100)
    else:
        money = c * 100
    if money > res:
        res = money
print(res)

# 점수계산
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))

sum = 0
cnt = 0
for x in a:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)


# 특별한 이차원 배열 2
a = [[5, 192, 33], [192, 72, 95], [33, 95, 999]]
c = [[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]
print(len(a))
def solution(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                cnt += 1
            else:
                cnt = cnt
    if cnt == len(arr)*len(arr):
        return 1
    else:
        return 0
print(solution(a))

# 콜라츠 수열 만들기
def solution(n):
    lst = []
    while n > 0:
        if n % 2 == 0:
            lst.append(n)
            n = n // 2
        elif n == 1:
            lst.append(n)
            n = 3 * n + 1
            break
        else:
            lst.append(n)
            n = 3 * n + 1
    return lst

print(solution(10))

# 9로 나눈 나머지
def solution(number):
    return int(number) % 9

print(solution("78720646226947352489"))

def solution(number):
    sum = 0
    for i in number:
        sum += int(i)
    return sum % 9

print(solution("78720646226947352489"))

# ad 제거하기
def solution(strArr):
    res = []
    for i in strArr:
        if 'ad' not in i:
            res.append(i)
    return res
print(solution(["and","notad","abcd"]))

# 순서 바꾸기
def solution(num_list, n):
    a = num_list[:n]
    b = num_list[n:]
    return b + a

print(solution([5, 2, 1, 7, 5],3))

# 할 일 목록
def solution(todo_list, finished):
    res = []
    for i in range(len(todo_list)):
        if finished[i] != True:
            res.append(todo_list[i])
    return res
print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"],[True, False, True, False]))

# 가까운 1 찾기
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
        elif arr[i] == 0:
            continue
    return -1
print(solution([1, 1, 1, 1, 0], 3))

# 배열 만들기
def solution(arr, intervals):
    res = []
    for i, j in intervals:
        res += arr[i:j+1]
    return res
print(solution([1, 2, 3, 4, 5],[[1, 3], [0, 4]]))

# l로 만들기
def solution(myString):
    str = ''
    for i in myString:
        if ord(i) < ord('l'):
            str += 'l'
        else:
            str += i
    return str
print(solution("abcdevwxyz"))

# 배열 비교하기
def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) == sum(arr2):
            return 0
        else:
            return -1
    else:
        return 1
print(solution([1, 2, 3, 4, 5]	, [3, 3, 3, 3, 3]))

# 0 떼기
def solution(n_str):
    str =''
    for i in range(len(n_str)):
        if n_str[i] == '0':
            str += ''
            print('1', str)
        elif i != '0':
            for j in range(i, len(n_str)):
                str += n_str[j]
            break
    return str
print(solution("0010"))
def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]

# 수열과 구간 쿼리3
def solution(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr
print(solution([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))


# 수열과 구간 쿼리 2
def solution(arr, queries):
    res = []
    for s, e, k in queries:
        a = arr[s:e+1]
        a.sort()
        for i in a:
            if i > k:
                res.append(i)
                break
        else:
            res.append(-1)
    return res
print(solution([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))

# 코드 처리하기

def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] != '1':
            if mode == 0:
                if i % 2 == 0:
                    ret += code[i]
            elif mode == 1:
                if i % 2 == 1:
                    ret += code[i]
        elif code[i] == '1':
            if mode == 0:
                mode = 1
            else:
                mode = 0
    if ret == '':
        return 'EMPTY'
    return ret

print(solution('abc1abc1abc'))

# 5명씩

def solution(names):
    res = []
    for i in range(0, len(names), 5):
        print(i)
        res.append(names[i])
    return res

print(solution(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))