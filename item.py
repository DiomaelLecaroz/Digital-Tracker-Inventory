class Item:
    def __init__(self, SKU, name, quantity, price):
        self.SKU = SKU
        self.name = name
        self.quantity = int(quantity)
        self.price = float(price)

    def getDetails(self):
        return f"{self.SKU} | {self.name[:15]:<15} | Qty: {self.quantity:<3} | ${self.price:.2f}"
