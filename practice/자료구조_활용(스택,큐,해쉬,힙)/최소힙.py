import heapq as hq

a=[]
while True:
    N = int(input())
    if N == -1:
        break
    if N == 0:
        if a:
            print(hq.heappop(a))
        else:
            print(-1)
    else:
        hq.heappush(a, N) # 힙 불변성을 유지하면서, item 값(N)을 heap(a)으로 푸시합니다.
                          # 기본적으로 heapq모듈은 최소 힙 구조
