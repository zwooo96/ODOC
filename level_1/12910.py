def solution(arr, divisor):
    answer = []
    for num in arr :
        if not num % divisor :
            answer.append(num)
    if not answer : #배열이 비어있으면
        answer.append(-1)
    answer.sort()
    return answer