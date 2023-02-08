import sys
from collections import defaultdict
N, K = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))

maxV = 0
left, right, cnt = 0, 0, defaultdict(int)
while right < N:
    if cnt[a[right]] < K:
        cnt[a[right]] += 1
        right += 1
    else:
        cnt[a[left]] -= 1
        left += 1
    maxV = max(maxV, right-left)

print(maxV)