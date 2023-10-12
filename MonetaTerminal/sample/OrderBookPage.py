import heapq

import Order
import MonetaTerminal.sample.side_enum as side_enum
import MonetaTerminal.sample.order_status_enum as order_enum

class OrderBookPage:
    def __init__(self, security) -> None:

        self.security = security
        self.buy_book = []  #heap  
        heapq._heapify_max(self.buy_book)
        self.sell_book = [] #heap
        heapq.heapify(self.sell_book)

    def __AddOrder(self, order: Order.Order) -> bool:
        #blindly add the order
        if order.side == side_enum.Side.Buy:
            heapq.heappush(self.buy_book, order)
        else:
            heapq.heappush(self.sell_book, order)

        return True
    
    def __Match(self, order_buy : Order.Order, order_sell : Order.Order):
        # Get how many shares are we transacting
        minVolume = min(order_buy.RemainingVolume(), order_sell.RemainingVolume())
        # Check which order was first and use that price
        price = order_buy.price
        if order_sell.dateIn < order_buy.dateIn:
            price = order_sell.price

        # Fill
        order_buy.Fill(minVolume, price, order_sell.id)
        order_sell.Fill(minVolume, price, order_buy.id)

        # Remove filled orders
        if(order_buy.GetStatus() == order_enum.order_status.filled):
            heapq.heappop(self.buy_book)
        if(order_sell.GetStatus() == order_enum.order_status.filled):
            heapq.heappop(self.sell_book)
    
    def __Balance(self) -> None:
        while True:
            best_buy = heapq.heappeek(self.buy_book)
            best_sell = heapq.heappeek(self.sell_book)
            if(best_buy.price >= best_sell.price):
                self.__Match(best_buy, best_sell)
            else:
                break

    def AppendOrder(self, order: Order.Order) -> None:
        self.__AddOrder(order)
        #check for imbalances
        self.__Balance()    

    #returns best buy (low), sell (high) prices and mid
    def GetPrices(self) -> []:
        best_buy = heapq.heappeek(self.buy_book)
        best_sell = heapq.heappeek(self.sell_book)
        average = (best_buy.price + best_sell.price ) / 2
        return tuple(best_buy.price, best_sell.price, average)


        
