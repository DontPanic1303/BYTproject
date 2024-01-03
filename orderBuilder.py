from main import Order


class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def add_item(self, item):
        self.order.add_item(item)

    def apply_discount(self, discount):
        self.order.apply_discount(discount)

    def get_order(self):
        return self.order

