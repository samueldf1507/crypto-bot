class Crypto():

    def __init__(self, symbol):
        self.symbol = symbol
        self.previous_price =  None
        self.previous_volume = None
        