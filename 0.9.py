begin_depo = float(input("введите начальный депозит "))
INTEREST_RATE = 0.04
cure_depo = begin_depo
for i in range(3):
  cure_depo*=(1+INTEREST_RATE)
  print(f"сумма на счете на конец {i+1} года = ",round(cure_depo,2))