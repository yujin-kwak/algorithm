arr = list(range(21)) # 0 ~ 20까지의 리스트 만들기

for _ in range(10): # 10번 반복
    s, e = map(int, input().split()) # 구간 읽기
    for i in range((e - s + 1) // 2):
        arr[s + i], arr[e - i]= arr[e - i], arr[s + i]

arr.pop(0) # 0제거
for x in arr:
    print(x, end = ' ')
