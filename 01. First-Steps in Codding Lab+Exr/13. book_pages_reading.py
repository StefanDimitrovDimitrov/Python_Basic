"""
Вход
От конзолата се четат 3 реда:
1.	Брой страници в текущата книга – цяло число;
2.	Страници, които може да прочита за 1 час – цяло число;
3.	Броя на дните, за които трябва да прочете книгата – цяло число;
Изход
Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.

Вход	Изход
212
20
2	5.3
Вход	Изход
432
15
4	7.2


"""


def needed_time_book_reading(pages, pages_per_hour, days):
    total_time = pages / pages_per_hour
    needed_hours_per_day = total_time / days
    print(needed_hours_per_day)


pages = int(input())
pages_per_hour = int(input())
days = int(input())

needed_time_book_reading(pages, pages_per_hour, days)
