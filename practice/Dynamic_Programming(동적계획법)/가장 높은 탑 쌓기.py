n = int(input())
bricks = []

for i in range(n):
    s, h, w = map(int, input().split())
    bricks.append((s, h, w)) # s: 넓이, h: 높이, w:무게
bricks.sort(reverse = True) # s에 대해 내림차순, s가 같으면 h에 대해, h도 같으면 w에 대해
dy=[0] * n
dy[0] = bricks[0][1] #0번 벽돌의 높이(h)
res = bricks[0][1]

for i in range(1, n):
    max_h = 0
    for j in range(i-1, -1, -1):
        if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
            max_h = dy[j]
    dy[i] = max_h + bricks[i][1]
    res = max(res, dy[i])

print(res)

