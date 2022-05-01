import sys
N=int(sys.stdin.readline())
n=[]
for i in range(N):
    n.append(int(sys.stdin.readline()))
for i in sorted(n):
    sys.stdout.write(str(i)+'\n')
#파이썬의 기본정렬메소드는 O(nlog(N))
#시간단축을 위해 sys.stdin, sys.stdout 사용