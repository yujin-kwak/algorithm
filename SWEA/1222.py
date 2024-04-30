for test_case in range(1, 11):
    N = int(input())
    ans = []
    stack = []
    res = []
    string = input()

# 후위 표기식 만들기
    for i in string:
        if i == "+":
            if not stack:
                stack.append(i)
            else:
                ans += stack.pop()
                stack.append(i)
        else:
            ans.append(i)
    
    while stack:
        ans += stack.pop()

#후위 표기식 계산
    for i in ans:
        if i == "+":
            num2 = res.pop()
            num1 = res.pop()
            res.append(num1 + num2)
        else:
            res.append(int(i))

    print("#{} {}".format(test_case, *res))