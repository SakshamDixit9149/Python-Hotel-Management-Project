import os

logged_in_admin = None
current_customer = None
filepath = "Level2 - FileHandling"
admin_filename = os.path.join(filepath, "admins.txt")


def add_admin(username, password):
    with open(admin_filename, "a") as f:
        f.write(username + "," + password + "\n")
        print("Username and password are append successfully!")


def read_userpass(username, password):
    with open(admin_filename, "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split(",")
            if stored_username == username and stored_password == password:
                return True
    return False


def adding_prices(customer_name, items, prices):
    customer_file = os.path.join(filepath, customer_name, "Prices.txt")
    with open(customer_file, "a") as file:
        file.write(items + ":$" + str(prices) + "\n")
        print(f"Added {items} with price ${prices} to {customer_name}'s file.")


def append_cus_data(name, address, contact):
    global filepath
    while os.path.exists(os.path.join(filepath, name)):
        name = input(
            "The Name you Entered already exists. Enter a different Name: ")
    os.mkdir(os.path.join(filepath, name))
    with open(os.path.join(filepath, name, "customers.txt"), "w") as file:
        file.write(name + "," + address + "," + contact + "\n")
        print("Customer Details successfully entered in system")
        global current_customer
        current_customer = name


def clearConsole():
    return os.system('clear')


def print_formatted_history(customer):
    customer_file = os.path.join(filepath, customer, "customers.txt")
    price_file = os.path.join(filepath, customer, "Prices.txt")

    with open(customer_file) as file:
        line = file.readline()
        name, address, contact = line.strip().split(',')

    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone Number: {contact}")
    print("--------")
    print("INVOICE")
    print("--------")

    booking_items = ["Ultra Royal", "Royal", "Elite", "Common"]
    gaming_items = ["Carrom", "Chess", "Table Tennis"]
    restaurant_items = ["Pizza", "Burger", "Salad"]

    booking_bill = []
    gaming_bill = []
    restaurant_bill = []

    total_amount = 0

    with open(price_file) as file:
        for line in file:
            item, price = line.strip().split(":$")
            price = int(price)
            total_amount += price
            if item in booking_items:
                booking_bill.append(f"{item}: ${price}")
            elif item in gaming_items:
                gaming_bill.append(f"{item}: ${price}")
            elif item in restaurant_items:
                restaurant_bill.append(f"{item}: ${price}")

    if booking_bill:
        print("Booking Bill")
        for item in booking_bill:
            print(item)

    if gaming_bill:
        print("\nGaming Bill")
        for item in gaming_bill:
            print(item)

    if restaurant_bill:
        print("\nRestaurant Bill")
        for item in restaurant_bill:
            print(item)
    print("~~~~~~")
    print("Total")
    print("~~~~~~")
    print(f"Grand Bill\nTotal: ${total_amount}")


def admin_show_history(customer):
    print_formatted_history(customer)


def show_history(customer):
    print_formatted_history(customer)


def register_admin():
    print("\n--- Admin Registration ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    add_admin(username, password)


def login_admin():
    print("\n--- Admin Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if read_userpass(username, password):
        print("Login Successfully!")
        global logged_in_admin
        logged_in_admin = username
        return True
    print("Invalid credentials! Please try again.")
    return False


def logout_admin():
    global logged_in_admin
    print("Logged Out:", logged_in_admin)
    logged_in_admin = None


def collect_customer_details():
    print("\n--- Customer Details ---")
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    contact = input("Enter contact number: ")
    append_cus_data(name, address, contact)
    return name


def show_menu():
    clearConsole()
    print("Welcome,", logged_in_admin)
    print("\n--- Main Menu ---")
    print("1. Booking Record")
    print("2. Restaurant Area")
    print("3. Gaming Zone")
    print("4. Calculate Total Bill")
    print("5. Show Transaction History for current user")
    print("6. Exit")


def booking_record(customer):
    print("\n--- Booking Record ---")
    print("1. Ultra Royal - $5000")
    print("2. Royal - $3500")
    print("3. Elite - $2500")
    print("4. Common - $1500")
    print("5. Go to Main Menu")
    choice = int(input("Enter your choice: "))
    prices = [5000, 3500, 2500, 1500]
    items = ["Ultra Royal", "Royal", "Elite", "Common"]
    if 1 <= choice <= len(prices):
        adding_prices(customer, items[choice - 1], prices[choice - 1])
        print("Item added to your bill.")
    else:
        print("Invalid choice! Please try again.")


def restaurant_area(customer):
    print("\n--- Restaurant Area ---")
    print("1. Pizza - $10")
    print("2. Burger - $7")
    print("3. Salad - $5")
    print("4. Go to Main Menu")
    choice = int(input("Enter your choice: "))
    prices = [10, 7, 5]
    items = ["Pizza", "Burger", "Salad"]
    if 1 <= choice <= len(prices):
        adding_prices(customer, items[choice - 1], prices[choice - 1])
        print("Item added to your bill.")
    else:
        print("Invalid choice! Please try again.")


def gaming_zone(customer):
    print("\n--- Gaming Zone ---")
    print("1. Carrom - $5")
    print("2. Chess - $3")
    print("3. Table Tennis - $8")
    print("4. Go to Main Menu")
    choice = int(input("Enter your choice: "))
    prices = [5, 3, 8]
    items = ["Carrom", "Chess", "Table Tennis"]
    if 1 <= choice <= len(prices):
        adding_prices(customer, items[choice - 1], prices[choice - 1])
        print("Game added to your bill.")
    else:
        print("Invalid choice! Please try again.")


def calculate_total_bill(customer):
    print_formatted_history(customer)


def handle_customer(customer):
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        match choice:
            case '1':
                booking_record(customer)
            case '2':
                restaurant_area(customer)
            case '3':
                gaming_zone(customer)
            case '4':
                calculate_total_bill(customer)
                input("Press enter to go back!")
            case '5':
                show_history(customer)
                input("Press enter to go back!")
            case '6':
                print("Exiting customer area...")
                global current_customer
                current_customer = None
                break
            case _:
                print("Invalid choice! Please try again.")


while True:
    if not logged_in_admin:
        clearConsole()
        print("\n--- Welcome to Hotel Management System ---")
        print("1. Admin Login")
        print("2. Exit")

        option = input("Enter your choice: ")
        match option:
            case '1':
                login_admin()
            case '2':
                print("Exiting the system...")
                os._exit(1)
            case _:
                print("Invalid choice! Please try again.")
        clearConsole()
    else:
        if current_customer is None:
            print("Welcome,", logged_in_admin)
            print("1. Add a New Customer")
            print("2. Add an Admin")
            print("3. Show Transaction History for a Customer")
            print("4. Logout")
            print("5. Exit")
            option = input("Enter your choice: ")
            match option:
                case '1':
                    current_customer = collect_customer_details()
                case '2':
                    register_admin()
                case '3':
                    give_customer = input("Enter the name of the Customer: ")
                    admin_show_history(give_customer)
                    input("Press enter to Go back!")
                case '4':
                    logout_admin()
                case '5':
                    print("Exiting Program...")
                    os._exit(1)
                case _:
                    print("Invalid choice! Please try again.")
        else:
            handle_customer(current_customer)
