from discontHandler import PercentageDiscountHandler, FixedDiscountHandler
from nieZaimplementowane.shoppingCart import ShoppingCart
from orderBuilder import OrderBuilder
from nieZaimplementowane.orderFrom import OrderForm
from orderMediator import OrderMediator
from nieZaimplementowane.paymentGateway import PaymentGateway


class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def apply_discount(self, discount):
        discount.apply_discount(self)

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


discount_handler_chain = PercentageDiscountHandler(FixedDiscountHandler())

cart = ShoppingCart()
payment_gateway = PaymentGateway()
order_form = OrderForm()

order_mediator = OrderMediator(cart, payment_gateway, order_form)

order_builder = OrderBuilder()

burger = Item("Burger", 10.0)
drink = Item("Drink", 5.0)

order_builder.add_item(burger)
order_builder.add_item(drink)

order_builder.apply_discount(discount_handler_chain)

order = order_builder.get_order()
order_mediator.process_order(order)