import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dist = [0] * 100001
queue = deque()
queue.append(N)

while queue:
    current = queue.popleft()
    if current == M:
        print(dist[current])
        break
    for i in (current - 1, current + 1, current * 2):
        if 0 <= i <= 100000 and not dist[i]:
            dist[i] = dist[current] + 1
            queue.append(i)

