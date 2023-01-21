import sys, heapq
N, E = map(int, sys.stdin.readline().strip().split())
adj = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    adj[a].append((b, c))
    adj[b].append((a, c))
v1, v2 = map(int, sys.stdin.readline().strip().split())

def dijkstra(N, start, adj):
    dist = [int(1e9)]*(N+1)
    hp = []
    heapq.heappush(hp, (0, start))
    dist[start] = 0

    while hp:
        cost, node = heapq.heappop(hp)
        for n, c in adj[node]:
            c += cost
            if c < dist[n]:
                dist[n] = c
                heapq.heappush(hp, (c, n))

    return dist

d1 = dijkstra(N, 1, adj) # 1시작

d2 = dijkstra(N, v1, adj) # v1시작

d3 = dijkstra(N, v2, adj) # v2시작

res = min(d1[v1]+d2[v2]+d3[N], d1[v2]+d3[v1]+d2[N]) # 총 2가지 경우의 수 존재

print(res if res < int(1e9) else -1)
