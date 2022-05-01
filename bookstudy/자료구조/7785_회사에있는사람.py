import sys
N = int(sys.stdin.readline().strip())
a = set()
for i in range(N):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        a.add(name)
    else:
        a.remove(name)

for i in sorted(a, reverse=True):
    print(i)
