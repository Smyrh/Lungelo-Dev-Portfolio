"""
LIST IMPLEMENTATION (Enhanced)
- Asks for price when item not found
- Fixed all syntax errors from screenshot
- Maintains parallel lists
"""
from shopping_cart import inventory  # Shared inventory

def run():
    items = []
    prices = []
    print("LIST-BASED CART (Add New Items)")
    
    while True:
        print("\nAvailable Items:")
        for i, (item, price) in enumerate(inventory.items(), 1):
            print(f"{i}. {item.title():<15} R{price:.2f}")
        
        choice = input("\nEnter item name/number or 'done': ").strip().lower()
        
        if choice == 'done':
            break
        
        # Handle numeric selection
        if choice.isdigit():
            try:
                idx = int(choice) - 1
                item = list(inventory.keys())[idx]
                price = inventory[item]
            except (ValueError, IndexError):
                print("Invalid item number!")
                continue
        # Handle new items
        elif choice not in inventory:
            print(f"\n'{choice}' not in inventory. Please enter price.")
            while True:
                try:
                    price = float(input(f"Enter price for {choice}: R"))
                    inventory[choice] = price  # Add to inventory
                    item = choice
                    print(f"New item added: {item.title()} - R{price:.2f}")
                    break
                except ValueError:
                    print("Invalid price! Numbers only.")
            continue
        # Existing items
        else:
            item = choice
            price = inventory[item]
        
        # Add to cart
        items.append(item)
        prices.append(price)
        print(f"Added {item.title()} - R{price:.2f}")

    # Display cart
    print("\nYOUR CART:")
    for i, (item, price) in enumerate(zip(items, prices), 1):
        print(f"{i}. {item.title():<15} R{price:.2f}")
    print(f"TOTAL: R{sum(prices):.2f}")