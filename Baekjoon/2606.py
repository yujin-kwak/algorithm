import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited[1] = 1
queue = deque([1])

while queue:
    current = queue.popleft()
    if G[current]:
        for i in G[current]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)

print(sum(visited) - 1)

