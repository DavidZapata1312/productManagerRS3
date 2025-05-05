import json
import os

json_file = 'inventory.json'

def initialize_file():
    if not os.path.exists(json_file):
        with open(json_file, 'w') as f:
            json.dump([], f, indent=4)

def load_data():
    with open(json_file, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def name_exists(name, data):
    for product in data:
        if product["name"].lower() == name.lower():
            return True
    return False

def add_product(name, price, quantity):
    data = load_data()

    if name_exists(name, data):
        print(f"A product with the name '{name}' already exists.")
        return

    new_product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    data.append(new_product)
    save_data(data)
    print(f"Product '{name}' added successfully.")

def change_price(name, new_price):
    data = load_data()

    for product in data:
        if product["name"].lower() == name.lower():
            product["price"] = new_price
            save_data(data)
            print(f"Price of product '{name}' updated to {new_price}.")
            return

    print(f"No product found with the name '{name}'.")

def change_quantity(name, new_quantity):
    data = load_data()

    for product in data:
        if product["name"].lower() == name.lower():
            product["quantity"] = new_quantity
            save_data(data)
            print(f"Quantity of product '{name}' updated to {new_quantity}.")
            return

    print(f"No product found with the name '{name}'.")

if __name__ == "__main__":
    initialize_file()

    while True:
        print("\n--- Options Menu ---")
        print("1. Add new product")
        print("2. Change product price")
        print("3. Change product quantity")
        print("4. Exit")
        option = input("Select an option (1/2/3/4): ").strip()

        if option == "1":
            print("\n--- Add new product ---")
            name = input("Product name: ").strip()
            try:
                price = float(input("Product price: "))
                quantity = int(input("Product quantity: "))
            except ValueError:
                print("Invalid price or quantity. Try again.")
                continue

            if not name:
                print("The name cannot be empty.")
                continue

            if price < 0:
                print("The price cannot be negative.")
                continue

            if quantity < 0:
                print("The quantity cannot be negative.")
                continue

            add_product(name, price, quantity)

        elif option == "2":
            print("\n--- Change product price ---")
            name = input("Product name: ").strip()
            try:
                new_price = float(input("New product price: "))
            except ValueError:
                print("Invalid price. Try again.")
                continue

            if new_price < 0:
                print("The price cannot be negative.")
                continue

            change_price(name, new_price)

        elif option == "3":
            print("\n--- Change product quantity ---")
            name = input("Product name: ").strip()
            try:
                new_quantity = int(input("New product quantity: "))
            except ValueError:
                print("Invalid quantity. Try again.")
                continue

            if new_quantity < 0:
                print("The quantity cannot be negative.")
                continue

            change_quantity(name, new_quantity)

        elif option == "4":
            print("Goodbye! Inventory updated.")
            break

        else:
            print("Invalid option. Try again.")
