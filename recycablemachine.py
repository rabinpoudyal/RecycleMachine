from recycableitem import RecycableItem

class RecycableMachine():
    
    def __init__(self):
        self.names = ["cans","paper","bottle","stop"]
        self.price = [0.2,0.1,0.3]
        self.item_list = []
        self.total_balance = 0
        self.max_items = 10
        self.total_items = 0
        
    def add_item(self, item):
        self.item_list.append(item)
        
    def order_the_cost(self):
        cost = 0
        for item in self.item_list:
            cost += item.price *item.quantity
        return cost
    
    def select_product(self):
        while True:
            name = input("balance:$[2].please select a product:(can,bottle,paper)")
            if name in self.names:
                return name
            else:
                print("product not exists,try again")
    
    def accept_product(self, product):
        price = 0
        for i, n in enumerate(self.names):
            if(product == n):
               price = self.prices[i]
               break
        quantity = int(input("how many {} do you have?".format(product)))
        print("please place {} {} into machine.".format(quantity, product))
        print("{} accepted\n".format(product)*quantity)
         
        self.add_item(RecycableItem(product, price, quantity, 0))
        print("you added {} {} (3) for $1 : {:.2f} each. you have ${:.2f}".format(quantity,product,price,self.order_the_cost()))
               
               
    def print_receipt(self):
        print('\n------final receipt-------\is')
        total_quantity = 0
        total_cost = 0
        for item in self.item_list:
            print('{} {:<2$} $(:>2f)'.format(item.quantity,item.name+"(s)", item.price*item.quantity))
            total_quantity += item.quantity
            total_cost +=item.price*item.quantity
            print("\n number of item:  {}\namount paid:  $[1.2f]\n".format(total_quantity, total_cost))
            print("thank you for using recycling machine at feduni\n")

