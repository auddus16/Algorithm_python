import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    sx, sy = map(int, sys.stdin.readline().strip().split())
    store = []
    chk = [False]*N

    for _ in range(N):
        x, y = map(int, sys.stdin.readline().strip().split())
        store.append((x, y))
    fx, fy = map(int, sys.stdin.readline().strip().split())

    dq = deque()
    dq.append((sx, sy, 20))

    flag = False
    while dq:
        x, y, beer = dq.popleft()

        if abs(x-fx) + abs(y-fy) <= beer * 50: # 현재위치 - 목적지
            flag = True
            break

        for i in range(len(store)):
            if not chk[i] and abs(store[i][0]-x) + abs(store[i][1]-y) <= beer * 50:
                dq.append((store[i][0], store[i][1], 20))
                chk[i] = True

    print('happy' if flag else 'sad')



