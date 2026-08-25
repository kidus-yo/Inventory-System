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
        elif choice == 13:
          save_files() 
          print("data Saved Successfully!✅")
        elif choice == 14:
            running = False
            print("Good Luck!")

if __name__ == "__main__":
    database.products.extend(load_files())
    main()
