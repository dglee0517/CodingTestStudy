# 파이썬 시작
print('hello world!')

# 첫 번째로 나오는 음수 list 연습

num_list = [12, 4, 15, 46, 38, -2, 15]
# num_list = [12, 22, 53, 24, 15, 6]

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

print(solution(num_list))
# index를 알고 싶을때
print(num_list.index(12)) # == 0

# 문자열 곱하기
def solution(my_string, k):
    answer = my_string*k
    return answer

print(solution('string', 3))

# 정수를 문자열로 바꾸기
def solution(n):
    return str(n)

print(solution(3))

# 문자열 숫자로 바꾸기
def solution(n):
    return int(n)

print(solution('123'))

# 문자열의 뒤의 n글자

def solution(my_string, n):
    answer = my_string[-n:]
    return answer

print(solution('He110W0r1d', 5))

# 앞에서 부터 n글자
def solution(my_string, n):
    return my_string[:n]

print(solution('He110W0r1d', 5))

# 문자 리스트를 문자열로 변환하기

def solution(arr):
    return "".join(arr)
print(solution(['a', 'b', 'c']))

# 문자열을 리스트로 변환하기

def soltion(my_string):
    return list(my_string)
print(soltion('Hello World'))

# # a와 b 출력하기
#
# a, b = map(int, input().strip().split(' '))
# print('a =',a,'b =',b)
#
# # 문자열 반복해서 출력하기
#
# a, b = input().strip().split(' ')
# b = int(b)
# result = a*b
# print(result)
#
# # 대소문자 바꿔서 출력하기
# str = input()
# result = ''
# for char in str:
#     if char.isupper():
#         result += char.lower()
#     else:
#         result += char.upper()
#
# print(result)
#
# # 특수문자 출력하기
# print('!@#$%^&*(\\'"'"'"<>?:;')
#
# # 덧셈식 출력하기
# a, b = map(int, input().strip().split(' '))
# print(a,'+',b,'=',a+b)

# 문자열 붙여서 출력하기

str1, str2 = input().strip().split(' ')
print(str1+str2)

# 문자열 돌리기
str = input()
for s in str:
    print(s)

# 홀짝 구분하기
a = int(input())

if a % 2 == 0:
    print(a,'is even')
else:
    print(a,'is odd')

# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    answer = my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    return answer

print(solution('He11oWor1d','lloWorl', 2))