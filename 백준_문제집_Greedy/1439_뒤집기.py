import sys
S = sys.stdin.readline().strip()
a = [0, 0]

i = 1
s = S[0]
a[int(s)] += 1
cnt = 1
while i<len(S):
    # print(i)
    if s == S[i]:
        cnt += 1
    else:
        # print(i)
        a[int(S[i])] += 1
        s = S[i]
        cnt = 1
    i+=1
# print(a)
print(min(a))