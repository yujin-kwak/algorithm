import sys
input = sys.stdin.readline

N = int(input())

k = 1
count = 0
while N > 0:
    if k > N:
        k = 1
    N -= k
    k += 1
    count += 1

print(count)