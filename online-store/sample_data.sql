-- Data Insertion Statements

USE online_store;

INSERT INTO Customer (
    FirstName,
    LastName,
    Email,
    StreetAddress,
    City,
    State,
    ZipCode
)
VALUES
    (
        'Alice',
        'Johnson',
        'alice@example.com',
        '100 Main Street',
        'Coolplace',
        'NY',
        '22222'
    ),
    (
        'Bob',
        'Smith',
        'bob@example.com',
        '250 Oak Avenue',
        'Newdog',
        'KY',
        '33333'
    ),
    (
        'Carla',
        'Davis',
        'carla@example.com',
        '425 street street',
        'Cincinnati',
        'OH',
        '45202'
    );

INSERT INTO CreditCard (
    CardNum,
    CustomerID,
    SecurityCode,
    ExpDate
)
VALUES
    ('TEST-1111', 1, '111', '2028-12-01'),
    ('TEST-2222', 2, '222', '2029-06-01'),
    ('TEST-3333', 3, '333', '2028-09-01');

INSERT INTO Product (
    Name,
    StockQuantity,
    Price
)
VALUES
    ('Wireless Mouse', 20, 29.99),
    ('Mechanical Keyboard', 10, 89.99),
    ('Computer Monitor', 5, 249.99),
    ('Secret Cool Awesome Product', 1, 500.00),
    ('Expensive Apple', 30, 14.99);

INSERT INTO Staff (
    Name,
    Position
)
VALUES
    ('Bob Evans', 'Inventory Manager'),
    ('Olivia Garden', 'Store Associate');

INSERT INTO Purchase (
    OrderNumber,
    ProductID,
    CustomerID,
    PurchaseDate,
    QuantityPurchased
)
VALUES
    (1001, 1, 1, '2026-07-20', 2),
    (1001, 4, 1, '2026-07-20', 1),
    (1002, 3, 2, '2026-07-21', 1);

INSERT INTO Updates (
    ProductID,
    StaffID,
    UpdateDate
)
VALUES
    (1, 1, '2026-07-18'),
    (3, 2, '2026-07-19');