a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 + n2)
        elif x == '-':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 - n2)
        elif x == '*':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 * n2)
        elif x == '/':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n1 / n2)

print(stack[0])