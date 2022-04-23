import math
dist = float(input("введите высоту в метрах "))
G =9.8
v = math.sqrt(2*G*dist)
print(round(v,2),"м/с")