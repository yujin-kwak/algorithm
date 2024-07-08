import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = []
result = 0

for i in range(N):
    heapq.heappush(queue, int(input().rstrip()))

while len(queue) >= 2:
    A = heapq.heappop(queue)
    B = heapq.heappop(queue)
    result += int(A + B)
    heapq.heappush(queue, (A + B))

print(result)




