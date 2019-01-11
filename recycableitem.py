class RecycableItem():

    def __init__(self, name, price, quantity, weight):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.weight = weight

    def __str__(self):
        return self.name
