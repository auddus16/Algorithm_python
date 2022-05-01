import sys
N, M= map(int, sys.stdin.readline().split())
def bt(res):
    if len(res)==M:
        print(' '.join(map(str, res)))
        return
    for i in range(1, N+1):
        res.append(i)
        bt(res)
        res.pop(-1)
bt([])