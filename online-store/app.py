from database import get_connection


def view_products():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT ProductID, Name, Price, Stock
            FROM Product
            ORDER BY ProductID
        """)

        products = cursor.fetchall()

        if not products:
            print("\nNo products found.")
            return

        print("\nProducts")
        print("-" * 60)
        print(f"{'ID':<5}{'Name':<25}{'Price':<15}{'Stock':<10}")
        print("-" * 60)

        for product_id, name, price, stock in products:
            print(
                f"{product_id:<5}"
                f"{name:<25}"
                f"${price:<14.2f}"
                f"{stock:<10}"
            )

    except Exception as error:
        print(f"Could not retrieve products: {error}")

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    view_products()