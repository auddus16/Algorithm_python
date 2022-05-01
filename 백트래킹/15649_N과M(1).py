import sys
N, M=map(int, sys.stdin.readline().split())
check=[False]*(N+1)
def bt(res):
    if len(res)==M:
        print(' '.join(map(str, res)))
        return
    for i in range(1, N+1):
        if check[i]:
            continue
        res.append(i)
        check[i]=True
        bt(res)
        res.pop(-1)
        check[i]=False
bt([])