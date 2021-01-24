def solution(s):
    answer = ''
    index = len(s)//2
    if not len(s) % 2 :
        answer = s[index-1] + s[index]
    else :
        answer = s[index]
    return answer