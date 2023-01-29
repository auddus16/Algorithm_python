import sys, heapq
N, M = map(int, sys.stdin.readline().strip().split())
card = list(map(int, sys.stdin.readline().strip().split()))
heapq.heapify(card)

for _ in range(M):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    new = a+b
    for _ in range(2):
        heapq.heappush(card, a+b)
print(sum(card))