from menu import *
from file_handling import *
import database

def main():
    running = True

    while running:
        choice = main_menu()

        if choice == 1:
            print("Welcome to Add Product")
            print()
            add_product()

        elif choice == 2:
            print("welcome to View Products")
            print()
            view_products()

        elif choice == 3:
            print("Welcome to Search Product")
            print()
            search_products()

        elif choice == 4:
            print("welcome to Update Products")
            print()
            update_product()

        elif choice == 5:
            print("Welcome to Delete Products")
            print()
            delete_product()

        elif choice == 6:
            print("Welcome to Sale Products")
            print()
            sale_products()

        elif choice == 7:
            print("Welcome to View Sales")
            print()
            view_sales()

        elif choice == 8:
            print("Welcome to Sales Report📊")
            print()
            sales_report()

        elif choice == 9:
            print("Welcome to Restock Product")
            print()
            restock_product()

        elif choice == 10:
            print("Welcome to Adjust Stock🧑‍🔧")
            print()
            adjust_stock()

        elif choice == 11:
            print("Welcome to Low Stock Report🔈")
            print()
            low_stock()

        elif choice == 13:
          save_files() 
          print("data Saved Successfully!✅")
        elif choice == 14:
            running = False
            print("Good Luck!")

if __name__ == "__main__":
    database.products.extend(load_files())
    database.sales.extend(load_sale())
    main()
