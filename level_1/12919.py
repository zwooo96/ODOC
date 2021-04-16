def solution(seoul):
    answer = '김서방은 '
    
    location = 0
    for i in seoul :
        if i == 'Kim' :
            break
        else :
            location += 1
        
    answer += str(location)
    answer += '에 있다'
    
    return answer