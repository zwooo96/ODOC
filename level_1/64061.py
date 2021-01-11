def solution(board, moves):
    answer = 0
    basket = []
    for i in moves :
        for j in range(len(board)) :
            if board[j][i-1] :
                if not len(basket) : #바구니가 비어있으면 그냥 추가
                    basket.append(board[j][i-1])
                else : #바구니가 비어있지 않으면
                    #마지막에 추가한 것과 비교하고 같으면 터트리기
                    if basket[-1] == board[j][i-1] :
                        basket.pop()
                        answer += 2 #한 번 터트릴 때 사라지는 인형의 개수는 2개
                    else :
                        basket.append(board[j][i-1])
                board[j][i-1] = 0 #뽑힘 처리
                break
    return answer