import sys
T= int(sys.stdin.readline())
for _ in range(T):
    k= int(sys.stdin.readline())
    n= int(sys.stdin.readline())
    res= [i for i in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            res[i]+=res[i-1]
    print(res[-1])