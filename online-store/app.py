# Main Menu Code + Python to SQL implementation 
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
    new_customer_id = None

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

        new_customer_id = cursor.lastrowid

        print("\nCustomer added successfully.")
        print(f"Customer ID: {new_customer_id}")

    except Exception as error:
        connection.rollback()
        print(f"Could not add customer: {error}")

    finally:
        cursor.close()
        connection.close()

    if new_customer_id is not None:
        choice = input(
            "Would you like to add a credit card for this customer? (y/n): "
        ).strip().lower()

        if choice == "y":
            add_credit_card(new_customer_id)

        elif choice != "n":
            print("Invalid choice. Credit card was not added.")

def add_credit_card(customer_id):
    card_num = input("Enter card number: ").strip()
    security_code = input("Enter security code: ").strip()
    exp_date = input("Enter expiration date (YYYY-MM-DD): ").strip()

    if not card_num or not security_code or not exp_date:
        print("All credit card fields are required.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO CreditCard (
                CardNum,
                CustomerID,
                SecurityCode,
                ExpDate
            )
            VALUES (%s, %s, %s, %s)
            """,
            (
                card_num,
                customer_id,
                security_code,
                exp_date
            )
        )

        connection.commit()
        print("Credit card added successfully.")

    except Exception as error:
        connection.rollback()
        print(f"Could not add credit card: {error}")

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

def view_staff():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT StaffID, Name, Position
            FROM Staff
            ORDER BY StaffID
        """)

        staff_members = cursor.fetchall()

        if not staff_members:
            print("\nNo staff members found.")
            return

        print("\nStaff")
        print("-" * 60)
        print(f"{'ID':<8}{'Name':<25}{'Position':<25}")
        print("-" * 60)

        for staff_id, name, position in staff_members:
            print(
                f"{staff_id:<8}"
                f"{name:<25}"
                f"{position:<25}"
            )

    except Exception as error:
        print(f"Could not retrieve staff: {error}")

    finally:
        cursor.close()
        connection.close()

def view_updates():
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT
                Updates.UID,
                Staff.Name,
                Staff.Position,
                Product.Name,
                Updates.UpdateDate
            FROM Updates
            JOIN Staff
                ON Updates.StaffID = Staff.StaffID
            JOIN Product
                ON Updates.ProductID = Product.ProductID
            ORDER BY Updates.UpdateDate, Updates.UID
        """)

        updates = cursor.fetchall()

        if not updates:
            print("\nNo product updates found.")
            return

        print("\nProduct Update History")
        print("-" * 100)
        print(
            f"{'UID':<8}"
            f"{'Staff':<25}"
            f"{'Position':<25}"
            f"{'Product':<25}"
            f"{'Date':<12}"
        )
        print("-" * 100)

        for uid, staff_name, position, product_name, update_date in updates:
            print(
                f"{uid:<8}"
                f"{staff_name:<25}"
                f"{position:<25}"
                f"{product_name:<25}"
                f"{str(update_date):<12}"
            )

    except Exception as error:
        print(f"Could not retrieve product updates: {error}")

    finally:
        cursor.close()
        connection.close()

def record_product_update():
    try:
        staff_id = int(input("Enter staff ID: "))
        product_id = int(input("Enter product ID: "))
        new_stock_quantity = int(input("Enter new stock quantity: "))
    except ValueError:
        print("Staff ID, product ID, and stock must be whole numbers.")
        return

    if new_stock_quantity < 0:
        print("Stock quantity cannot be negative.")
        return

    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT StaffID
            FROM Staff
            WHERE StaffID = %s
            """,
            (staff_id,)
        )

        if cursor.fetchone() is None:
            print("Staff member not found.")
            return

        cursor.execute(
            """
            SELECT ProductID, Name, StockQuantity
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

        _, product_name, old_stock_quantity = product

        cursor.execute(
            """
            UPDATE Product
            SET StockQuantity = %s
            WHERE ProductID = %s
            """,
            (new_stock_quantity, product_id)
        )

        cursor.execute(
            """
            INSERT INTO Updates (
                ProductID,
                StaffID,
                UpdateDate
            )
            VALUES (%s, %s, %s)
            """,
            (
                product_id,
                staff_id,
                date.today()
            )
        )

        connection.commit()

        print("\nProduct updated successfully.")
        print(f"Product: {product_name}")
        print(f"Old stock: {old_stock_quantity}")
        print(f"New stock: {new_stock_quantity}")

    except Exception as error:
        connection.rollback()
        print(f"Could not update product: {error}")

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
    print("7. View staff")
    print("8. View product updates")
    print("9. Record product update")
    print("10. Exit")


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
            view_staff()

        elif choice == "8":
            view_updates()

        elif choice == "9":
            record_product_update()

        elif choice == "10":
            print("Goodbye! Thank you for visiting.")
            break

        else:
            print("Invalid option. Enter a number from 1 through 10.")


if __name__ == "__main__":
    main()