def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]

    def bfs(x,y):
        block = board[x][y]
        pop_set = set()
        if board[x+1][y] == board[x][y+1] == board[x+1][y+1] == block:
            pop_set = {(x,y),(x+1,y),(x,y+1),(x+1,y+1)}
        return pop_set
                
    def down_board(board):
        for y in range(n):
            for x in range(m-2,-1,-1):
                for next_x in range(m-1, x, -1):
                    if board[x][y] != '-' and board[next_x][y] == '-':
                        board[next_x][y] = board[x][y]
                        board[x][y] = '-'
                        
    while True:
        pop_set = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '-':
                    pop_set.update(bfs(i,j))
        
        if pop_set:
            answer += len(pop_set)
            for x,y in pop_set:
                board[x][y] = '-'
            down_board(board)
        else:
            break
    
    return answer
