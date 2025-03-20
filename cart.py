class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))
        print(f"Added {quantity} x {item.name} to cart")

    def remove_item(self, SKU):
        self.items = [i for i in self.items if i[0].SKU != SKU]

    def clear_cart(self):
        self.items = []

    def calculate_total(self):
        return sum(item.price * qty for item, qty in self.items)

    def generate_receipt(self):
        receipt = []
        total = 0
        for item, qty in self.items:
            subtotal = item.price * qty
            receipt.append(f"{item.name[:15]:<15} ({qty}x) \t${subtotal:.2f}")
            total += subtotal
        receipt.append(f"\n{'Total:':<20}\t${total:.2f}")
        return "\n".join(receipt)
