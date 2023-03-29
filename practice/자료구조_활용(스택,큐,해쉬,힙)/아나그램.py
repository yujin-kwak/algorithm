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
