small_count = int(input("сколько бутылок объемом меньше 1 литра?"))
big_count = int(input("сколько бутылок объемом больше 1 литра?"))
small_price = 0.1
big_price = 0.25
all_money = small_count*small_price+big_count*big_price
print("Вы заработаете $"+str(round(all_money,2)))