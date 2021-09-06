"""

Напишете програма, която изчислява необходимите средства,
които Божидара ще трябва да заплати на фирмата изпълнител на проекта.
Цената на един кв. м. е 7.61лв със ДДС.
Тъй като нейният двор е доста голям,
фирмата изпълнител предлага 18% отстъпка от крайната цена.
От конзолата се прочита само един ред:
1.	Кв. метри, които ще бъдат озеленени – реално число.

На конзолата се отпечатват два реда:
•	"The final price is: {крайна цена на услугата} lv."
•	"The discount is: {отстъпка} lv."

"""


def landscape_expenses(m, price, discount):
    price = m * price
    discount_price = price * (discount / 100)
    total_price = price - discount_price
    print(f"The final price is: {total_price} lv.\n"
          f"The discount is: {discount_price} lv.")


m = int(input())
price = 7.61
discount = 18  # %

landscape_expenses(m, price, discount)

# 550  - > 3432.11
# 150  - > 205.47
