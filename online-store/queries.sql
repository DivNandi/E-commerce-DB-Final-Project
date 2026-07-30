USE online_store;

-- Query 1:
-- Show all products currently in stock.
SELECT
    ProductID,
    Name,
    StockQuantity,
    Price
FROM Product
WHERE StockQuantity > 0
ORDER BY Name;


-- Query 2:
-- Show customers and their credit-card expiration dates.
SELECT
    Customer.FirstName,
    Customer.LastName,
    CreditCard.CardNum,
    CreditCard.ExpDate
FROM Customer
JOIN CreditCard
    ON Customer.CustomerID = CreditCard.CustomerID
ORDER BY Customer.LastName;


-- Query 3:
-- Show purchase history with customers and products.
SELECT
    Purchase.OrderNumber,
    Customer.FirstName,
    Customer.LastName,
    Product.Name AS ProductName,
    Purchase.QuantityPurchased,
    Product.Price,
    Purchase.QuantityPurchased * Product.Price AS LineTotal,
    Purchase.PurchaseDate
FROM Purchase
JOIN Customer
    ON Purchase.CustomerID = Customer.CustomerID
JOIN Product
    ON Purchase.ProductID = Product.ProductID
ORDER BY Purchase.OrderNumber;


-- Additional query:
-- Show which staff members updated which products.
SELECT
    Updates.UID,
    Staff.Name AS StaffName,
    Staff.Position,
    Product.Name AS ProductName,
    Updates.UpdateDate
FROM Updates
JOIN Staff
    ON Updates.StaffID = Staff.StaffID
JOIN Product
    ON Updates.ProductID = Product.ProductID
ORDER BY Updates.UpdateDate;