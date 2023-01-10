import sys
N = int(sys.stdin.readline().rstrip())
a = [int(sys.stdin.readline().strip()) for _ in range(N)]
res = 0
for i in range(N-2, -1, -1):
    if a[i] >= a[i+1]:
        res += a[i] - a[i+1]+1
        a[i] = a[i+1]-1
print(res)

