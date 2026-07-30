# Main Menu Code
from decimal import Decimal, InvalidOperation
from database import get_connection
from datetime import date

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

def view_purchases():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                Purchase.OrderNumber,
                Customer.FirstName,
                Customer.LastName,
                Product.Name,
                Purchase.QuantityPurchased,
                Product.Price,
                Purchase.QuantityPurchased * Product.Price AS LineTotal,
                Purchase.PurchaseDate
            FROM Purchase
            JOIN Customer
                ON Purchase.CustomerID = Customer.CustomerID
            JOIN Product
                ON Purchase.ProductID = Product.ProductID
            ORDER BY Purchase.OrderNumber, Product.Name
        """)

        purchases = cursor.fetchall()

        if not purchases:
            print("\nNo purchases found.")
            return

        print("\nPurchase History")
        print("-" * 110)
        print(
            f"{'Order':<10}"
            f"{'Customer':<25}"
            f"{'Product':<25}"
            f"{'Qty':<8}"
            f"{'Price':<12}"
            f"{'Total':<12}"
            f"{'Date':<12}"
        )
        print("-" * 110)

        for (
            order_number,
            first_name,
            last_name,
            product_name,
            quantity,
            price,
            line_total,
            purchase_date
        ) in purchases:
            customer_name = f"{first_name} {last_name}"

            print(
                f"{order_number:<10}"
                f"{customer_name:<25}"
                f"{product_name:<25}"
                f"{quantity:<8}"
                f"${price:<11.2f}"
                f"${line_total:<11.2f}"
                f"{str(purchase_date):<12}"
            )

    except Exception as error:
        print(f"Could not retrieve purchases: {error}")

    finally:
        cursor.close()
        connection.close()

def record_purchase():
    try:
        order_number = int(input("Enter order number: "))
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity purchased: "))
    except ValueError:
        print("Order number, IDs, and quantity must be whole numbers.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT CustomerID
            FROM Customer
            WHERE CustomerID = %s
            """,
            (customer_id,)
        )

        if cursor.fetchone() is None:
            print("Customer not found.")
            return

        cursor.execute(
            """
            SELECT StockQuantity
            FROM Product
            WHERE ProductID = %s
            FOR UPDATE
            """,
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:
            print("Product not found.")
            return

        current_stock = product[0]

        if current_stock < quantity:
            print(
                f"Not enough inventory. "
                f"Only {current_stock} unit(s) are available."
            )
            return

        cursor.execute(
            """
            INSERT INTO Purchase (
                OrderNumber,
                ProductID,
                CustomerID,
                PurchaseDate,
                QuantityPurchased
            )
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                order_number,
                product_id,
                customer_id,
                date.today(),
                quantity
            )
        )

        cursor.execute(
            """
            UPDATE Product
            SET StockQuantity = StockQuantity - %s
            WHERE ProductID = %s
            """,
            (quantity, product_id)
        )

        connection.commit()
        print("Purchase recorded successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Could not record purchase: {error}")

    finally:
        cursor.close()
        connection.close()


def display_menu():
    print("\n======================================")
    print("    Div's Mini Online Store Viewer")
    print("======================================")
    print("1. View products")
    print("2. Add product")
    print("3. View customers")
    print("4. Add customer")
    print("5. View purchases")
    print("6. Record purchase")
    print("7. Exit")


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
            view_purchases()

        elif choice == "6":
            record_purchase()

        elif choice == "7":
            print("Goodbye! Thank you for visiting.")
            break
        else:
            print("Invalid option. Enter a number from 1 through 7.")


if __name__ == "__main__":
    main()