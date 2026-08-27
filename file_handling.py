import json
from database import *
from models.product import *
from models.sales import *
from datetime import datetime

def save_files():
        file_path = "C:/Users/victus/OneDrive/Desktop/product.json"

        data = {
              "products": [],
              "sales": [],
        }
        
        for product in products:
            data.append["products"]({
                "name": product.name,
                "price": product.price,
                "catagory": product.catagory,
                "quantity": product.product_quantity,
                "product_id": product.product_id
            })

            for sale in sales:
                 data.append["sales"]({
                  "name": sale.proaduct_name,
                   "quantity": sale.quantity,
                   "date": sale.date,
                   "sale_id": sale.sale_id,   
                 })


        with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)

def load_files():
    file_path = "C:/Users/victus/OneDrive/Desktop/product.json"

    loaded_files = []

    with open(file_path, 'r') as file:
          content = json.load(file)

          for data in content["products"]:
                product = Product(
                      data["name"],
                      data["price"],
                      data["quantity"],
                      data["catagory"],
                      
                )



                product.product_id = data["product_id"]
                loaded_files.append(product) 

          if content:
                highest_id = max( found["product_id"] for found in content["products"])
                Product.product_id = highest_id + 1

          return loaded_files

def load_sale():
      file_path = "C:/Users/victus/OneDrive/Desktop/product.json"

      loaded_sales = []
      with open(file_path, 'r') as file:
            content = json.load(file)

            for data in content["sales"]:
                  sales = Sale(

                   data["name"],
                   data["quantity"],
                   datetime.strptime(data["date"], "%Y-%m-%d")
                  )

                  sales.sale_id = data["sale_id"]
                  loaded_sales.append(sales)


            if content:
                  highest_id = max(number["sale_id"] for number in content["sales"])
                  Sale.sale_id = highest_id + 1

            return loaded_sales