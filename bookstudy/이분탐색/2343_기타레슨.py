import sys
N, M=map(int, sys.stdin.readline().split())
a=list(map(int, sys.stdin.readline().split()))
s=max(a)
e=sum(a)
def check(m):
    cnt=1
    hap=0
    for i in range(N):
        if hap+a[i]<=m:
            hap+=a[i]
        else:
            cnt+=1
            hap=a[i]
    return cnt

mid=(s+e)//2
ans=e
while s<=e:
    if check(mid)>M: # M개를 넘길 경우
        s=mid+1
    else: # M개 이하
        ans = mid
        e=mid-1
    mid=(s+e)//2
print(ans)