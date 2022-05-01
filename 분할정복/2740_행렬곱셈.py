import sys
N, M= map(int, sys.stdin.readline().split())
a= list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
M, K= map(int, sys.stdin.readline().split())
b= list(list(map(int, sys.stdin.readline().split())) for _ in range(M))
res=[[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            res[n][k]+= a[n][m] * b[m][k]

for i in res:
    for j in i:
        print(j, end=' ')
    print()



