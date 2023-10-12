import IDGenerator
import MonetaTerminal.sample.side_enum as side_enum
import MonetaTerminal.sample.order_status_enum as order_enum
import datetime
#Container structure for orders
class Order:

    # Method to enable Order to be used in heapq 
    # return True if self is less than other, False otherwise
    def __lt__(self, other) -> bool:
        return self.price < other.price

    def __init__(self, ticker : str, volume : int, price : float, side: side_enum.Side, dateIn : datetime, senderID : str) -> None:
        self.id = IDGenerator.IDGenerator.GetNewOrderId()
        self.ticker = ticker
        self.volume = volume
        self.filled_volume = 0

        self.price = price
        self.side = side
        self.dateIn = dateIn
        self.senderID = senderID
        self.__status = order_enum.order_status.new
        #self.__associated_orders = []
        

    def RemainingVolume(self) -> int:
        return self.volume - self.filled_volume

    def GetStatus(self) -> order_enum.order_status:
        return self.__status
    
    def Fill(self, volume: int, price: float, otherOID):
        
        self.filled_volume += volume
        if self.filled_volume == volume:
            self.__status = order_enum.order_status.filled
        else:
            self.__status = order_enum.order_status.partial_fill
        #Notify watchers
        

