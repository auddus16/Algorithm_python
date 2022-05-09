import sys, heapq
T=int(sys.stdin.readline())
for _ in range(T):

    M=int(sys.stdin.readline())
    arr=[]
    if M % 10 ==0:
        for _ in range(M//10):
            arr.extend(list(map(int, sys.stdin.readline().split())))
    else:
        for _ in range(M//10+1):
            arr.extend(list(map(int, sys.stdin.readline().split())))

    min_q=[]
    max_q=[]
    ans=[arr[0],]
    mid=arr[0]

    for idx, val in enumerate(arr[1:]):
        if val<mid: #왼쪽 max_h으로
            heapq.heappush(max_q, -val)
        else:
            heapq.heappush(min_q, val)

        if idx % 2 !=0: # 삽입이 2번 이루어졌을 때마다 길이 비교
            if len(max_q)<len(min_q):
                heapq.heappush(max_q, -mid)
                mid=heapq.heappop(min_q)
            elif len(max_q)>len(min_q):
                heapq.heappush(min_q, mid)
                mid=-heapq.heappop(max_q)

            ans.append(mid)

    print(len(ans))
    print(' '.join(map(str, ans)))
