# Main Menu Code

from decimal import Decimal, InvalidOperation

from database import get_connection


def view_products():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT ProductID, Name, StockQuantity, Price
            FROM Product
            ORDER BY ProductID
        """)

        products = cursor.fetchall()

        if not products:
            print("\nNo products found.")
            return

        print("\nProducts")
        print("-" * 65)
        print(f"{'ID':<5}{'Name':<30}{'Stock':<12}{'Price':<12}")
        print("-" * 65)

        for product_id, name, stock_quantity, price in products:
            print(
                f"{product_id:<5}"
                f"{name:<30}"
                f"{stock_quantity:<12}"
                f"${price:<11.2f}"
            )

    except Exception as error:
        print(f"Could not retrieve products: {error}")

    finally:
        cursor.close()
        connection.close()


def add_product():
    name = input("Enter product name: ").strip()

    try:
        stock_quantity = int(input("Enter stock quantity: "))
        price = Decimal(input("Enter product price: $"))
    except (ValueError, InvalidOperation):
        print("Stock must be a whole number and price must be numeric.")
        return

    if not name:
        print("Product name cannot be empty.")
        return

    if stock_quantity < 0:
        print("Stock quantity cannot be negative.")
        return

    if price < 0:
        print("Price cannot be negative.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO Product (
                Name,
                StockQuantity,
                Price
            )
            VALUES (%s, %s, %s)
            """,
            (name, stock_quantity, price)
        )

        connection.commit()
        print("\nProduct added successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Could not add product: {error}")

    finally:
        cursor.close()
        connection.close()


def view_customers():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                CustomerID,
                FirstName,
                LastName,
                Email,
                StreetAddress,
                City,
                State,
                ZipCode
            FROM Customer
            ORDER BY CustomerID
        """)

        customers = cursor.fetchall()

        if not customers:
            print("\nNo customers found.")
            return

        print("\nCustomers")
        print("-" * 100)

        for customer in customers:
            (
                customer_id,
                first_name,
                last_name,
                email,
                street_address,
                city,
                state,
                zip_code
            ) = customer

            print(f"Customer ID: {customer_id}")
            print(f"Name: {first_name} {last_name}")
            print(f"Email: {email}")
            print(f"Address: {street_address}, {city}, {state} {zip_code}")
            print("-" * 100)

    except Exception as error:
        print(f"Could not retrieve customers: {error}")

    finally:
        cursor.close()
        connection.close()


def add_customer():
    first_name = input("Enter first name: ").strip()
    last_name = input("Enter last name: ").strip()
    email = input("Enter email: ").strip()
    street_address = input("Enter street address: ").strip()
    city = input("Enter city: ").strip()
    state = input("Enter two-letter state abbreviation: ").strip().upper()
    zip_code = input("Enter ZIP code: ").strip()

    customer_values = [
        first_name,
        last_name,
        email,
        street_address,
        city,
        state,
        zip_code
    ]

    if any(not value for value in customer_values):
        print("Every customer field is required.")
        return

    if len(state) != 2:
        print("State must be a two-letter abbreviation.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO Customer (
                FirstName,
                LastName,
                Email,
                StreetAddress,
                City,
                State,
                ZipCode
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                first_name,
                last_name,
                email,
                street_address,
                city,
                state,
                zip_code
            )
        )

        connection.commit()
        print("\nCustomer added successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Could not add customer: {error}")

    finally:
        cursor.close()
        connection.close()


def display_menu():
    print("\n==========================")
    print("    Mini Online Store")
    print("==========================")
    print("1. View products")
    print("2. Add product")
    print("3. View customers")
    print("4. Add customer")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            view_customers()

        elif choice == "4":
            add_customer()

        elif choice == "5":
            print("Goodbye! Thank you for visiting.")
            break

        else:
            print("Invalid option. Enter a number from 1 through 5.")


if __name__ == "__main__":
    main()