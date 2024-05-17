T = int(input())
arr = []
for i in range(1, 10):
    for j in range(1, 10):
        if (i * j) not in arr:
            arr.append(int(i * j))

for test_case in range(1, T + 1):
    N = int(input())
    if N in arr:
        res = "Yes"
    else:
        res = "No"

    print("#{} {}".format(test_case, res))