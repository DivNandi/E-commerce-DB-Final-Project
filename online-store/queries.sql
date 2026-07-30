-- Query 1
SELECT * FROM Product;

-- Query 2
SELECT Name, Price
FROM Product
WHERE Price > 50;

-- Query 3 (Multi-table join)
SELECT
    Customer.Name,
    Product.Name,
    OrderItem.Quantity
FROM Customer
JOIN Orders
    ON Customer.CustomerID = Orders.CustomerID
JOIN OrderItem
    ON Orders.OrderID = OrderItem.OrderID
JOIN Product
    ON Product.ProductID = OrderItem.ProductID;