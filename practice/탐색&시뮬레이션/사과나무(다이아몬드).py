n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
res = 0
s = e = n // 2  # 시작 지점과 끝 지점 변수 사용

for i in range(n):
    for j in range(s, e+1): # s부터 e까지의 값만 res에 저장
        res += board[i][j]
    if i < n // 2:  # i가 n//2보다 작으면 시작점이 작아지고 끝점이 커져야 함.
        s -= 1
        e += 1
    else: # 그 외에는 시작점이 커지고 끝점이 작아져야 함.
        s += 1
        e -= 1

print(res)