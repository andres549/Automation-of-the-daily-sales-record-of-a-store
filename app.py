from servicios import *
from archivos import save_csv

# Main program variables
# The list "inventory" will store all products during program execution.
# The variable "continue_program" controls the main loop, allowing the menu
# to repeat until the user chooses to exit.
inventory = []
continue_program = "yes"


# Input validations
def input_int(message):
    """
    This function asks the user for an integer and validates the input.
    """
    valid = False

    while not valid:
        try:
            number = int(input(message))
            valid = True
        except ValueError:
            print("Please enter a valid integer.")

    return number


def input_float(message):
    """
    This function asks the user for a decimal number (float) and validates the input.
    """
    valid = False

    while not valid:
        try:
            number = float(input(message))
            valid = True
        except ValueError:
            print("Please enter a valid number.")

    return number

# Main menu loop
while continue_program == "yes":

    # Display menu
    # This block prints the main menu with all available options.
    # Each number corresponds to a specific action such as adding, showing,
    # searching, updating, or deleting products, as well as generating statistics
    # and exporting data to CSV.
    print("\n=== MENU ===")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Search product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Statistics")
    print("7. Save CSV")
    print("8. Export CSV")
    print("9. Exit")

    option = input("Choose an option: ")

    # Validate option
    # This loop ensures that the user can only choose valid options between 1 and 9.
    # If an incorrect value is entered, the program shows an error message and
    # asks again until a valid option is provided.
    while option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid option")
        option = input("Choose an option: ")

    # Option 1: Add product
    # Allows the user to register a new product in the inventory by asking for
    # name, price, and quantity. Then calls "add_product" to insert it into the list.
    if option == "1":
        name = input("Product name: ")
        price = input_float("Price: ")
        quantity = input_int("Quantity: ")
        add_product(inventory, name, price, quantity)

    # Option 2: Show inventory
    # Displays all products currently stored in the inventory.
    elif option == "2":
        show_inventory(inventory)

    # Option 3: Search product
    # Lets the user search for a specific product in the inventory.
    # If found, shows its details; otherwise informs the user it was not found.
    elif option == "3":
        show_inventory(inventory)
        name = input("Search product: ")
        product = search_product(inventory, name)

        if product is not None:
            print("\n=== PRODUCT FOUND ===")
            print("Name:", product["name"])
            print("Price:", product["price"])
            print("Quantity:", product["quantity"])
        else:
            print("Product not found")

    # Option 4: Update product
    # Allows the user to modify an existing product’s details.
    # If the user types "0", that field will not be changed.
    elif option == "4":
        show_inventory(inventory)
        name = input("Product to update: ")
        print("Write 0 if you don't want to change something")

        price = input_float("New price: ")
        quantity = input_int("New quantity: ")

        if price == 0:
            price = None
        if quantity == 0:
            quantity = None

        update_product(inventory, name, price, quantity)

    # Option 5: Delete product
    # Removes a product from the inventory after asking for its name.
    elif option == "5":
        show_inventory(inventory)
        name = input("Product to delete: ")
        delete_product(inventory, name)

    # Option 6: Statistics
    # Generates basic statistics: total units, total value,
    # most expensive product, and product with highest stock.
    elif option == "6":
        data = calculate_statistics(inventory)
        if data is not None:
            print("\n=== STATISTICS ===")
            print("Total units:", data[0])
            print("Total value:", data[1])
            print("Most expensive product:", data[2]["name"], "- $", data[2]["price"])
            print("Highest stock product:", data[3]["name"], "- Units:", data[3]["quantity"])

    # Option 7: Save CSV
    # Saves the inventory into a file named "inventory.csv".
    elif option == "7":
        save_csv(inventory, "inventory.csv")
        print("Inventory saved to inventory.csv")

    # Option 8: Export CSV
    # Exports the inventory into a CSV file with a custom name chosen by the user.
    elif option == "8":
        file_name = input("File name: ")
        save_csv(inventory, file_name + ".csv")
        print(f"Inventory exported to {file_name}.csv")

    # Option 9: Exit
    # Ends the program by setting "continue_program" to "no"
    # and shows a farewell message.
    elif option == "9":
        continue_program = "no"
        print("Thank you for using our program")
