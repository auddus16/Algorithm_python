import sys
N, M = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
sum_arr = [0] * (N+1)
for i in range(1, N+1):
    sum_arr[i] = sum_arr[i-1] + a[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().strip().split())
    print(sum_arr[j] - sum_arr[i-1])