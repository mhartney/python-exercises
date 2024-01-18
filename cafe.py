"""This program calculates the total value of a Cafe's stock 
and prints it in a table. It demonstrates use of lists and dictionaries."""

def print_table(menu_list, price_dict, stock_dict, cost_dict, stock_sum):
    """Function formats and prints output information in a neat table.
       Table parameter options below."""
    # Print table header.
    print("\n" + ''.center(TABLE_WIDTH, '='))
    print(f" {ITALIC_START}RIVER GARDENS CAFE{ITALIC_END} ".center(60, '-'))
    print("ITEM ".ljust(COLUMN1, '=') + " PRICE ".ljust(COLUMN2, '='), end=" ")
    print("UNIT ".ljust(COLUMN3, '=') + " TOTAL".rjust(COLUMN4, '='))

    # Loop through list & dictionaries, then print table columns.
    for i in menu_list:
        item_price = f" £{price_dict[i]:.2f} "
        item_stock = f"{stock_dict[i]} "
        items_cost = f" £{cost_dict[i]:.2f}"
        i = f"{i.title()} "
        print(i.ljust(COLUMN1, '.') + item_price.ljust(COLUMN2, '.'), end=" ")
        print(item_stock.ljust(COLUMN3, '.') + items_cost.rjust(COLUMN4, '.'))
    
    # Print total stock calculation at table bottom.
    print(''.center(TABLE_WIDTH, '='))
    print(f"Total Stock: £{stock_sum:.2f}".center(TABLE_WIDTH, ' '))
    print(''.center(TABLE_WIDTH, '=') + "\n")

# Table parameter options; column width adjustments, italics.
COLUMN1 = 25
COLUMN2 = 12
COLUMN3 = 6
COLUMN4 = 8
TABLE_WIDTH = COLUMN1 + COLUMN2 + COLUMN3 + COLUMN4 + 1 # Number added at end to adjust width.
ITALIC_START = "\033[3m"
ITALIC_END = "\033[0m"

# Cafe menu, stock and price list.
menu = ["granola", "pancakes", "eggs benedict",
        "full english breakfast", "americano"]

price = {"granola": 6.45,
         "pancakes": 11.00,
         "eggs benedict": 12.90,
         "full english breakfast": 13.95,
         "americano": 3.30}

stock = {"granola": 10,
         "pancakes": 30,
         "eggs benedict": 23,
         "full english breakfast": 12,
         "americano": 30}

# Create dictionary, calculating and storing total cost of stock per item.
cost_per_stock = {}
TOTAL_STOCK_SUM = 0
for product in menu:
    cost_per_stock[product] = stock[product] * price[product]
    TOTAL_STOCK_SUM += stock[product] * price[product] # Calculate total sum of cafe stock.

# Print results.
print_table(menu, price, stock, cost_per_stock, TOTAL_STOCK_SUM)
