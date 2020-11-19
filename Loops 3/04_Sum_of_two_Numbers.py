first_number = int(input())
second_number = int(input())
third_number = int(input())

n_combination = 0
is_the_right_combination = False

x_1 = 0
y_1 = 0

for x in range(first_number, second_number + 1):
    for y in range(first_number, second_number + 1):
        n_combination += 1
        if x + y == third_number:
            is_the_right_combination = True
            x_1 = x
            y_1 = y
            break
    if is_the_right_combination:
        break

if is_the_right_combination:
    print(f"Combination N:{n_combination} ({x_1} + {y_1} = {third_number})")
else:
    print(f"{n_combination} combinations - neither equals {third_number}")
