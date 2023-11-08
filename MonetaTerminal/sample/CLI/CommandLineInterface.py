import readline
from OrderLogic.Order import Order

class CLI:
    def __init__(self) -> None:
        self.running = True # Controls the status of the CLI
        self.context = ("main","$")  # Used to inform the user of contextual information (ex: submenu)

    def __print_help(self) -> None:
        print("add \t Adds an order with the specified characteristics ")
        print("quit \t exists from the program")
        print("help \t prints this help page")

    def __parse_add_order(self):
        print("Additional info required: [ticker] [side] [qty] [price] -> OrderID")
        user_input = input("add_order$ ")
        tokens = user_input.split()
        try:
            ticker = tokens[0]
            side   = tokens[1]
            qty    = tokens[2]
            price  = tokens[3]
            #TODO
            #order = Order(ticker, qty, price)
        except:
            print("Failed to tokenize the input string")

    def __parse(self,user_input: str):
        if(user_input == "help"):
            self.__print_help()
        elif(user_input == "quit"):
            self.running = False
        elif(user_input == "add"):
            self.__parse_add_order()
        else:
            print(user_input + " is an unknown command")
            self.__print_help();
    
    def MainLoop(self) -> None:
        while(self.running):
            user_input = input("$ ")
            self.__parse(user_input)

        print("Shutting down the CLI interpreter")