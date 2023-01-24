h, w = map(int, input().split())
world = list(map(int, input().split()))

ans = 0
for i in range(1, w - 1):
    left_max = max(world[:i])
    right_max = max(world[i+1:])

    compare = min(left_max, right_max)

    if world[i] < compare: # 현재위치 - 양옆 최대블럭 중 최소
        ans += compare - world[i]

print(ans)