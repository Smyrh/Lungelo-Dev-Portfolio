# Shopping Cart Program
from inventory import inventory

total = 0
foods = []
prices = []

while True:
    food = input("Enter a food to buy, press T for total, or q to quit: ")
    if food.lower() == 'q':
        break
    elif food.lower() == 't':
        total = 0  # Reset total for current calculation
        for price in prices:
            total += price
        print(f"\nYour total is: R{total}")
    else:
        if food.lower() in inventory:
            price = inventory[food.lower()]
        else:
            price = float(input(f"{food} not in inventory. Enter the price in R: "))
        foods.append(food)
        prices.append(price)
        
    print("--- YOUR CART ---")
    for food in foods:
        print(food, end=" ")
    print() 