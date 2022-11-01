import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
multi = []
cnt = 0
for i, v in enumerate(a):
    if v in multi: # V가 이미 멀티탭에 꽂혀있는 경우
        continue
    elif len(multi) < n: # 멀티탭에 자리가 있는 경우 -> 그냥 꽂으면 됨.
        multi.append(v)
    else: # 빼고 꽂아야 하는 경우
        cnt += 1
        flag = False
        nxt = (-1, 0) # a에서 idx, 뺄 곳(multi) idx
        for j, val in enumerate(multi): # 멀티탭에서 가장 나중에 사용되는 제품을 찾아 갱신
            if val in a[i+1:]: # 이후에 사용된다면,
                nxt_idx = a[i+1:].index(val)
                if nxt[0] < nxt_idx: # 가장 나중에 사용되는 걸로 갱신해준다.
                    nxt = (nxt_idx, j)
            else: # 이후 사용되지 않는 전기용품이 있다면 그걸로 선택
                flag = True
                multi[j] = v
                break
        if not flag:
            multi[nxt[1]] = v

print(cnt)
