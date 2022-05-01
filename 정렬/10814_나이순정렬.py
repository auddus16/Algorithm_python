import sys
N=int(sys.stdin.readline())
mem=[list(map(str, sys.stdin.readline().split())) for _ in range(N)]
mem.sort(key=lambda x:int(x[0]))
for i in mem:
    sys.stdout.write(' '.join(i)+'\n')