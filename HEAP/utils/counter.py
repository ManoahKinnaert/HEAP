class Counter:
    def __init__(self):
        self.compares = 0
        self.exchanges = 0
    
    def increment_compares(self):
        self.compares += 1
    
    def increment_exchanges(self):
        self.exchanges += 1

    def decrement_compares(self):
        assert self.compares > 0
        self.compares -= 1
    
    def decrement_exchanges(self):
        assert self.exchanges > 0
        self.exchanges -= 1
    
    def reset_compares(self):
        self.compares = 0
    
    def reset_exchanges(self):
        self.exchanges = 0

    def reset(self):
        self.reset_compares()
        self.reset_exchanges()