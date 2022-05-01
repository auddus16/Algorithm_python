import sys
a=sys.stdin.readline().strip().split('-')
num=[]
for i in a:
    print(i)
    cnt=0
    s=i.split('+')
    for j in s:
        cnt+=int(j)
    num.append(cnt)
ans=num[0]
for i in range(1, len(num)):
    ans-=num[i]
print(ans)