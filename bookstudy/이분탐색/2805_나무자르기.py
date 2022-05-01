import sys
N, M = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
t.sort()
lo = 0
hi = max(t)
mid = (lo + hi)//2
def get_total_tree(h):
    sum = 0
    for i in t:
        if i > h:
            sum += i-h
    return sum
ans = 0
while lo <= hi:
    if get_total_tree(mid) >= M:
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
    mid = (lo+hi)//2
print(ans)


