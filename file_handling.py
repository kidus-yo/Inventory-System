import json
from database import *

def save_files():
        file_path = "C:/Users/victus/OneDrive/Desktop/product.json"

        data = []
        for product in products:
            data.append({
                "name": product.name,
                "price": product.price,
                "catagory": product.catagory,
                "quantity": product.product_quantity,
            })


        with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

def load_files():
    pass