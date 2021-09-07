n = int(input())

left_sum = sum([int(input()) for _ in range(n)])
right_sum = sum([int(input()) for _ in range(n)])


if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(right_sum - left_sum)
    print(f'No, diff = {diff}')
