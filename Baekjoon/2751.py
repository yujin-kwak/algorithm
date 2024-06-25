import sys
input = sys.stdin.readline

# def quick_sort(numbers):
#     if len(numbers) <= 1:
#         return numbers
#
#     pivot = numbers[len(numbers) // 2]
#     small, equal, big = [], [], []
#
#     for n in numbers:
#         if n < pivot:
#             small.append(n)
#         elif n > pivot:
#             big.append(n)
#         else:
#             equal.append(n)
#
#     return quick_sort(small) + equal + quick_sort(big)

N = int(input())

numbers = []
for i in range(N):
    num = int(input())
    numbers.append(num)

# res = quick_sort(numbers)

numbers.sort()

for i in numbers:
    print(i)

