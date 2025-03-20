import os

def display_inventory(inventory):
    print("\n=== Inventory ===")
    if not inventory.items:
        print("No items in inventory.")
    else:
        for item in inventory.items.values():
            print(item.getDetails())

def main_menu(user):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_inventory(user.inventory)
        print("\nMain Menu:")
        print("1. POS System (Cart)")
        print("2. Inventory Management")
        print("3. Analytics Dashboard")
        print("4. Logout")
        choice = input("\nEnter your choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            return
        else:
            print("Invalid choice!")

def cart_menu(user):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_inventory(user.inventory)
        print("\n=== POS System ===")
        print("1. Add Item to Cart")
        print("2. Remove Item from Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Back to Main Menu")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            pass

        elif choice == '2':
            pass

        elif choice == '3':
            pass

        elif choice == '4':
            pass

        elif choice == '5':
            return
        else:
            print("Invalid choice!")

def inventory_menu(user):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_inventory(user.inventory)
        print("\nInventory Management:")
        print("1. Add New Item")
        print("2. Update Existing Item")
        print("3. Delete Item")
        print("4. Return to Main Menu")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            sku = input("SKU: ")
            name = input("Product Name: ")
            qty = int(input("Initial Quantity: "))
            price = float(input("Price: $"))
            user.inventory.add_item(sku, name, qty, price)
            input("\nItem added! Press Enter to continue...")

        elif choice == '2':
            sku = input("Enter SKU to update: ")
            if sku in user.inventory.items:
                qty = input("New Quantity (leave blank to skip): ")
                price = input("New Price (leave blank to skip): $")
                user.inventory.update_item(sku,
                                          int(qty) if qty else None,
                                          float(price) if price else None)
                input("\nItem updated! Press Enter to continue...")
            else:
                print("Item not found!")
                input("\nPress Enter to continue...")
                
        elif choice == '3':
            sku = input("Enter SKU to delete: ")
            if sku in user.inventory.items:
                confirm = input(f"Are you sure you want to delete item {sku}? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    user.inventory.delete_item(sku)
                    input("\nItem deleted! Press Enter to continue...")
                else:
                    input("\nDeletion canceled. Press Enter to continue...")
            else:
                print("Item not found!")
                input("\nPress Enter to continue...")
                
        elif choice == '4':
            return
        else:
            print("Invalid choice!")

def analytics_menu(user):
    pass
