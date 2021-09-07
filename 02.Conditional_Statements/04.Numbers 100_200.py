number = int(input())

if number < 100:
    print("Less than 100")
elif number <= 200:
    print("Between 100 and 200")
else:
    print("Greater than 200")

class Checker:

    def __init__(self, number):
        self.number = number

    def less_100(self):
        if self.number < 100:
            return "Less than 100"

    def between_100_and_200(self):
        if 100 <= self.number <= 200:
            return "Between 100 and 200"

    def greater_than_200(self):
        if self.number > 200:
            return "Greater than 200"

number = int(input())

check_number = Checker(number)

print(check_number)