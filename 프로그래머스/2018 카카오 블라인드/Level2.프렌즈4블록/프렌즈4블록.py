def pop_block(board, m, n):
    pop_union_set = set()
    # 행과 열이 반대인 보드니까
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i-1][j-1] == board[i][j-1] == board[i-1][j] != '_':
                # 합집합 만들기
                pop_union_set |= set([(i,j),(i-1,j-1),(i,j-1),(i-1,j)])
    
    for i,j in pop_union_set:
        board[i][j] = 0
    
    for i, row in enumerate(board):
        empty_list = ['_'] * row.count(0)
        board[i] = empty_list + [block for block in row if block != 0]
        
    return len(pop_union_set)
    
def solution(m, n, board):
    answer = 0
    reversed_board = list(map(list,zip(*board)))
    while True:
        pop = pop_block(reversed_board, m, n)
        if pop == 0:
            return answer
        answer += pop
    
    return answer
