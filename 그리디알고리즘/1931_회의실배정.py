import sys
N=int(sys.stdin.readline().strip())
a=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
a.sort(key=lambda x:(x[1], x[0]))
s=0
cnt=0
for i in range(len(a)):
    if s<=a[i][0]:
        s=a[i][1]
        cnt+=1
print(cnt)