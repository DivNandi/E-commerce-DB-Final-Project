INSERT INTO Customer (Name, Email)
VALUES
    ('Alice Johnson', 'alice@example.com'),
    ('Bob Smith', 'bob@example.com'),
    ('Carla Davis', 'carla@example.com');

INSERT INTO Product (Name, Price, Stock)
VALUES
    ('Wireless Mouse', 29.99, 20),
    ('Mechanical Keyboard', 89.99, 10),
    ('Computer Monitor', 249.99, 5),
    ('USB-C Cable', 14.99, 30);

INSERT INTO Orders (CustomerID, OrderDate)
VALUES
    (1, '2026-07-20'),
    (2, '2026-07-21');

INSERT INTO OrderItem (OrderID, ProductID, Quantity)
VALUES
    (1, 1, 2),
    (1, 4, 1),
    (2, 3, 1);
    
SELECT * FROM Customer;
SELECT * FROM Product;
SELECT * FROM Orders;
SELECT * FROM OrderItem;
