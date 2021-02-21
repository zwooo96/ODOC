def solution(n, lost, reserve):
    answer = 0
    for student in range(n+1) :
        #여벌이 있지만 자신도 체육복을 도둑맞은 학생은 일반 학생과 같아지므로 제외한다
        if student in lost and student in reserve :
            lost.remove(student)
            reserve.remove(student)
    
    for student in range(n+1) :
        if student in lost :
            #빌려줄 사람이 있으면 더 이상 도둑맞은 학생X
            #빌려주고 나면 더 이상 빌려줄 수 있는 학생X
            if student-1 in reserve :
                lost.remove(student)
                reserve.remove(student-1)
            elif student+1 in reserve :
                lost.remove(student)
                reserve.remove(student+1)
    
    answer = n - len(lost) #전체 학생에서 옷 없는 학생 빼면 답
    return answer