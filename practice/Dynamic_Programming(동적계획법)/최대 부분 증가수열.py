n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)  #arr배열의 0번 인덱스에 0을 넣어서 1번 인덱스부터 사용할 수 있도록 함
dy = [0] * (n+1)
dy[1] = 1
res = 0 # 최대 길이

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)