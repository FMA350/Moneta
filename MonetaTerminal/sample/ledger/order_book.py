from threading import Lock, Thread

from helper_methods.singleton_meta import SingletonMeta
from ledger.order import Order


# The OrderBook is the single holder of the state of this trading venue.
class OrderBook (metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.pages = {} # list of securities tracked by the book
                        # with relative buy and sell heaps

    
    def add_order(self, new_order: Order) -> bool:
        # Check if an order page already exists in the book

        if new_order.ticker in self.pages:
            print("Page is present for " + new_order.ticker)
        else:
            print("Page not present for " + new_order.ticker)
            print("Add page: TODO")

        print("Adding order")
