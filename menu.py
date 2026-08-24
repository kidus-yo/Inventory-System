from models.product import * 
from database import *


def main_menu():
    print("Welcome to Invenstory Managment System💭")
    print("1. Add Product")
    print("2. View Product")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Sale Product")
    print("7. View Sales")
    print("8. Sales Report")
    print("9. Restock Product")
    print("10. Adjust Stock")
    print("11. Low Stock Report")
    print("12. Inventory Statstics")
    print("13. Save")
    print("14. Exit")

    try:
        choice = int(input("Please Enter your choice: "))
        return choice

    except ValueError:
        print("Please make your choice using numbers only")

    except Exception:
        print("Soemthing Went Wrong")

def add_product():
     name = input("Enter name of the Product: ")
     price = int(input("Enter the price of the product: "))
     quantity =  int(input("Enter quantity: "))
     catagory = input("Enter Cantagory: ")

     product = Product(name, price, quantity, catagory)
     products.append(product)
     print("Product Added Successully✅")
     print("-" * 30)
     print(f"The product id is:{Product.product_id}")
     print("-" * 30)

def view_products():

    for product in products:
     print("-" * 30)
     print(f"Name: {product.name}")
     print(f"Price: {product.price}")
     print(f"quantity: {product.product_quantity}")
     print(f"Catagory: {product.catagory}")
     print(f"The product Id is: {product.product_id}")
     print("-" * 30)

def search_products():
    enter_ID = int(input("Please Enter the product_ID: "))
    for product in products:
        if enter_ID == product.product_id:
                 print("-" * 30)
                 print(f"Name: {product.name}")
                 print(f"Price: {product.price}")
                 print(f"quantity: {product.quantity}")
                 print(f"Catagory: {product.catagory}")
                 print(f"The product Id is: {product.product_id}")