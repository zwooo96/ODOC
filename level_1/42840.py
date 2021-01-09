def solution(answers):
    answer = []
    #수포자 각각의 답을 최대 문제 수(10000)만큼 생성
    supoja1 = [1,2,3,4,5] * 2000
    supoja2 = [2,1,2,3,2,4,2,5] * 1250
    supoja3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    cnts = [0] * 3

    for i in range(len(answers)) :
        if answers[i] == supoja1[i] :
            cnts[0] += 1
        if answers[i] == supoja2[i] :
            cnts[1] += 1
        if answers[i] == supoja3[i] :
            cnts[2] += 1
    
    max_cnt = max(cnts)
    for i in range(len(cnts)) :
        if cnts[i] == max_cnt :
            answer.append(i+1)
    
    return answer