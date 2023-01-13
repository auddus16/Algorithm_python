import sys
from collections import deque
N, K = map(int, sys.stdin.readline().strip().split())
dx = (+1, -1)
chk = [False]*100001
chk[N] = True
dq = deque()
dq.append((0, N))

res = 9999999
while dq:
    t, x = dq.popleft()
    if x == K: # 도착
        res = min(t, res)
        continue
    for i in range(2):
        nx = x+dx[i]
        if 0<=nx<=100000 and not chk[nx]:
            dq.append((t+1, nx))
            chk[nx] = True
    nx = x*2
    if 0<=nx<=100000 and not chk[nx]:
        dq.append((t+1, nx))
        chk[nx] = True
print(res)
