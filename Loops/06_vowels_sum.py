"""
Да се напише програма, която чете текст (стринг), въведен от потребителя,
и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:

"""

dict = {"a":1,"e":2,"i":3,"o":4,"u":5}

def sum_values(word):
    return sum([dict[i] for i in word if i in dict])
word = input()

print(sum_values(word))

