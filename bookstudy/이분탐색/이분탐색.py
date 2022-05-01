from bisect import bisect_left, bisect_right
a = [2, 3, 6, 6, 6, 10, 12, 15] # 총 8개 -> 기준은 4번째 값 -> mid = a[3]
l = bisect_left(a, 5) # a에서 목표값 6보다 같거나 큰 첫번째 값의 위치를 반환
r = bisect_right(a, 5) # a에서 목표값 6보다 큰 첫번째 값의 위치를 반환
print(l)
print(r)