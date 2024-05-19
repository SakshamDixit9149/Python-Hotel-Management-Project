import os
admins = [["Saksham", "123"]]
customers = []
logged_in_admin = None
current_customer = None


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
    print("\n--- Main Menu ---")
    print("1. Booking Record")
    print("2. Restaurant Area")
    print("3. Gaming Zone")
    print("4. Calculate Total Bill")
    print("5. Exit")


def booking_record(customer):
    print("\n--- Booking Rewcord ---")
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
        if choice == '1':
            booking_record(customer)
        elif choice == '2':
            restaurant_area(customer)
        elif choice == '3':
            gaming_zone(customer)
        elif choice == '4':
            calculate_total_bill(customer)
        elif choice == '5':
            print("Exiting customer area...")
            global current_customer
            current_customer = None
            break
        else:
            print("Invalid choice! Please try again.")


while True:
    if not logged_in_admin:
        print("\n--- Welcome to Hotel Management System ---")
        print("1. Admin Login")
        print("2. Admin Register")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            login_admin()
        elif option == '2':
            register_admin()
            handle_customer()
        elif option == '3':
            print("Exiting the system...")
            os.exit()
        else:
            print("Invalid choice! Please try again.")

    else:
        if current_customer == None:
            print("1. Add a New Customer")
            print("2. Logout")
            print("3. Exit")
            option = input("Enter your choice: ")
            if option == '1':
                current_customer = collect_customer_details()
            elif option == '2':
                logged_in_admin = None
            else:
                os.exit()
        else:
            handle_customer(current_customer)
