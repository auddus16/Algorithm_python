import sys
N=sys.stdin.readline().strip()
for i in sorted(N, reverse=True):
    sys.stdout.write(i)