n = int(input()) # 1부터 n까지의 수열
reverse_num = list(map(int, input().split())) # 역수열
num = [0] * n # 원수열 만들 리스트

for i in range(n):
    for j in range(n):
        if reverse_num[i] == 0 and num[j] == 0:
            num[j] = i + 1
            break
        elif num[j] == 0:
            reverse_num[i] -= 1


print(num)
