import csv

# Function to save the inventory into a CSV file
def save_csv(inventory, path):
    # Check if the inventory is empty
    if len(inventory) == 0:
        print("No data to save")
        return

    try:
        # Open the file in write mode
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)

            # Write the header row into the CSV file
            writer.writerow(["product name", "unit price", "quantity"])

            # Loop through each product in the inventory
            for product in inventory:
                # Check if the product has the required fields
                if "name" in product and "price" in product and "quantity" in product:
                    # Write product data into the CSV file
                    writer.writerow([product["name"], product["price"], product["quantity"]])
                else:
                    # If the product is missing fields, skip it
                    print("Invalid product skipped")

        # Confirmation message for the user
        print("Inventory saved in:", path)

    # Catch any error that occurs during the process
    except Exception as e:
        print("Error while saving:", e)


