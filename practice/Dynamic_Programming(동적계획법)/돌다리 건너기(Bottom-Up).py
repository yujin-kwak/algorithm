n = int(input())
dy = [0] * (n+2)

dy[1] = 1
dy[2] = 2

for i in range(3, n+2): #마지막 돌 다음 땅으로 가는 방법까지 고려해야함
    dy[i] = dy[i-2] + dy[i-1]

print(dy[n+1])
