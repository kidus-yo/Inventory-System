from models.sales import *

class Product:

    product_id = 1100
    def __init__(self, name, price, product_quantity, catagory):
        self.name = name
        self.price = price
        self.product_quantity = product_quantity
        self.catagory = catagory