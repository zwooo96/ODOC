def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    if not arr :
        arr.append(-1)
        
    answer = arr
    return answer