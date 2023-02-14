import sys, heapq
N = int(sys.stdin.readline().strip())
a = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
a.sort(key=lambda x : (x[0], x[1]))
room = []
for i in a:
    if not room: # 맨처음
        heapq.heappush(room, i[1])
    else: # 새로운 강의실 배정
        if room[0] > i[0]:
            heapq.heappush(room, i[1])
        else: # 현재 강의실 값 갱식
            heapq.heappop(room)
            heapq.heappush(room, i[1])
print(len(room))