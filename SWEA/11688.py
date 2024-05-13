T = int(input())

for test_case in range(1, T + 1):
    input_str = list(input())
    a = 1
    b = 1
    for i in range(len(input_str)):
        if input_str[i] == 'L':
            b = a + b
        else:
            a = a + b
    print("#{} {} {}".format(test_case, a, b))