import os
admins = [["Saksham", "123"]]
customers = []
logged_in_admin = None
current_customer = None


def clearConsole():
    return os.system('clear')


def register_admin():
    print("\n--- Admin Registration ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    for admin in admins:
        if admin[0] == username:
            print("Username already exists! Try logging in.")
            return
    admins.append([username, password])
    print("Admin registered successfully!")


def login_admin():
    print("\n--- Admin Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    for admin in admins:
        if admin[0] == username and admin[1] == password:
            print("Login successful!")
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
    customer = [name, address, contact, 0]
    customers.append(customer)
    print("Customer details recorded successfully!")
    return customer


def show_menu():
    clearConsole()
    print("Welcome,", logged_in_admin)
    print("\n--- Main Menu ---")
    print("1. Booking Record")
    print("2. Restaurant Area")
    print("3. Gaming Zone")
    print("4. Calculate Total Bill")
    print("5. Exit")


def booking_record(customer):
    print("\n--- Booking Record ---")
    print("1. Ultra Royal - $ 5000")
    print("2. Royal - $3500")
    print("3. Elite - $2500")
    print("4. Common - $1500")
    print("5. Go to Main Menu")
    choice = int(input("Enter your choice: "))
    prices = [5000, 3500, 2500, 1500]
    if 0 <= choice < len(prices):
        customer[3] = customer[3]+prices[choice-1]
        print("Item added to your bill.")
    else:
        print()


def restaurant_area(customer):
    print("\n--- Restaurant Area ---")
    print("1. Pizza - $10")
    print("2. Burger - $7")
    print("3. Salad - $5")
    print("4. Go to Main Menu")
    choice = int(input("Enter your choice: "))
    prices = [10, 7, 5]
    if 0 <= choice < len(prices):
        customer[3] = customer[3]+prices[choice-1]
        print("Item added to your bill.")
    else:
        print()


def gaming_zone(customer):
    print("\n--- Gaming Zone ---")
    print("1. Carrom - $5")
    print("2. Chess - $3")
    print("3. Table Tennis - $8")
    print("4. Go to Main Menu")
    choice = int(input("Enter your choice: "))
    prices = [5, 3, 8]
    if 0 <= choice < len(prices):
        customer[3] = customer[3]+prices[choice-1]
        print("Game added to your bill.")
    else:
        print()


def calculate_total_bill(customer):
    print("\n--- Total Bill ---")
    print(f"Customer Name: {customer[0]}")
    print(f"Total Bill: ${customer[3]}")


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

    else:
        if current_customer == None:
            clearConsole()
            print("Welcome,", logged_in_admin)
            print("1. Add a New Customer")
            print("2. Add a Admin ")
            print("3. Logout")
            print("4. Exit")
            option = input("Enter your choice: ")
            match option:
                case '1':
                    current_customer = collect_customer_details()
                case '2':
                    register_admin()
                case '3':
                    logout_admin()
                case '4':
                    os._exit(1)
                case _:
                    print("Invalid choice! Please try again.")
        else:
            handle_customer(current_customer)
