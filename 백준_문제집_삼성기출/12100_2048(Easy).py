from copy import deepcopy
import sys
N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# print(board)

def check(board, k):
    if k==0: # 위
        for c in range(N):
            p = 0
            for i in range(1, N):
                if board[i][c]:
                    tmp = board[i][c]
                    board[i][c] = 0
                    if board[p][c] == 0:
                        board[p][c] = tmp
                    elif board[p][c] == tmp:
                        board[p][c] *= 2
                        p += 1
                    else:
                        p += 1
                        board[p][c] = tmp

    elif k==1: # 아래
        for j in range(N):
            pointer = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    elif k==2: # 왼
        for j in range(N):
            pointer = N - 1
            for i in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[pointer][j] == 0:
                        board[pointer][j] = tmp
                    elif board[pointer][j] == tmp:
                        board[pointer][j] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[pointer][j] = tmp
    else:
        for i in range(N):
            pointer = N - 1
            for j in range(N - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][pointer] == 0:
                        board[i][pointer] = tmp
                    elif board[i][pointer] == tmp:
                        board[i][pointer] *= 2
                        pointer -= 1
                    else:
                        pointer -= 1
                        board[i][pointer] = tmp
    # print(board)
    return board

ans = 0
def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    # copy_board = copy.deepcopy(board)
    for i in range(4):
        copy_board = check(deepcopy(board), i)
        dfs(copy_board, cnt + 1)


dfs(board, 0)
print(ans)