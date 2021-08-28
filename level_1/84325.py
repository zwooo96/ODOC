def solution(table, languages, preference):
    
    #직업군 별 점수를 저장할 list
    result = [0 for i in range(len(table))]

    #공백을 기준으로 나눔
    for i in range(len(table)) :
        table[i] = table[i].split()
    
    for i in range(len(table)) : #각 직업군 별로 탐색
        for j in range(len(languages)) : #각 언어 별로 탐색 
            tmp = 0
            for k in range(1, len(table[i])) :
                if table[i][k] == languages[j] : #해당 언어인 경우
                    tmp += (6-k) * preference[j] #점수와 선호도를 곱함
            result[i] += tmp #직업군 별 점수 산출
    
    val = max(result) #최댓값 산출
    temp = []
    for i in range(len(result)) :
        if val == result[i] : #최댓값과 일치하는 점수를 가진 직업군을 전부 저장
            temp.append(table[i][0])
    temp.sort() #사전 순으로 가장 빠른 직업군을 얻기 위해 정렬
    
    return temp[0]