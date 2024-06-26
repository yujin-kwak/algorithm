import sys
input = sys.stdin.readline

n = int(input())
p = [0] * (n + 1)

# def fibonacci(n):
#     if n == 0:
#         p[0] = 0
#     elif n == 1:
#         p[1] = 1
#     elif p[n] == 0:
#         p[n] = fibonacci(n - 1) + fibonacci(n - 2)
#     return p[n]

if n == 0:
    p[0] = 0
    print(p[0])
elif n == 1:
    p[1] = 1
    print(p[1])
else:
    p[0] = 0
    p[1] = 1
    for i in range(2, n + 1):
        p[i] = p[i-1] + p[i-2]
    print(p[n])