import csv
import time
from getpass import getpass
from cart import Cart
from inventory_system import InventorySystem
from utils import USER_CSV

class User:
    def __init__(self):
        self.current_user = None
        self.cart = Cart()
        self.inventory = InventorySystem()

    def register(self):
        print("\n--- Registration ---")
        name = input("Name: ")
        email = input("Email: ")
        password = getpass("Password: ")

        with open(USER_CSV, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, password])
        print("Registration successful!")

    def login(self):
        print("\n--- Login ---")
        email = input("Email: ")
        password = getpass("Password: ")

        with open(USER_CSV, 'r') as f:
            for row in csv.reader(f):
                if row[1] == email and row[2] == password:
                    self.current_user = row[0]
                    print("\nLogin successful!\n")
                    time.sleep(2)
                    return True
        print("Invalid credentials!")
        return False

    def logout(self):
        self.current_user = None
        self.cart.clear_cart()
        print("Logged out successfully!")
