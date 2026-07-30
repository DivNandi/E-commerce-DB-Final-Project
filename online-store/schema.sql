-- Schema Creation Statements 

DROP DATABASE IF EXISTS online_store;

CREATE DATABASE online_store;

USE online_store;

CREATE TABLE Customer (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    StreetAddress VARCHAR(150) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State CHAR(2) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL
);

CREATE TABLE CreditCard (
    CardNum VARCHAR(19) PRIMARY KEY,
    CustomerID INT NOT NULL,
    SecurityCode VARCHAR(4) NOT NULL,
    ExpDate DATE NOT NULL,

    CONSTRAINT fk_creditcard_customer
        FOREIGN KEY (CustomerID)
        REFERENCES Customer(CustomerID)
        ON DELETE CASCADE
);

CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    StockQuantity INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,

    CONSTRAINT chk_product_stock
        CHECK (StockQuantity >= 0),

    CONSTRAINT chk_product_price
        CHECK (Price >= 0)
);

CREATE TABLE Staff (
    StaffID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(100) NOT NULL
);

CREATE TABLE Purchase (
    OrderNumber INT NOT NULL,
    ProductID INT NOT NULL,
    CustomerID INT NOT NULL,
    PurchaseDate DATE NOT NULL,
    QuantityPurchased INT NOT NULL,

    PRIMARY KEY (OrderNumber, ProductID),

    CONSTRAINT fk_purchase_product
        FOREIGN KEY (ProductID)
        REFERENCES Product(ProductID),

    CONSTRAINT fk_purchase_customer
        FOREIGN KEY (CustomerID)
        REFERENCES Customer(CustomerID),

    CONSTRAINT chk_purchase_quantity
        CHECK (QuantityPurchased > 0)
);

CREATE TABLE Updates (
    UID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT NOT NULL,
    StaffID INT NOT NULL,
    UpdateDate DATE NOT NULL,

    CONSTRAINT fk_updates_product
        FOREIGN KEY (ProductID)
        REFERENCES Product(ProductID),

    CONSTRAINT fk_updates_staff
        FOREIGN KEY (StaffID)
        REFERENCES Staff(StaffID)
);
