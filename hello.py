print('Hello, World!')
a = 10
print(a)
x = "Hello"
print(x)
print(type(x))

for i in range(1,11):
    print('*')


for i in range(1,6):
    for j in range(i):
        print('*',end=' ')
    print()

num_list = [12, 4, 15, 46, 38, -2, 15]
#num_list = [12, 22, 53, 24, 15, 6]
check = 0

def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1

print(solution(num_list))


def solution(my_string, k):
    answer = my_string*k
    return answer

print(solution('string', 3))


def solution(n):
    return str(n)

print(solution(3))

# 문자열의 뒤의 n글자
# 문자열 자르거나 곱해보는 연습 가능

def solution(my_string, n):
    answer = my_string[-n:]
    return answer

print(solution('He110W0r1d', 5))

# 문자 리스트를 문자열로 변환하기

def solution(arr):

    return "".join(arr)

print(solution(['a', 'b', 'c']))

s = 'hello world'
lst = list(s)
print(lst)