from helper_methods.id_generator import IDGenerator
from ledger.side_enum import Side
from ledger.order_status_enum import order_status
import datetime
#Container structure for orders
class Order:

    # Method to enable Order to be used in heapq 
    # return True if self is less than other, False otherwise
    def __lt__(self, other) -> bool:
        return self.price < other.price

    def __init__(self, ticker : str, volume : int, price : float, side: Side, dateIn : datetime, senderID : str) -> None:
        self.id = IDGenerator.GetNewOrderId()
        self.ticker = ticker
        self.volume = volume
        self.filled_volume = 0
        self.price = price
        self.side = side
        self.dateIn = dateIn
        self.senderID = senderID
        self.__status = order_status.new
        self.__associated_orders = []

    def RemainingVolume(self) -> int:
        return self.volume - self.filled_volume

    def GetStatus(self) -> order_status:
        return self.__status
    
    def Fill(self, volume: int, price: float, otherOID):
        #TODO: finish and correct
        self.filled_volume += volume
        if self.filled_volume == volume:
            self.__status = order_status.filled
        else:
            self.__status = order_status.partial_fill
        #Notify watchers
        

