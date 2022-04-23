souv_count = int(input("введите количество сувениров "))
trinkets_count = int(input("введите количество безделушек "))
SOUV_WEIGHT = 75
TRINKETS_WEIGHT = 112
all_weight = SOUV_WEIGHT*souv_count+trinkets_count*TRINKETS_WEIGHT
print("общий вес=",all_weight,"g", sep = "")