
# ROLE 1: THE MENU BUILDER
# Stores all menu items in a LIST. Writes add/remove/display
# functions. Owns the daily specials list.
 
menu = ["Latte", "Cold Brew", "Espresso", "Mocha"]
daily_specials = ["Pumpkin Spice Latte"]
 
 
def add_item(item):
    """Add a new item to the menu list."""
    menu.append(item)
    print(f"Added '{item}' to the menu.")
 
 
def remove_item(item):
    """Remove an item from the menu list."""
    if item in menu:
        menu.remove(item)
        print(f"Removed '{item}' from the menu.")
    else:
        print(f"'{item}' is not on the menu.")
 
 
def display_menu():
    """Print the full menu, including today's specials."""
    print("\n----- MENU -----")
    for item in menu:
        print(f"- {item}")
    if daily_specials:
        print("\nToday's Specials:")
        for special in daily_specials:
            print(f"* {special}")
    print("----------------")
 
 
# =========================================================
# ROLE 2: THE PRICE MANAGER
# Stores item names + prices in a DICT. Writes a lookup
# function so anyone can call get_price("Latte").
# =========================================================
 
prices = {
    "Latte": 4.50,
    "Cold Brew": 4.00,
    "Espresso": 3.00,
    "Mocha": 5.00,
    "Pumpkin Spice Latte": 5.50,
}
 
 
def get_price(item):
    """Look up the price of a menu item. Returns None if not found."""
    return prices.get(item)
 
 
def set_price(item, new_price):
    """Update or add a price for an item."""
    prices[item] = new_price
    print(f"Price for '{item}' set to ${new_price:.2f}")
 
 
# =========================================================
# ROLE 3: THE INFO KEEPER
# Stores fixed item details (name, category, calories) as
# TUPLES, since these details shouldn't change once set.
# Why tuples? Once a drink's category/calorie count is
# recorded, it should stay locked in -- tuples protect that.
# =========================================================
 
item_info = [
    ("Latte", "Espresso Drink", 190),
    ("Cold Brew", "Cold Coffee", 5),
    ("Espresso", "Espresso Drink", 5),
    ("Mocha", "Espresso Drink", 290),
    ("Pumpkin Spice Latte", "Seasonal Espresso Drink", 380),
]
 
 
def get_info(item):
    """Return the (name, category, calories) tuple for an item, or None."""
    for info in item_info:
        if info[0] == item:
            return info
    return None
 
 
def display_info(item):
    """Print an item's category and calories in a readable way."""
    info = get_info(item)
    if info:
        name, category, calories = info
        print(f"{name}: {category}, {calories} calories")
    else:
        print(f"No info found for '{item}'.")
 
 
# =========================================================
# ROLE 4: THE ORDER TAKER
# Writes take_order(), calculate_total(), and print_receipt().
# Calls the other teammates' functions/data to tie it together.
# =========================================================
 
def take_order():
    """
    Build an order by asking the customer for items.
    Uses the Menu Builder's `menu` list to validate choices
    and the Price Manager's get_price() to confirm each item
    is priced.
    """
    order = []
    print("\nType 'done' when you're finished ordering.")
    while True:
        item = input("What would you like to order? ")
        if item.lower() == "done":
            break
        if item in menu and get_price(item) is not None:
            order.append(item)
            print(f"Added '{item}' to your order.")
        else:
            print(f"Sorry, '{item}' isn't available. Try again.")
    return order
 
 
def calculate_total(order):
    """
    Add up the price of every item in the order using the
    Price Manager's get_price() function.
    """
    total = 0
    for item in order:
        price = get_price(item)
        if price is not None:
            total += price
    return total
 
 
def print_receipt(order):
    """
    Print a full receipt: each item's price (Price Manager)
    and category/calories (Info Keeper), then the total.
    """
    print("\n========= RECEIPT =========")
    for item in order:
        price = get_price(item)
        info = get_info(item)
        category = info[1] if info else "Unknown"
        print(f"{item:<20} ${price:>5.2f}   ({category})")
    total = calculate_total(order)
    print("----------------------------")
    print(f"{'TOTAL':<20} ${total:>5.2f}")
    print("============================")
 
 
# =========================================================
# DEMO: everything working together
# (Replace this with take_order() for a real interactive run)
# =========================================================
 
if __name__ == "__main__":
    display_menu()
 
    # Simulated order instead of live input(), so this demo runs on its own
    demo_order = ["Latte", "Mocha", "Pumpkin Spice Latte"]
    print(f"\nDemo order: {demo_order}")
 
    print_receipt(demo_order)
 
    print("\nItem details lookup:")
    for item in demo_order:
        display_info(item)
 
    # Uncomment this line to place a real order via the keyboard:
    # my_order = take_order()
    # print_receipt(my_order)
 