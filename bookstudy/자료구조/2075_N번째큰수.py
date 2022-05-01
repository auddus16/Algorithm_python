import heapq
import sys
N = int(sys.stdin.readline().strip())
h = []
for _ in range(N):
    for j in map(int, sys.stdin.readline().split()):
        if len(h) >= N:
            heapq.heappushpop(h, j) # heap에 push하고 정렬된 후 pop연산
        else:
            heapq.heappush(h, j)
print(heapq.heappop(h))

