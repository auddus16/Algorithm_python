import sys
T=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
cnt=0
for n in a:
    if n==1:
        continue
    flag=True
    for i in range(2, n):
        if n%i==0:
            flag=False
            break
    if flag:
        cnt+=1
print(cnt)