import copy

def rotate_90(board):
    return list(zip(*board[::-1]))

def compare_key(m, board):
    n = len(board) - 2 * m
    for i in range(n):
        for j in range(n):
            if board[m+i][m+j] != 1:
                return False
    return True


def is_locked(m, i, j, key, board):
    copy_board = copy.deepcopy(board)
    for x in range(m):
        for y in range(m):
            nx, ny = x+i, y+j
            if copy_board[nx][ny] == 1 and key[x][y] == 1:
                return False
            if copy_board[nx][ny] == 0 and key[x][y] == 1:
                copy_board[nx][ny] = key[x][y]
    return compare_key(m, copy_board)


def solution(key, lock):
    answer = False
    n, m = len(lock), len(key)
    board = [[0] * (n + 2 * m) for _ in range(n + 2 * m)]

    for i in range(n):
        for j in range(n):
            board[i+m][j+m] = lock[i][j]


    rotated_key = key
    for i in range(4):
        rotated_key = rotate_90(rotated_key)
        for x in range(1,m+n):
            for y in range(1,m+n):
                if is_locked(m, x, y, rotated_key, board):
                    return True
    return answer