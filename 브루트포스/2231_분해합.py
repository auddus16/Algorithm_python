import sys
N=int(sys.stdin.readline())
for i in range(1, N+1):
    temp=list(map(int, str(i)))
    total=i+sum(temp)
    if total==N:
        print(i)
        break
    if i==N:
        print(0)