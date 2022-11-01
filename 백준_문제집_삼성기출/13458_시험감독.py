import sys
N = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
B, C = map(int, sys.stdin.readline().strip().split())

cnt = 0
for i in range(N):
    # 총감독
    a[i] -= B
    cnt += 1
    #부감독
    if a[i] > 0:
        if a[i] <= C: # 부감독이 1명만 필요한 경우
            cnt += 1
        else: # 부감독 n명이 필요한 경우
            cnt += a[i]//C
            if a[i]%C != 0:
                cnt += 1

print(cnt)
