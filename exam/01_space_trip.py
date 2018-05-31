star = input()
distance = int(input())
budget = int(input())
fuel_consumption = float(input())
gas_price = float(input())

liters_per_Gm = fuel_consumption / 100
price_per_Gm = liters_per_Gm * gas_price
needed_money = price_per_Gm * distance
leftover = budget - needed_money
if leftover >= 0:
    print(f"Off to {star} with ${leftover:.2f} for snacks")
else:
    print(f"Maybe another time, need ${-leftover:.2f} more")
