
"""

Да се напише програма,
която чете две цели числа въведени от потребителя и отпечатва по-голямото от двете.
"""

def greater_number(first_number, second_number):
    print(first_number if first_number > second_number else second_number)


first_number = int(input())
second_number = int(input())

greater_number(first_number, second_number)
