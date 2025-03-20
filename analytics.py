class Analytics:
    @staticmethod
    def get_highest_product_count(inventory):
        return max(inventory.items.values(), key=lambda x: x.quantity, default=None)

    @staticmethod
    def get_total_product_count(inventory):
        return sum(item.quantity for item in inventory.items.values())

    @staticmethod
    def get_total_inventory_value(inventory):
        return sum(item.quantity * item.price for item in inventory.items.values())
