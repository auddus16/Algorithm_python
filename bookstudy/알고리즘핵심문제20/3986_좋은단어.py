import sys
N = int(sys.stdin.readline().strip())
a = []
for _ in range(N):
    a.append(list(sys.stdin.readline().strip()))

res = 0
for i in range(N):
    stk = []
    for j in range(len(a[i])):
        if not stk: # 스택 비어있을 때
            stk.append(a[i][j])
        else:
            if stk[-1] == a[i][j]:
                stk.pop()
            else:
                stk.append(a[i][j])
    if not stk:
        res += 1
print(res)

