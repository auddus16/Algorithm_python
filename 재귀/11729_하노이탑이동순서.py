import sys
N= int(sys.stdin.readline())
def hanoi(n, s, e):
    if n==1:#원판이 1개인 경우 s, e출력후 리턴
        print(s, e)
        return
    hanoi(n-1, s, 6-s-e)#1단계: n-1개 원판을 1->2
    print(s, e)#2단계: 1개를 1->3
    hanoi(n-1, 6-s-e, e)#3단계: n-1개 원판을 2->3
print(2**N-1)
hanoi(N, 1, 3)