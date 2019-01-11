class RecycableItem():
    
    def __init__(self,name,price,quantity, extraparam):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.extraparam = extraparam

    def __str__(self):
        return self.name
 
