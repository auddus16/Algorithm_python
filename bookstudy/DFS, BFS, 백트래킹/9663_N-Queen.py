import sys
N = int(sys.stdin.readline())
ans = 0
col = [False] * N   # i열에 퀸을 놓다.
d1 = [False] * 2 * N
d2 = [False] * 2 * N

def bt(row):
    global ans
    if row == N:    # N개의 퀀을 다 놓은 경우, 경우에 1을 추가한다.
        ans += 1
        return
    for j in range(N):
        if not col[j] and not d1[row-j] and not d2[row+j]:
            col[j] = True
            d1[row-j] = True
            d2[row+j] = True

            bt(row+1)

            col[j] = False
            d1[row-j] = False
            d2[row+j] = False

bt(0)
print(ans)
