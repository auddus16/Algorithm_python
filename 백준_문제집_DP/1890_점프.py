import sys
N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
dp = [[0]*(N) for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        s = board[i][j]
        if s == 0:
            break
        if 0<=i+s<N: # 아래
            dp[i+s][j] += dp[i][j]
        if 0<=j+s<N: # 오른쪽
            dp[i][j+s] += dp[i][j]

print(dp[N-1][N-1])