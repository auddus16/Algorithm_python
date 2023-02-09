import sys
N, M = map(int, sys.stdin.readline().strip().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
sum_arr = [[0]*(N+1) for _ in range(N+1)]

# 누적합 구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_arr[i][j] = arr[i-1][j-1] + sum_arr[i-1][j] + sum_arr[i][j-1] - sum_arr[i-1][j-1]

# print(sum_arr)
# 부분합 구하기
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    print(sum_arr[x2+1][y2+1] - sum_arr[x2+1][y1] - sum_arr[x1][y2+1] + sum_arr[x1][y1])