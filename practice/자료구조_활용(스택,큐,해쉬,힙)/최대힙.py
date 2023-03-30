import heapq as hq

a=[]
while True:
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if a:
            print(-hq.heappop(a))
        else:
            print(-1)
    else:
        hq.heappush(a, -N)