import sys
R, C = map(int, sys.stdin.readline().split())
board = list(list(sys.stdin.readline().strip()) for _ in range(R))
alph = set()
ans = 0

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c, cnt):
    global ans
    ans = max(cnt, ans)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<= nr <R and 0<= nc <C:
            if board[nr][nc] not in alph:
                alph.add(board[nr][nc])
                dfs(nr, nc, cnt+1)
                alph.remove(board[nr][nc])

alph.add(board[0][0])
dfs(0, 0, 1)
print(ans)