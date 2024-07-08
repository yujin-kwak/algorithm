import sys
import heapq
input = sys.stdin.readline

N =int(input())
numbers = []

for i in range(N):
    x = int(input())

    if x == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)

    else:
        heapq.heappush(numbers, x)