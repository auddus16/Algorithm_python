import sys
s = sys.stdin.readline().strip()
acnt = 0
minV = 9999
for i in s:
    if i == 'a':
        acnt += 1
for i in range(len(s)):
    cnt = 0
    for j in range(i, i+acnt):
        if j>=len(s):
            if s[(j-len(s))%len(s)] == 'b':
                cnt += 1
        else:
            if s[j] == 'b':
                cnt += 1
    minV = min(minV, cnt)
print(minV)