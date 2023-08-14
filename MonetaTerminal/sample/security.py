import random

class IDGenerator:
    id: int = 0
    def GetNewId() -> int:
        id += 1
        return id

class Security:
    def __init__(self, name: str, ticker: str, initialPrice: float):
        self.id = IDGenerator.GetNewId()
        
        self.name  = name
        self.ticker = ticker
        self.price = initialPrice

    # Simulates a market tick. New prices are generated
    def UpdatePrice(self):
        percent_change = random.uniform(0.0, 10.0) - 5.0
        price_change = percent_change * self.price
        price = price + price_change
