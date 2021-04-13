def solution(priorities, location):
    answer = 0
    
    queue = []
    for i in range(len(priorities)) :
        queue.append((priorities[i], i)) #중요도와 요청 문서의 위치를 저장
    
    while queue : 
        now = queue.pop(0)
        pri, loc = now[0], now[1]

        for i in range(len(queue)) : #대기목록을 돌면서
            if queue[i][0] > pri : #중요도가 더 높은 문서가 있다면 현재 문서를 맨 뒤에 저장
                queue.append(now)
                break
        else : #중요도가 더 높은 문서가 없다면 출력
            answer += 1
            if loc == location : #요청문서가 출력됐다면 정지
                break
            
    return answer