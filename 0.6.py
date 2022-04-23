price = float(input("Введите стоимость еды"))
tax = price*0.20
tips = price*0.18
all_price = round(price+tax+tips,2)
print("all is ",all_price,"\n","tips is ",round(tips,2),"\n","tax is ",round(tax), sep="")