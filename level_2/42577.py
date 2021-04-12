def solution(phone_book):
    answer = True
    
    phone_book.sort() #정렬을 하게 되면, 바로 뒷 번호만 확인하면 된다
    for i in range(len(phone_book)-1) :
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] : #한 번호가 바로 뒷 번호의 접두어라면
            answer = False
            break
            
    return answer