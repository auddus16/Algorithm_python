import sys
# T = int(sys.stdin.readline().rstrip())
# for _ in range(T):
#     n = int(sys.stdin.readline().strip())
#     a = list(map(int, sys.stdin.readline().strip().split()))
#
#     maxV = max(a)
#     i = 0
#     res = 0
#     while i<n:
#         if a[i]<maxV: #매수
#             res += maxV - a[i]
#         elif a[i]==maxV: #최대값 갱신
#             if i+1 < n:
#                 maxV = max(a[i+1:])
#         i += 1
#     print(res)
#시간 초과 해결
for _ in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    answer = 0
    mx = data[-1] # 최대값을 맨 뒤에 원소로 지정
    for i in range(n-2,-1,-1):
        if data[i] > mx: #오늘 가격이 mx라면
            mx = data[i]
        else:
            answer += mx-data[i] #오늘 가격이 최대가 아니라면 최대-지금가격만큼 더한다
    print(answer)