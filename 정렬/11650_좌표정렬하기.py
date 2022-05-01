import sys
N=int(sys.stdin.readline())
n=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
n.sort()
for i in n:
    sys.stdout.write(' '.join(map(str,i))+'\n')