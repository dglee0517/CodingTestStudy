# 프로그래머스 코딩 기초 트레이닝
# 주사위 게임 3

def solution(a, b, c, d):
    lst = [a, b, c, d]
    lst.sort()
    a, b, c, d = lst[0], lst[1], lst[2], lst[3]
    if a == b == c == d:
        return 1111 * a
    elif a == b == c:
        return (10 * a + d) ** 2
    elif b == c == d:
        return (10 * b + a) ** 2
    elif a == b and c == d:
        return (a + c) * abs(a - c)
    elif a == b or b == c or c == d:
        if a == b:
            return c * d
        elif b == c:
            return a * d
        elif c == d:
            return a * b
    else:
        return a

print(solution(1, 4, 4, 4))

# 배열 만들기

def solution(intStrs, k, s, l):
    res = []
    for i in range(len(intStrs)):
        tmp = int(intStrs[i][s:s+l])
        if tmp > k:
            res.append(tmp)
    return res
print(solution(["0123456789","9876543210","9999999999999"], 50000, 5, 5))

# 문자열 뒤집기
def solution(my_string, s, e):
    res = list(my_string)
    res[s:e+1] = res[s:e+1][::-1]
    return ''.join(res)
print(solution("Progra21Sremm3", 6, 12))

# 세로 읽기
def solution(my_string, m, c):
    str = ""
    for i in range(0, len(my_string), m):
        lst = my_string[i:i+m]
        str += lst[c-1]
    return str
print(solution("ihrhbakrfpndopljhygc", 4, 2))

# qr code
def solution(q, r, code):
    str = ""
    for i in range(len(code)):
        if i % q == r:
            str += code[i]
    return str
print(solution(3, 1, "qjnwezgrpirldywt"))