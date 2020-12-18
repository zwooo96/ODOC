def solution(participant, completion):
    answer = ''
    p_dic = {}
    c_dic = {}

    for i in participant : #참가자 동명이인의 수를 센다
        if i in p_dic :
            p_dic[i] += 1
        else :
            p_dic[i] = 0
    
    for i in completion : #완주자 동명이인의 수를 센다
        if i in c_dic :
            c_dic[i] += 1
        else :
            c_dic[i] = 0
    
    for i in p_dic :
        if i not in c_dic : #완주자에 명단이 없거나
            answer = i
        #해당 이름의 참가자 수와 완주자 수가 다르다면
        elif p_dic[i] != c_dic[i] :
            answer = i
    
    return answer

"""
#정확성은 전부 통과했으나 효율성에 실패한 풀이법들
def solution(participant, completion):
    answer = ''
    for i in participant :
        if participant.count(i) == 1 :
            if i not in completion :
                answer = i
        else :
            if participant.count(i) != completion :
              answer = i
    return answer

def solution(participant, completion):
    answer = ''
    p_dic = {}
    c_dic = {}
    for i in participant :
        p_dic[i] = participant.count(i)
    for i in completion :
        c_dic[i] = completion.count(i)
    for i in participant :
        try :
            if p_dic[i] != c_dic[i] :
                answer = i
        except :
            answer = i
    return answer
"""