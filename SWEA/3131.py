res = []

N = 1000000
M = N ** 0.5

num = [1] * N
num[0] = 0
num[1] = 0
for i in range(2, int(M) + 1):
    if num[i] == 1:
        for j in range(i+i, N, i):
            num[j] = 0

for i in range(N):
    if num[i] == 1:
        res.append(i)

print(*res)