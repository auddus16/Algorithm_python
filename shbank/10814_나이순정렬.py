import sys
N = int(sys.stdin.readline().strip())
a = []
for i in range(N):
    s = sys.stdin.readline().split()
    a.append((int(s[0]), s[1], i))
a.sort(key=lambda x : (x[0], x[2]))

for i in a:
    print(f'{i[0]} {i[1]}')