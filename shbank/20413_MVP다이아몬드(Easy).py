import sys
N = int(sys.stdin.readline())
mvp = list(map(int, sys.stdin.readline().strip().split()))
a = sys.stdin.readline().strip()

prev = 0
sum = 0
res = []
for i in range(N):
    if a[i] == 'B':
        sum += mvp[0] - prev - 1
        prev = mvp[0] - prev - 1
    elif a[i] == 'S':
        sum += mvp[1] - prev - 1
        prev = mvp[1] - prev - 1
    elif a[i] == 'G':
        sum += mvp[2] - prev - 1
        prev = mvp[2] - prev - 1
    elif a[i] == 'P':
        sum += mvp[3] - prev - 1
        prev = mvp[3] - prev - 1
    else:
        sum += mvp[3]
        prev = mvp[3]

print(sum)
