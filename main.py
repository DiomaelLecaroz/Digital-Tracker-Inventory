import os
from user import User
from utils import init_files()
from menus import main_menu

def main():
    init_files()
    user = User()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== Stockwise Inventory System ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("\nEnter your choice: ")

        if choice == '1':
            user.login()
            main_menu(user)
            user.logout()
        elif choice == '2':
            user.register()
        elif choice == '3':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
