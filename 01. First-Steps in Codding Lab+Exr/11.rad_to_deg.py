from math import pi
from math import floor

"""
Напишете програма, която чете ъгъл в радиани (rad) и го преобразува в градуси (deg).  Принтирайте получените градуси като цяло число използвайки math.floor.
Използвайте формулата: градуси = радиани * 180 / π. 

Примерен вход и изход
вход	изход		вход	изход		вход	изход		вход	Изход
3.1416	 180		 6.2832	360		   0.7854	45		      0.5236	30


"""

def rad_to_deg(rad):
    deg = rad * 180/pi
    print(floor(deg))


radians = float(input())

rad_to_deg(radians)