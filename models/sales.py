from models.product import *

class Sale:

    sale_id = 2200
    total = 0
    product_quantity = 0
    
    def __init__(self, product, quantity, date):
        self.product = product
        self.quantity = quantity
        self.date = date
        Sale.total += 1
        Sale.product_quantity += quantity
 