"""
Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.


вход	изход
5
10
20
304
0
50	Max number: 304
    Min number: 0

"""


# import sys
#
# smallest = sys.maxsize
# biggest = -sys.maxsize
#
# n = int(input())
# for i in range(0, n):
#     num = int(input())
#     if num < smallest:
#         smallest = num
#     if num > biggest:
#         biggest = num
#
# print(f'Max number: {biggest}')
# print(f'Min number: {smallest}')

def max_min_num(n):
    list_nums = [int(input()) for _ in range(n)]
    print(f'Max number: {max(list_nums)}')
    print(f'Min number: {min(list_nums)}')

n = int(input())
max_min_num(n)
