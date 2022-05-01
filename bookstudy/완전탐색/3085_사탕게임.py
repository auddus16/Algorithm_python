import sys

N = int(sys.stdin.readline().strip())
b = list(list(sys.stdin.readline().strip()) for _ in range(N))
ans = 0
def check(a):
    global ans
    for i in range(N):
        cnt_r = 1
        cnt_c = 1
        for j in range(1, N):
            if  a[i][j-1] == a[i][j]:
                cnt_r +=1
            else:
                cnt_r = 1
            if a[j-1][i] == a[j][i]:
                cnt_c +=1
            else:
                cnt_c = 1
            ans = max(ans, max(cnt_r, cnt_c))

for i in range(N):
    for j in range(N):
        if j+1 < N:
            if b[i][j] != b[i][j+1]: # 행
                b[i][j], b[i][j+1] = b[i][j+1], b[i][j]
                check(b)
                b[i][j], b[i][j+1] = b[i][j+1], b[i][j]

            if b[j][i] != b[j+1][i]: # 열
                b[j][i], b[j+1][i] = b[j+1][i], b[j][i]
                check(b)
                b[j][i], b[j+1][i] = b[j+1][i], b[j][i]

print(ans)
