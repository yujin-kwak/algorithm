T = int(input())
arr = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for test_case in range(1, T + 1):
    T, T_len = input().split()
    in_arr = list(input().split())
    new_arr = []

    for i in range(len(in_arr)):
        for j in range(10):
            if in_arr[i] == arr[j]:
                new_arr.append(j)
                break

    new_arr.sort()
    res = []
    for i in new_arr:
        res.append(arr[i])

    print("{}".format(T), *res)