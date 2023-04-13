from collections import deque

n, m = map(int, input().split()) # n: 일의 개수, m: 순서 정보의 개수
graph = [[0] * (n + 1) for _ in range(n + 1)]
degree = [0] * (n + 1)
dq = deque()

# 초기화 (방향, 진입 차수)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1

# 차수가 0이면 queue에 넣음
for i in range(1, n + 1):
    if degree[i] == 0:
        dq.append(i)

# dq에서 꺼낸 일 다음 수행해야 하는 일의 진입 차수 1 감소
# 감소 후 진입 차수가 0이 되었다면 다시 queue에 넣음
while dq:
    x = dq.popleft()
    print(x, end = ' ')
    for i in range(1, n + 1):
        if graph[x][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                dq.append(i)