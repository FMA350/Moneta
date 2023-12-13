import heapq
import threading
from side_enum import Side
from order import Order, order_status_enum

class OrderBookPage:
    def __init__(self, security) -> None:

        self.page_lock = threading.Lock()

        self.security = security
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
    
    def __Match(self, order_buy : Order.Order, order_sell : Order.Order):
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
        if(order_buy.GetStatus() == order_status_enum.order_status.filled):
            heapq.heappop(self.buy_book)
        if(order_sell.GetStatus() == order_status_enum.order_status.filled):
            heapq.heappop(self.sell_book)

        self.page_lock.release()
    
    def __Balance(self) -> None:
        self.page_lock.acquire()
        while True:
            best_buy = heapq.heappeek(self.buy_book)
            best_sell = heapq.heappeek(self.sell_book)
            if(best_buy.price >= best_sell.price):
                self.__Match(best_buy, best_sell)
            else:
                break
        self.page_lock.release()

    def RemoveOrder(self, order: Order.Order) -> bool:
        #TODO
        pass

    def ModifyOrder(self, order: Order.Order) -> bool:

        #TODO
        pass

    def AppendOrder(self, order: Order.Order) -> None:
        self.__AddOrder(order)
        self.__Balance()    

    # Returns best buy (low), sell (high) prices and mid
    # Aux method
    def GetPrices(self) -> []:
        best_buy = heapq.heappeek(self.buy_book)
        best_sell = heapq.heappeek(self.sell_book)
        average = (best_buy.price + best_sell.price ) / 2
        return tuple(best_buy.price, best_sell.price, average)


        
