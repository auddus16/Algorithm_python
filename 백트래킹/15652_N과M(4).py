import sys
N, M=map(int, sys.stdin.readline().split())
def bt(res, idx):
    if len(res)==M:
        print(' '.join(map(str, res)))
        return
    for i in range(idx, N+1):
        res.append(i)
        bt(res, i)
        res.pop(-1)
bt([], 1)