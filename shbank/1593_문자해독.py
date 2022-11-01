import sys
g, N = map(int, sys.stdin.readline().strip().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

wl = [0] * 58
sl = [0] * 58
# W의 각 알파벳마다 등장부분 +1
for i in W:
    wl[ord(i) - 65] += 1

start, cnt, length = 0, 0, 0
for i in range(N):
    sl[ord(S[i]) - 65] += 1
    length += 1

    if length == g:
        if wl == sl:
            cnt += 1
        sl[ord(S[start]) - 65] -= 1

        start += 1
        length -= 1

print(cnt)

