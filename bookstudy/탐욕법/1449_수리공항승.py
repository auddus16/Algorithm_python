import sys
N, L = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a.sort() # 항상 왼쪽부터 효율적으로 붙이기 위해
e = 0
cnt = 0
for i in a:
    if e < i+0.5: # 새로 붙여
        cnt += 1
        e = i-0.5 + L
print(cnt)