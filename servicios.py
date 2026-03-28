# servicios.py


def add_product(inventory, name, price, quantity):
    """
    Adds a new product to the inventory list.
    Receives product data and stores it as a dictionary.
    """
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)
    print("Product added successfully")


def show_inventory(inventory):
    """
    Displays all products in the inventory.
    Shows name, price, and quantity in a list format.
    """
    if inventory == []:
        print("Inventory is empty")
    else:
        print("\n=== INVENTORY ===")
        counter = 1
        for product in inventory:
            print(str(counter) + ". Name: " + product["name"] +
                  " | Price: $" + str(product["price"]) +
                  " | Quantity: " + str(product["quantity"]))
            counter = counter + 1


def search_product(inventory, name):
    """
    Searches for a product by name.
    Returns the product if found, otherwise returns None.
    """
    for product in inventory:
        if product["name"] == name:
            return product
    return None


def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Updates the price and/or quantity of a product.
    Uses search_product to find the product first.
    """
    product = search_product(inventory, name)

    if product != None:
        if new_price != None:
            product["price"] = new_price

        if new_quantity != None:
            product["quantity"] = new_quantity

        print("Product updated")
    else:
        print("Product not found")


def delete_product(inventory, name):
    """
    Deletes a product from the inventory.
    Finds the product and removes it from the list.
    """
    product = search_product(inventory, name)

    if product != None:
        inventory.remove(product)
        print("Product deleted")
    else:
        print("Product not found")


def calculate_statistics(inventory):
    """
    Calculates inventory statistics:
    total units, total value,
    most expensive product, and highest stock product.
    Returns all values as a tuple.
    """
    if inventory == []:
        print("Inventory is empty")
        return None

    total_units = 0
    total_value = 0

    most_expensive = None
    highest_stock = None

    for product in inventory:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

        if most_expensive == None or product["price"] > most_expensive["price"]:
            most_expensive = product

        if highest_stock == None or product["quantity"] > highest_stock["quantity"]:
            highest_stock = product

    return total_units, total_value, most_expensive, highest_stock