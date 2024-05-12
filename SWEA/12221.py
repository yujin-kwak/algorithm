T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())

    res = 0
    if A >= 10 or B >= 10:
        res = -1
    else:
        res = A * B
    
    print("#{} {}".format(test_case, res))