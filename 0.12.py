import math
PI = math.pi
r = float(input("введите радиус круга "))
h = float(input("введите высоту "))
sqr_round = PI*(r**2)
v = round(sqr_round*h,1)
print(v)