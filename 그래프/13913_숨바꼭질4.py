import sys
from collections import deque
N, K = map(int, sys.stdin.readline().strip().split())
dx = (-1, +1)

chk = [-1] * 100001
chk[N] = 0
dq = deque()
dq.append((N, 0))
res = [0] * 100001
res_time = int(1e9)
while dq:
    x, t = dq.popleft()
    if x == K:
        res_time = t
        print(res_time)
        break
    if 0 <= 2*x <= 100000 and chk[2*x] == -1:
        dq.append((x*2, t+1))
        chk[2*x] = t+1
        res[2*x] = x
    for i in range(2):
        nx = x + dx[i]
        if 0 <= nx <= 100000 and chk[nx] == -1:
            dq.append((nx, t+1))
            chk[nx] = t+1
            res[nx] = x

ans = []
tmp = K
for _ in range(res_time+1):
    ans.append(tmp)
    tmp = res[tmp]
print(' '.join(map(str, ans[::-1])))
