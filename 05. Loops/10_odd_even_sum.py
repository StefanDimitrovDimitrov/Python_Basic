"""

Да се напише програма, която чете n-на брой цели числа, подадени от потребителя,
и проверява дали сумата от числата на четни позиции е равна на сумата на числата на нечетни позиции.
При равенство да се отпечатат два реда:
"Yes" и на нов ред "Sum = " + сумата; иначе да се отпечата "No" и на нов ред "Diff = " + разликата.
Разликата се изчислява по абсолютна стойност.

вход	изход	коментар
4
10
50
60
20

            Yes
            Sum = 70	10+60 = 50+20 = 70

"""


n = int(input())
even_sum = []
odd_sum = []

[even_sum.append(int(input())) if i % 2 == 0 else odd_sum.append(int(input())) for i in range(n)]

if sum(even_sum) == sum(odd_sum):
    print(f"Yes")
    print(f'Sum = {sum(even_sum)}')
else:
    print(f"No")
    print(f'Diff = {abs(sum(even_sum) - sum(odd_sum))}')