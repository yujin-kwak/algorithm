import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    G[B].append(A)

def bfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque()
    queue.append(start)
    count = 0

    while queue:
        current = queue.popleft()

        for x in G[current]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)
                count += 1

    return count

res = []
for i in range(1, len(G)):
    res.append(bfs(i))

for i in range(len(res)):
    if res[i] == max(res):
        print(i + 1, end = ' ')