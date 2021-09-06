"""

Напишете програма, която пресмята нужните разходи за закупуването на храна за кучета и други животни.
Една опаковка храна за кучета е на цена 2.50лв., а всяка останала, която не е за тях струва 4лв.
Вход
От конзолата се четат 2 реда:
1.	Броят на кучетата - цяло число;
2.	Броят на останалите животни  - цяло число.
Изход
На конзолата се отпечатва:



"""

def food_expenses(num_dogs, num_others, food_price_dog, food_price_others):
    total = float(num_dogs*food_price_dog + num_others*food_price_others)
    print(f'{total} lv.')

num_dogs = int(input())
num_others = int(input())
dog_food_price = 2.5
others_food_price = 4

food_expenses(num_dogs, num_others,dog_food_price, others_food_price)

# dog - 5 others - 4 result 28.5 lv
# dog - 13 others - 9 result 68.5 lv





