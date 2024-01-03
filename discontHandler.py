class DiscountHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def apply_discount(self, order):
        if self.successor:
            self.successor.apply_discount(order)

class PercentageDiscountHandler(DiscountHandler):
    def apply_discount(self, order):
        super().apply_discount(order)

class FixedDiscountHandler(DiscountHandler):
    def apply_discount(self, order):
        super().apply_discount(order)