def solution(a, b):
    arr = [i for i in range(min(a,b), max(a,b)+1)]
    answer = sum(arr) 
    return answer