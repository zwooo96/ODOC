def solution(n):
    answer = []
    
    tmp = list(map(int, str(n)))
    for i in range(len(tmp)-1, -1, -1) :
        answer.append(tmp[i])
    
    return answer