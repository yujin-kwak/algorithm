def check_self_number(x):
    tmp = int(x)
    while x != 0:
        tmp += (x % 10)
        x = x // 10
    if tmp <= 10000:
        check[tmp] = 1

check = [0] * 10001
for i in range(1, 10001):
    check_self_number(i)

for j in range(1, 10001):
    if check[j] == 0:
        print(j)