import os

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Stockwise Inventory System ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
