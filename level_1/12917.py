def solution(s):
    answer = ''
    s = list(s)
    s.sort(key=lambda x : -ord(x))
    answer = "".join(s)
    return answer