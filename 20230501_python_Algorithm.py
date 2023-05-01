'''
import sys
sys.stdin = open('input.txt', 'rt')

n = input()
print(n)

# k번째 약수
import sys
#sys.stdin = open('input.txt', 'rt')
n, k = map(int, input().split())
cnt = 0

for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

# k번째 수

import sys
#sys.stdin = open('input.txt', 'rt')
T = int(input())
for t in range(T):
    n, s , e, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = lst[s-1:e]
    lst.sort()
    print('#%d %d' %(t+1, lst[k-1]))

# K번째 큰 수
import sys
#sys.stdin = open('input.txt', 'rt')

n, k = map(int, input().split())
lst = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(lst[i]+lst[j]+lst[m])
res = list(res)
res.sort(reverse = True)
print(res[k-1])

# 최솟값 구하기

arr  = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i]  < arrMin:
        arrMin = arr[i]
print(arrMin)

# 대표값 구하기
n = int(input())
lst = list(map(int, input().split()))
# ave = round(sum(lst) / n) # 소수 첫째 자리에서 반올림
# 파이썬에서는 round_half_even 방식을 택함
# a = 4.5000
# print(round(a)) >>> 짝수쪽으로 근사값이 됨 그래서 4가 됨
# a = 66.6
# a = a + 0.5
# a = int(a) >>> 67
ave = int(sum(lst) / n + 0.5)
min = 2147000000
for idx, x in enumerate(lst):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)

# 정다면체

n, k = map(int, input().split())
cnt =[0]*(n+k+3)
max = -2147000000
for i in range(1, n+1):
    for j in range(1, k+1):
        cnt[i+j] += 1

for i in range(n+k+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(n+k+1):
    if cnt[i] == max:
        print(i, end = ' ')
'''

# n개 간격의 원소들

def solution(num_list, n):
    answer = []
    for i in range(0,len(num_list),n):
        answer.append(num_list[i])
    return answer
print(solution([4, 2, 6, 1, 7, 6], 4))


def solution(num_list, n):
    return num_list[::n]
print(solution([4, 2, 6, 1, 7, 6], 4))

# A 강조하기
def solution(myString):
    str = ''
    for i in myString:
        if i == 'a':
            str += i.upper()
        elif i == 'A':
            str += i
        else:
            str += i.lower()
    return str
print(solution("abstract Algebra"))

# 접미사인지 확인하기

def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    else:
        return 0
print(solution("banana", "nan"))

# 접두사인지 확인하기
def solution(my_string, is_prefix):
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0
print(solution("apple", "ap"))

# 원하는 문자열 찾기
def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0

print(solution('aaAA','aaaaa'))

# 뒤에서 5등까지
def solution(num_list):
    num_list.sort()
    lst = []
    for i in range(5):
        lst.append(num_list[i])
    return lst
print(solution([12, 4, 15, 46, 38, 1, 14]))

# 배열의 원소만큼 추가하기
def solution(arr):
    lst = []
    for i in arr:
        for j in range(i):
            lst.append(i)
    return lst
print(solution([6, 6]))

# 접미사 배열
def solution(my_string):
    lst = []
    for i in range(len(my_string)):
        lst.append(my_string[-i:])
    lst.sort()
    return lst
print(solution("banana"))

# 간단한 식 계산하기
def solution(binomial):
    return int(eval(binomial))
print(solution('43 + 12'))

binomial = '0 - 7777'

def solution(binomial):
    a, b, c = binomial.split(' ')
    if b == '+':
        return int(a) + int(c)
    elif b == '-':
        return int(a) - int(c)
    elif b == '*':
        return int(a) * int(c)

print(solution(binomial))

# 공백으로 구분하기2

def solution(my_string):
    lst = []
    for i in my_string.split(' '):
        if i != '':
            lst.append(i)
    return lst
print(solution(" i    love  you"))

# 부분 문자열 이어 붙여 문자열 만들기
def solution(my_strings, parts):
    str = ''
    for idx, (s,e) in enumerate(parts):
        str += my_strings[idx][s:e+1]
    return str
print(solution(["progressive", "hamburger", "hammer", "ahocorasick"],[[0, 4], [1, 2], [3, 5], [7, 7]]))

# 배열의 원소 삭제하기

def solution(arr, delete_list):
    result = []
    for i in arr:
        if i not in delete_list:
            result.append(i)
    return result
print(solution([110, 66, 439, 785, 1], [377, 823, 119, 43]))
