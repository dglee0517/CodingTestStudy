# 20230503 파이썬 알고리즘 공부

# 탐색 & 시뮬레이션
# string
# 회문 문자열 검사(대소문자 구분 x)
'''
import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    # for j in range(size//2):
    #     if s[j] != s[-1-j]:
    #         print('#%d NO' %(i+1))
    #         break
    # else:
    #     print('#%d YES' %(i+1))
    # 파이썬 함수로 코드
    if s == s[::-1]: # 문자를 거꾸로
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))

# 숫자만 추출
# 문자열에 섞여 있는 숫자만 추출해서 출력
# 추출한 숫자의 약수의 개수도 함께 출력

import sys
sys.stdin = open('input.txt', 'rt')

s = input()
res = 0
for i in s:
    if i.isdigit(): # 알파벳이 아닌 모든 숫자 형태 찾아줌
        # isdecimal 0 ~ 9까지 숫자를 찾아줌
        res = res * 10 + int(i)
print(res)
cnt = 0
# 약수 갯수 찾기
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)


# 카드 역배치
import sys
sys.stdin = open('input.txt', 'rt')

# a, b = map(int, input().split())
# a, b = b, a # a와 b swap하는 방법 알아둘것

a = list(range(21))
for _ in range(10): # _를 해주면 변수가 없이 반복함
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]= a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end=' ')

# 두 리스트 합치기 (sort사용하지 말고 풀것)
입력 예제
3
1 3 5
5
2 3 6 7 9

import sys
sys.stdin = open('input.txt', 'rt')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
print(c)
for x in c:
    print(x, end=' ')


# 수들의 합
# 내가 푼 코드(시간초과로 2문제 틀림)
import sys
sys.stdin = open('input.txt', 'rt')

a, b = map(int, input().split())
n = list(map(int, input().split()))
cnt = 0
sum = 0
for i in range(a):
    sum = n[i]
    for j in range(i+1, a):
        if n[j] == b:
            cnt += 1
            break
        sum += n[j]
        if sum == b:
            cnt += 1
            break
print(cnt)

# 정답
import sys
sys.stdin = open('input.txt', 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
'''

# ===============
# 프로그래머스 기초 트레이닝
# 수열과 구간 쿼리 4
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, len(arr[s:e+1])):
            if i * k == 0:
                arr[i] = arr[i] + 1
            elif i % k == 0:
                arr[i] = arr[i] + 1
    return arr
print(solution([0, 1, 2, 4, 3],[[0, 4, 1],[0, 3, 2],[0, 3, 3]]))

# 배열 만들기 2
# 5와 0만 포함된 배열만들기
# 2진수에 5를 곱한것과 같다
def solution(l, r):
    res = []
    for i in range(l, r+1):
        if all(j in ['0', '5'] for j in str(i)):
            res.append(i)
    if res:
        return res
    else:
        return [-1]

print(solution(5, 555))

def solution(l, r):
    res = []
    binary = 0
    while True:
        num = int(bin(binary)[2:])*5
        if num > r:
            break
        elif l <= num:
            res.append(num)
        binary += 1

    if res:
        return res
    else:
        return [-1]
print(solution(10, 200))

# 배열 만들기 4
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        elif len(stk) > 0:
            if stk[-1] < arr[i]:
                stk.append(arr[i])
                i += 1
            elif stk[-1] >= arr[i]:
                stk.pop()
    return stk
print(solution([1, 4, 2, 5, 3]))
stk =[1,2,4]
stk.pop()
print(stk)

# 간단한 논리 연산
def solution(x1, x2, x3, x4):
    return (x1 or x2) and  (x3 or x4)

print(solution(True, False, False, False))

# 주사위 게임 3

def solution(a, b, c, d):
    lst = [a, b, c, d]
    cnt = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == nums[i]:
                counts[i] += 1

    if max(cnt) == 4:
        return 1111 * a
    elif max(cnt) == 3:
        p = lst[cnt.index(3)]
        q = lst[cnt.index(2)]
        return (10 *p + q)**2
    elif max(cnt) == 2:
        if min(cnt) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = lst[cnt.index(2)]
            return (a * b * c * d) / (p ** 2)
    else:
        return min(lst)

nums = [5, 5, 1, 5]
counts = [0] * len(nums)
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[j] == nums[i]:
            counts[i] += 1
print(counts)
print(counts.index(1))
print(nums[counts.index(3)])

# 문자열 여러 번 뒤집기
def solution(my_string, queries):
    lst = list(my_string)
    for s, e in queries:
        lst[s:e+1] = lst[s:e+1][::-1]
    return ''.join(lst)

print(solution("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))

s = "rermgorpsam"
lst = list(s)
print(lst[::-1])
lst[2], lst[3] =lst[3], lst[2]
print(str(lst))