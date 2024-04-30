for test_case in range(1, 11):
    res = [] #후위표기식 결과 저장 변수
    cal = [] #후위표기식 계산 결과 저장 변수
    stack = []

    N = int(input())
    string = input()

    #후위표기식 만들기
    for i in string:
        if i == '+' or i == '*':
            if not stack:
                stack.append(i)
            else:
                if i == '+':
                    while stack:
                        res += stack.pop()
                    stack.append(i)
                elif i == '*':
                    if stack[-1] == '*':
                        res += stack.pop()
                        stack.append('*')
                    else:
                        stack.append('*')
        else:
            res.append(i)
    
    while stack:
        res += stack.pop()

    #후위표기식 계산하기
    for i in res:
        if i == '+' or i == '*':
            num2 = cal.pop()
            num1 = cal.pop()
            if i == '+':
                cal.append(num1 + num2)
            else:
                cal.append(num1 * num2)
        else:
            cal.append(int(i))

    print("#{} {}".format(test_case, *cal))