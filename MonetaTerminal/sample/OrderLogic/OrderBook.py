class OrderBook:
    def __init__(self) -> None:
        self.pages = [] # list of securities tracked by the book
                        # with relative buy and sell heaps

        