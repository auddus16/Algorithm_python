from collections import Counter
import sys
cnt=Counter(sys.stdin.readline().strip())
if sum(i%2 for i in cnt.values())>1: # 홀수 개 알파벳이 2개 이상일 경우 -> 불가능
    print("I'm Sorry Hansoo")
else:
    left=''
    for ch, n in sorted(cnt.items()): # 사전순 정렬
        left+=ch*(n//2) # 왼쪽 절반('A' 3개라면,  1개 붙인다.) -> 홀짝 검사 X
    res=left
    for ch, n in cnt.items(): # 홀수 개 알파벳은 가운데 붙인다.
        if n%2 ==1: # 홀수 개 알파벳은 1개 이하로 존재-> break
            res+=ch
            break
    res+=''.join(reversed(left)) # 왼쪽 절반 구해놓은 걸 반전해서 오른쪽에 붙이기
    print(res)