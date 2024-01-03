class OrderMediator:
    def __init__(self, cart, payment_gateway, order_form):
        self.cart = cart
        self.payment_gateway = payment_gateway
        self.order_form = order_form

    def process_order(self):
        if self.cart.is_valid() and self.order_form.is_complete():
            self.payment_gateway.process_payment()