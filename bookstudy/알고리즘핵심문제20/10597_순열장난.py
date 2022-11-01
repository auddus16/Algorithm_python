import sys
a = sys.stdin.readline().strip()
cnt = 0 # 순열 숫자 개수(1~cnt)

# 순열의 범위 구하기 = 순열에 있는 숫자의 개수 판별
if len(a) <= 9: # 1자리 수로만 이루어짐.
    cnt = len(a)
else: # 1자리 + 2자리
    cnt = 9+((len(a)-9)//2)
chk = [0 for _ in range(cnt+1)]
ans = [0 for _ in range(cnt)]

res = ''
flag = False
def bt(idx, c):
    global flag, res
    if flag:
        return
    if idx == len(a): # 순열 모두 순회
        if c == cnt: # 숫자 개수 모두 찾았다면, res 출력 후 종료
            flag = True
            res = ' '.join(map(str, ans))
            print(res)
            sys.exit()
        # 그렇지 못하면 다시 회귀
        return

    # 1자리 수
    n1 = int(a[idx])
    if not chk[n1]:
        chk[n1] = True
        ans[c] = n1
        bt(idx+1, c+1)
        chk[n1] = False

    # 2자리 수
    if idx+1 < len(a):
        n2 = int(a[idx:idx+2])
        if n2 <= cnt and not chk[n2]: # 조건 순서 중요함..n2범위 먼저 체크해야 함.
            chk[n2] = True
            ans[c] = n2
            bt(idx+2, c+1)
            chk[n2] = False
bt(0, 0)
# print(ans)
# print(res)