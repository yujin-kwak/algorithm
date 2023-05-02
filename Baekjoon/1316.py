n = int(input()) # 그룹 단어의 개수

count = 0
for _ in range(n):
    input_str = input()
    check = [0] * 26
    pre = -1 # pre 임의 값 지정 (초기)
    for x in input_str:
        tmp = ord(x) - 97

        if check[tmp] == 0:
            check[tmp] = 1
        elif check[tmp] == 1 and pre == tmp:
            continue
        else:
            break

        pre = tmp # 이전값 저장
    else:
        count += 1

print(count)