class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []



    def sell_drink(self, drink):
        self.till += drink.price


    def add_drinks(self, drink):
        self.drinks.append(drink)   


    def check_drunkenness(self, customer):
        check = False
        if customer.drunkenness >= 2:
            check = True 
        return check
            


