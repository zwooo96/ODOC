def solution(array, commands):
    answer = []
    for command in commands :
        temp = array[command[0]-1:command[1]] #i부터 j까지 자른다
        temp.sort()
        answer.append(temp[command[2]-1]) #k번째 수를 구한다
    return answer