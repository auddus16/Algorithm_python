import sys
INF=987654321
cache=[INF]*10_000_001 # 초기값, 임시마크=0
A, B, K = map(int, sys.stdin.readline().split())

def S(n): # S(N) 계산하는 함수
    return sum(int(ch) ** K for ch in str(n))

def dfs(n):
    if cache[n] == INF: # 최초 방문한 N
        cache[n] = 0 # 임시마크 해두고 탐색 시작
        cache[n] = min(n, dfs(S(n))) # 최초 수열 n부터
    else:
        # 이미 탐색이 완료된 N이라면, 바로 반환
        if cache[n]:
            return cache[n]
        # 탐색 중인 N. 즉, 임시마크 0이 되어 있는 N
        # cycle 발견.
        # 다시 cycle을 돌면서 최소값을 탐색
        m = n
        nn = S(n)
        while nn != n:
            m = min(m, nn)
            nn = S(nn)

        # cycle에서의 N들의 최소값을 갱신해준다. (현재 m에 최소값 저장되어 있음.)
        cache[n] = m
        nn = S(n)
        while nn != n:
            cache[nn] = m
            nn = S(nn)

    return cache[n]

ans=0
for i in range(A, B+1):
    ans+=dfs(i)
print(ans)