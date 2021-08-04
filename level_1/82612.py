def solution(price, money, count):
    answer = 0

    for i in range(1, count+1) :
        money -= price * i
    
    answer = abs(money) if money < 0 else answer
    
    return answer