import sys, heapq

def dijkstra(v, s, adj):
    dist = [int(1e9)] * (v+1) # 최단경로 배열
    dist[s] = 0 # 시작점은 최단경로 0으로 초기화
    hp = []
    heapq.heappush(hp, [0, s]) # 가중치0, 노드0

    while hp:
        cost, node = heapq.heappop(hp) # 최소힙에서 가장 가까운 노드 선택
        for n, c in adj[node]: # node와 인접한 노드
            c += cost
            if c<dist[n]:
                dist[n] = c
                heapq.heappush(hp, [c, n])
    return dist

V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())

adj = [[] for _ in range(V+1)] # 인접리스트 1:(2, 2), (3, 3) -> 1번 노드의 인접리스트!
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    adj[u].append((v, w))

for res in dijkstra(V, K, adj)[1:]:
    print(res if res != int(1e9) else 'INF')