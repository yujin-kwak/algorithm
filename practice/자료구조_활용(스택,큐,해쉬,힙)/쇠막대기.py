li = input()
stack = []
count = 0

for i in range(len(li)):
    if li[i] == '(':
        stack.append(li[i])
    else:
        stack.pop()
        if li[i-1] == '(':
            count += len(stack)
        else:
            count += 1

print(count)