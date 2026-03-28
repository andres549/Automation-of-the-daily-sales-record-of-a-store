# Automation of the Daily Sales Record of a Store

This project is a Python-based application designed to automate the daily sales record of a store.  
It provides a simple command-line interface (CLI) where users can manage inventory, track products, and export data for reporting.

## Features

- **Add Product**: Register new products with name, price, and quantity.
- **Show Inventory**: Display all products currently stored in the inventory.
- **Search Product**: Find a specific product by name and view its details.
- **Update Product**: Modify product details (price and quantity).
- **Delete Product**: Remove products from the inventory.
- **Statistics**: Generate basic statistics such as:
  - Total units
  - Total inventory value
  - Most expensive product
  - Product with highest stock
- **Save CSV**: Save the inventory into a default CSV file (`inventory.csv`).
- **Export CSV**: Export the inventory into a custom-named CSV file.
- **Exit**: End the program gracefully.

## Project Structure

 app.py              # Main program with the menu loop
 servicios.py        # Functions for inventory operations (add, update, delete, search, statistics)
 archivos.py         # Functions for saving/exporting inventory to CSV
 README.md           # Project documentation

 
## Requirements

- Python 3.8 or higher
- Git installed
- Visual Studio Code (recommended for editing and running the project)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Automation-of-the-daily-sales-record-of-a-store.git
   
2.Open the project in Visual Studio Code:
code Automation-of-the-daily-sales-record-of-a-store

3.Run the program:
python app.py

by:@andres549


