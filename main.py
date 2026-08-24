from menu import *
from file_handling import *

def main():
    running = True

    while running:
        choice = main_menu()

        if choice == 1:
            print("Welcome to Add Product")
            print()
            add_product()

        elif choice == 13:
          save_files() 
          print("data Saved Successfully!✅")
        elif choice == 14:
            running = False
            print("Good Luck!")

if __name__ == "__main__":
    main()
