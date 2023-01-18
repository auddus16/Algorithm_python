import sys, heapq
N, M = map(int, sys.stdin.readline().strip().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    adj[a].append((b, c)) # 양방향 그래프
    adj[b].append((a, c))
hp = []
dist = [int(1e9)] * (N+1)
heapq.heappush(hp, (0, 1))
dist[1] = 0

while hp:
    cost, node = heapq.heappop(hp)
    for n, c in adj[node]:
        c += cost
        if c<dist[n]:
            dist[n] = c
            heapq.heappush(hp, (c, n))
print(dist[N])