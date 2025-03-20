import csv
from item import Item
from utils import INVENTORY_CSV

class InventorySystem:
    def __init__(self):
        self.items = {}
        self.load_inventory()

    def load_inventory(self):
        with open(INVENTORY_CSV, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    self.items[row[0]] = Item(*row)

    def save_inventory(self):
        with open(INVENTORY_CSV, 'w', newline='') as f:
            writer = csv.writer(f)
            for item in self.items.values():
                writer.writerow([item.SKU, item.name, item.quantity, item.price])

    def check_availability(self, SKU, quantity=1):
        item = self.items.get(SKU)
        return item and item.quantity >= quantity

    def add_item(self, SKU, name, quantity, price):
        self.items[SKU] = Item(SKU, name, quantity, price)
        self.save_inventory()

    def update_item(self, SKU, quantity=None, price=None):
        item = self.items.get(SKU)
        if item:
            if quantity is not None:
                item.quantity = int(quantity)
            if price is not None:
                item.price = float(price)
            self.save_inventory()
    
    def delete_item(self, SKU):
        if SKU in self.items:
            del self.items[SKU]
            self.save_inventory()
        else:
            print("Item not found.")

