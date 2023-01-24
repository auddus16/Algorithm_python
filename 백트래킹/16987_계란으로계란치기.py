n = int(input())
s = [0]*n # 내구도
w = [0]*n # 무게

for i in range(n):
    s[i], w[i] = map(int, input().split())

res = 0 
def solve(idx, eggs):
    global res
    if idx == n: # 가장 최근에 든 계란이 마지막 계란
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt +=1
        if cnt > res:
            res = cnt
        return

    if eggs[idx] > 0:
        for i in range(n): # 부딪힐 계란 탐색 (깨지면 손에 든 계란을 내려놓고, 재귀)
            flag = False
            if eggs[i] > 0 and i != idx: # 깨졌다! 내구도 0 이상, 자기자신 제외
                flag = True
                tmp = eggs[:] # 내구도 갱신
                tmp[i] -= w[idx]
                tmp[idx] -= w[i]
                solve(idx+1, tmp) # 재귀(다음 계란을 쥔다.)
        if not flag: # 깨지지 않은 다른 계란이 없는 경우, 다음 계란을 쥔다.
            solve(idx+1, eggs)
    else: # 이미 깨진 계란이라면, 바로 다음 계란으로 넘어간다.
        solve(idx+1, eggs)

solve(0, s)
print(res)