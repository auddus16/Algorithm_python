import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    board = [0] * (N+1)
    for _ in range(N-1):
        r, c = map(int, sys.stdin.readline().strip().split())
        board[c] = r
    a, b = map(int, sys.stdin.readline().strip().split())

    # 부모노드 리스트 생성
    a_parents, b_parents = [0, a], [0, b]
    while board[a]:
        a_parents.append(board[a])
        a = board[a]

    while board[b]:
        b_parents.append(board[b])
        b = board[b]

    # 뒤에서부터(루트노드부터) 달라지는 지점 바로 직전이 가장 가까운 공통 조상
    i = 1
    while a_parents[-i] == b_parents[-i]:
        i += 1
    print(a_parents[-i+1])

