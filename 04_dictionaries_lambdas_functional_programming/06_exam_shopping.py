products_in_stock = {}
line = input()
while line != "shopping time":
    splited_line = line.split()
    product = splited_line[1]
    quantity = int(splited_line[2])
    if product in products_in_stock:
        products_in_stock[product] = products_in_stock[product] + quantity
    else:
        products_in_stock[product] = quantity
    line = input()
line = input()
while line != "exam time":
    splited_line = line.split()
    product = splited_line[1]
    quantity = int(splited_line[2])
    if product not in products_in_stock:
        print(f"{product} doesn't exist")
    elif products_in_stock[product] == 0:
        print(f"{product} out of stock")
    elif products_in_stock[product] < quantity:
        products_in_stock[product] = 0
    else:
        products_in_stock[product] = products_in_stock[product] - quantity
    line = input()
[print(f"{key} -> {value}") for key, value in products_in_stock.items() if value > 0]
