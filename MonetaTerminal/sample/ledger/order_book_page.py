import heapq
import threading

from ledger.side_enum import Side
from ledger.order import Order
from ledger.order_status_enum import order_status


class OrderBookPage:
    def __init__(self, ticker: str) -> None:

        self.page_lock = threading.Lock()

        self.ticker = ticker
        self.buy_book = []  #heap  
        heapq._heapify_max(self.buy_book)
        self.sell_book = [] #heap
        heapq.heapify(self.sell_book)

    def __AddOrder(self, order: Order) -> bool:
        self.page_lock.acquire()
        #blindly add the order
        if order.side == Side.Buy:
            heapq.heappush(self.buy_book, order)
        else:
            heapq.heappush(self.sell_book, order)
        self.page_lock.release()
        return True
    
    def __Match(self, order_buy : Order, order_sell : Order):
        print("Matching " + str(order_buy.id) + " with " + str(order_sell.id))
        self.page_lock.acquire()
        # How many shares are we transacting?
        minVolume = min(order_buy.RemainingVolume(), order_sell.RemainingVolume())
        # Check which order was first and use that price
        price = order_buy.price
        if order_sell.dateIn < order_buy.dateIn:
            price = order_sell.price

        # Fill
        order_buy.Fill(minVolume, price, order_sell.id)
        order_sell.Fill(minVolume, price, order_buy.id)

        # Remove filled orders
        if(order_buy.GetStatus() == order_status.filled):
            heapq.heappop(self.buy_book)
        if(order_sell.GetStatus() == order_status.filled):
            heapq.heappop(self.sell_book)

        self.page_lock.release()
    
    def __Balance(self) -> None:
        self.page_lock.acquire()
        while True:

            if len(self.buy_book) == 0 or len(self.sell_book) == 0:
                break

            best_buy = self.buy_book[0]
            best_sell = self.sell_book[0]

            if(best_buy.price >= best_sell.price):
                self.__Match(best_buy, best_sell)
            else:
                break
        self.page_lock.release()

    def RemoveOrder(self, order: Order) -> bool:
        #TODO
        pass

    def ModifyOrder(self, order: Order) -> bool:
        #TODO
        pass

    def AppendOrder(self, order: Order) -> None:
        self.__AddOrder(order)
        self.__Balance()    
        self.PrintAll()


    # Aux methods 


    # Returns best buy (low), sell (high) prices and mid
    def GetPrices(self) -> []:
        best_buy = self.buy_book[0]
        best_sell = self.sell_book[0]
        average = (best_buy.price + best_sell.price ) / 2
        return tuple(best_buy.price, best_sell.price, average)
    

    def __print_list(self, orders: []) -> None:
        for order in orders:
            print("### ID: "+ str(order.id))
            print("### Price: "+ str(order.price))
            print("### Size: "+ str(order.size))
            print ("")

    def PrintAll(self) -> None:
        print("# Product ticker: " + self.ticker)
        print("## Current sell orders:" )
        self.__print_list(self.sell_book)
        print("## Current buy orders:" )
        self.__print_list(self.buy_book)
        
        
