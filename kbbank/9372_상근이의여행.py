import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    f = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]
    # print(f)
    cnt = 1
    s1 = set([f[0][0], f[0][1]])
    while len(s1) != N:
        for i in f:
            if i[0] in s1 and i[1] in s1: # 둘 다 있는 경우
                continue
            if i[0] in s1 or i[1] in s1:
                s1.update([i[0], i[1]])
                cnt += 1
    print(cnt)