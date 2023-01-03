from collections import deque
import sys
n, w, l = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

t = 0
now = 0
in_bridge = []
out_bridge = []
while len(out_bridge) < n:

    if len(in_bridge) > 0 and in_bridge[0][1] > w: # 선두 트럭 다리 건넜는지?
        out_bridge.append(in_bridge[0])
        now -= in_bridge[0][0]
        in_bridge.pop(0)

    if len(trucks) != 0:
        if len(in_bridge) < w and now+trucks[0] <= l: # 진입 가능
            in_bridge.append([trucks[0], 1])
            now += trucks[0]
            trucks.pop(0)
    for truck in in_bridge: # 다리 위 트럭 시간 +1
        truck[1] += 1

    # print(in_bridge)
    t += 1

print(t)