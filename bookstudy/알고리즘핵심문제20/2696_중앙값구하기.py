import sys, heapq
T=int(sys.stdin.readline())
for _ in range(T):

    M=int(sys.stdin.readline())
    arr=list(map(int, sys.stdin.readline().split()))

    cnt=0
    ans=[]
    h=[]
    for i in range(0, M):
        if i%2==0:
            h=[]
            heapq.heappush(h, arr[i])
            ans.append(h[len(h)//2])
        else:
            heapq.heappush(h, arr[i])

    print(M//2+1)
    print(' '.join(map(str, ans)))
