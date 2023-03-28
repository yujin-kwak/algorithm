from collections import deque
N, M = map(int, input().split())
Q = [(idx, value) for idx, value in enumerate(list(map(int, input().split())))]
Q = deque(Q)
count = 0

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        count += 1
        if cur[0] == M:
            print(count)
            break