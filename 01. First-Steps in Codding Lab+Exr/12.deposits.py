"""

Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент. Използвайте следната формула:
сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

Вход	Изход
200
3
5.7	 202.85

Вход	Изход
2350
6
7
	2432.25

"""


def deposits(deposit, period, annual_rate):
    annual_rate = annual_rate/100
    total = deposit + period * ((deposit*annual_rate)/12)
    print(total)


d = float(input())
p = int(input())
a_r = float(input()) # %

deposits(d,p,a_r)
