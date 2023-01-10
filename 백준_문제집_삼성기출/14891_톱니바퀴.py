import sys
wheel = [sys.stdin.readline().strip() for _ in range(4)]
K = int(sys.stdin.readline().strip())
# print(wheel)
def rotate(chk, idx, d):
    chk[idx] = True
    if idx-1 >= 0 and not chk[idx-1]:
        if wheel[idx-1][2] != wheel[idx][6]:  # 극이 다르면
            chk[idx-1] = True
            rotate(chk, idx-1, d * (-1))

    if idx+1 < 4 and not chk[idx+1]:
        if wheel[idx+1][6] != wheel[idx][2]:
            chk[idx+1] = True
            rotate(chk, idx+1, d * (-1))

    if d == 1: #시계방향
        wheel[idx] = wheel[idx][7]+ wheel[idx][0:7]
    else:
        wheel[idx] = wheel[idx][1:] + wheel[idx][0]
    # print(wheel)

for _ in range(K):
    n, di = map(int, sys.stdin.readline().split())
    chk = [False] * 4
    rotate(chk, n-1, di)

# print(wheel)
res = 0
for i in range(4):
    if wheel[i][0] == '0':
        continue
    else:
        res += 2 ** i
print(res)
