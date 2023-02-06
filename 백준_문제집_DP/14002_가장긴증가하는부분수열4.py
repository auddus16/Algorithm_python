import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * N
for i in range(N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
res = max(dp)
ans = []
idx = N-1
i = res
while i > 0:
    if ans:
        if dp[idx] == i and ans[0] > A[idx]:
            ans.insert(0, A[idx])
            i -= 1
    else:
        if dp[idx] == i:
            ans.append(A[idx])
            i -= 1
    idx -= 1

print(res)
print(' '.join(map(str, ans)))