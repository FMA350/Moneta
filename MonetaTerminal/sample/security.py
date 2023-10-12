import random
import IDGenerator

#likely to remove
class Security:
    def __init__(self, name: str, ticker: str):
        self.id = IDGenerator.GetNewId()
        self.name = name
        self.ticker = ticker
        # add SEDOL and other identifiers

