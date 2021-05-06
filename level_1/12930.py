def solution(s):
    answer = ''
    tmp = s.split(" ")
    for word in tmp :
        i = 0
        for w in word :
            if w.isalpha() :
                if i % 2 :
                    answer += w.lower()
                else :
                    answer += w.upper()
                i += 1
        answer += " "
    if len(answer) != len(s) :
        answer = answer[:-1]
    return answer