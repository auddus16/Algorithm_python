import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().strip().split())
A = [[5]*N for _ in range(N)]
A1 = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
board = [[deque() for _ in range(N)]for _ in range(N)]

for _ in range(M):
    x, y, age = map(int, sys.stdin.readline().strip().split())
    board[x-1][y-1].append(age)


# board.sort()
# print(board)
for _ in range(K):
    # 봄 + 여름
    for i in range(N):
        for j in range(N):
            next = 0  # 여름에 양분으로 변할 양
            if len(board[i][j]) > 0: # 나무 존재
                a = A[i][j]
                hq = [] # 남아 있는 나무 저장 리스트
                while True:
                    if not board[i][j]:
                        board[i][j] = hq
                        break

                    # heapq.heapify(board[i][j])
                    tree = board[i][j].popleft()
                    # print(f'x:{i}, y:{j} age:{tree}')
                    if a < tree:
                        # 나이 못 먹음.. 나머지 나무 다 죽어
                        next += tree//2
                        for t in board[i][j]:
                            next += t//2
                        board[i][j] = hq
                        break
                    else: # 나이 먹기
                        a -= tree
                        hq.append(tree+1)
                        # heapq.heappush(hq, tree+1)

                A[i][j] = a
            A[i][j] += next

    # 가을
    dx = (-1, -1, -1, 0, 0, +1, +1, +1)
    dy = (-1, 0, +1, -1, +1, -1, 0, +1)
    for i in range(N):
        for j in range(N):
            for t in board[i][j]:
                if t % 5 == 0: # 5배수 나이 나무
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0<=nx<N and 0<=ny<N:
                            board[nx][ny].appendleft(1)
    # 겨울
    for i in range(N):
        for j in range(N):
            A[i][j] += A1[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(board[i][j])
print(cnt)



