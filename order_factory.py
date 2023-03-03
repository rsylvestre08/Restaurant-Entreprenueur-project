from chicken import Chicken
from rice import Rice
from steak import Steak


class OrderFactory:
    def create_order(self,type):
        if type == 'chicken':
            return Chicken()
        elif type == 'rice':
            return Rice()
        elif type == 'steak':
            return Steak()
        
        