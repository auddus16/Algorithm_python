import sys
C = int(sys.stdin.readline().strip())

def find(x):
    if x == parent[x]:
        return x
    p = find(parent[x])
    parent[x] = p

    return p

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x # y를 x의 root 노드의 자식으로
        number[x] += number[y] # y 친구 수 더하기

for _ in range(C):
    T = int(sys.stdin.readline().strip())
    parent, number = {}, {}
    for _ in range(T):
        a, b = sys.stdin.readline().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a, b)

        print(number[find(a)])