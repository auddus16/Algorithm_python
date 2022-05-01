import heapq
import sys
N = int(sys.stdin.readline().strip())
h = []
for i in range(N):
    a = int(sys.stdin.readline().strip())
    if a == 0:
        print(heapq.heappop(h)[1] if len(h) else 0)

    else:
        heapq.heappush(h, (abs(a), a)) # (절댓값, 원본값) -> 튜플로 저장. 절댓값을 우선으로 정렬. 같을 경우 원본값 정렬

