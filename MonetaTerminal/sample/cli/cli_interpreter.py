import readline
from datetime import datetime

from ledger.order import Order
from ledger.order_book import OrderBook
from ledger.order_status_enum import order_status
from ledger.side_enum import Side, get_side_from_str

class CLI:
    def __init__(self) -> None:
        self.running = True # Controls the status of the CLI
        self.context = ("main","$")  # Used to inform the user of contextual information (ex: submenu)

    def __print_help(self) -> None:
        print("add \t Adds an order with the specified characteristics ")
        print("qadd \t Adds two orders for AAPL for quick testing")
        print("quit \t exists from the program")
        print("help \t prints this help page")

    def __parse_add_order(self) -> Order:
        print("Additional info required: [side] [ticker] [qty] [price] -> OrderID")
        user_input = input("add_order$ ")
        tokens = user_input.split()
        try:
            side = tokens[0]
            ticker   = tokens[1]
            qty    = tokens[2]
            price  = tokens[3] #Currently a float, eventually a class of its own for precision
            order = Order(ticker, qty, price, get_side_from_str(side), datetime.now(), "CLI")
            print(" new order created with ID: " + str(order.id))
            return order
        except Exception as e:
            print("Failed to tokenize the input string")
            print(e)
            
    # TODO: move to a map[string][function] and allow for extensions
    def __parse(self,user_input: str):
        if(user_input == "help"):
            self.__print_help()
        elif(user_input == "quit"):
            self.running = False
        elif(user_input == "add"):
            order = self.__parse_add_order()
            # Pass the order to the appropriate OrderBookPage
            orderBook = OrderBook()
            orderBook.add_order(order)
        elif(user_input == "qadd"):
            order_buy1 = Order("AAPL", 50, 126.25, Side.Buy, datetime.now(), "CLI_B")
            order_buy2 = Order("AAPL", 20, 126.50, Side.Buy, datetime.now(), "CLI_B")
            OrderBook().add_order(order_buy1)
            OrderBook().add_order(order_buy2)
            order_sell = Order("AAPL", 200, 125.75, Side.Sell, datetime.now(), "CLI_S")
            OrderBook().add_order(order_sell)
        else:
            print(user_input + " is an unknown command")
            self.__print_help();
    
    def MainLoop(self) -> None:
        while(self.running):
            user_input = input("$ ")
            self.__parse(user_input)

        print("Shutting down the CLI interpreter")