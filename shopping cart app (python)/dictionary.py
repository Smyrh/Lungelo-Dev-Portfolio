"""
DICTIONARY IMPLEMENTATION
- Uses dictionary comprehensions
- Shows item counts
"""
from shopping_cart import inventory  # Shared inventory

def run():
    cart = {}
    print("DICTIONARY CART (Items: Count)")
    while True:
        print("\nInventory:")
        for i, item in enumerate(inventory.items(), 1):
            print(f"{i}. {item[0].title():<15} R{item[1]:.2f}")
        
        choice = input("Enter item#/name or 'done': ").lower()
        if choice == 'done': break
        
        try:
            item = list(inventory.keys())[int(choice)-1] if choice.isdigit() else choice
            cart[item] = cart.get(item, 0) + 1
            print(f"Added {item} (Total: {cart[item]})")
        except (ValueError, IndexError):
            print("Invalid selection")

    print("\nRECEIPT:")
    total = sum(inventory[k]*v for k,v in cart.items())
    for item, qty in cart.items():
        print(f"{qty}x {item.title():<15} R{inventory[item]*qty:.2f}")
    print(f"TOTAL: R{total:.2f}")