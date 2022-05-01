import sys
a = list(list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip())))
a.sort(key=lambda x:(x[1], x[0]))
ans = 0
s = 0
for i in a:
    if s <= i[0]:
        s = i[1]
        ans += 1
print(ans)