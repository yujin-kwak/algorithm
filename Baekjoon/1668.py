import sys
input = sys.stdin.readline

N = int(input())
high = []

for _ in range(N):
    high.append(int(input()))

count_left = 0
max_left = 0
for i in high:
    if max_left < i:
        max_left = i
        count_left += 1

count_right = 0
max_right = 0
for i in range(N-1, -1, -1):
    if max_right < high[i]:
        max_right = high[i]
        count_right += 1

print(count_left)
print(count_right)