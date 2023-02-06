import sys
N = int(sys.stdin.readline().strip())
a = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
a.sort(key= lambda x: (x[1], x[0]))
for i in range(N):
    print(f'{a[i][0]} {a[i][1]}')