import json 

def save_files():
        file_path = "C:/Users/victus/OneDrive/Desktop/product.json"

        data = []
        for product in content:
            data.append({
                "name": product.name,
                "price": product.price,
                "catagory": product.catagory,
                "quantity": product.quantity,
            })


        with open(file_path, 'w') as file:
                content = json.dump(data, file, indent=4)

def load_files():
    pass