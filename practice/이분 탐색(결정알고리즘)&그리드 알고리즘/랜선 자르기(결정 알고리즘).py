def count_fn(length): # k개의 랜선으로 length 길이의 랜선을 만들 수 있는 개수
    cnt = 0
    for x in line:
        cnt += (x // length)
    return cnt

k, n = map(int, input().split()) # k: 가지고있는 랜선의 개수, n: 같은 길이의 랜선으로 만들 개수
line = [] # k개의 리스트 저장할 변수
res = 0 # n개의 랜선을 만들 수 있는 최대 길이
largest = 0 # 주어진 랜선 중 가장 긴 랜선(범위)

for i in range(k):
    temp = int(input())
    line.append(temp)
    largest = max(largest, temp) # largest와 temp 중 큰 값을 저장

lt = 1 # 범위의 왼쪽 지점
rt = largest # 범위의 오른쪽 지점

while lt <= rt:
    mid = (lt + rt) // 2
    if count_fn(mid) >= n: # 답으로 가능
        res = mid
        lt = mid + 1 # 더 좋은 답을 찾기 위해 범위 변경 (더 큰 경우 봄)
    else: # 답으로 가능하지 않음
        rt = mid - 1 # 현재 값보다 더 큰 값은 답으로 가능하지 않음, 작은 부분만 본다.

print(res)