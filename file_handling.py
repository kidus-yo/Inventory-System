import json
from database import *
from models.product import *

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
    file_path = "C:/Users/victus/OneDrive/Desktop/product.json"

    loaded_files = []

    with open(file_path, 'r') as file:
          content = json.load(file)

          for data in content:
                product = Product(
                      data["name"],
                      data["price"],
                      data["quantity"],
                      data["catagory"]
                )

                product.product_id = data["product_id"]
                loaded_files.append(product) 

          if content:
                highest_id = max( key["product_id"] for key in content)
                Product.product_id = highest_id + 1

          return loaded_files