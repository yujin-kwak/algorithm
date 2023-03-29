'''
str1 = input()
str2 = input()
check = dict()

for i in str1:
    check[i] = check.get(i,0) + 1

for j in str2:
    check[j] = check.get(j,0) - 1

for x in check.values():
    if x != 0:
        print("NO")
        break
else:
    print("YES")
'''

#딕셔너리 사용 x
str1 = input()
str2 = input()
check = [0] * 52

for x in str1:
    if x.isupper():
        check[ord(x)-65] += 1
    else:
        check[ord(x)-71] += 1

for x in str2:
    if x.isupper():
        check[ord(x)-65] -= 1
    else:
        check[ord(x)-71] -= 1

for i in range(52):
    if check[i] != 0:
        print("NO")
        break
else:
    print("YES")