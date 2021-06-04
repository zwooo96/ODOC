def solution(phone_number):
    
    cnt = len(phone_number)
    answer = '*' * (cnt-4)
    answer += phone_number[-4:]
    
    return answer