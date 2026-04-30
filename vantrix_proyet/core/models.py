class Product:
    def __init__(self, title, selling_price, cost):
        self.title = title
        self.selling_price = selling_price
        self.cost = cost

        self.profit = 0
        self.margin = 0
        self.score = 0
        self.decision = None

    def to_dict(self):
        return self.__dict__