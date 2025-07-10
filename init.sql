CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Email VARCHAR(150),
    PhoneNumber VARCHAR(20),
    SignupDate DATE,
    CustomerType VARCHAR(50)
);

CREATE TABLE Address (
    AddressID SERIAL PRIMARY KEY,
    CustomerID INT,
    Street TEXT,
    City VARCHAR(100),
    Postcode VARCHAR(20),
    Country VARCHAR(100),
    AddressType VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE Category (
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(100)
);

CREATE TABLE Product (
    StockCode VARCHAR(20) PRIMARY KEY,
    Description TEXT,
    Price NUMERIC(10, 2),
    Weight NUMERIC(8, 2),
    Color VARCHAR(50),
    Brand VARCHAR(100),
    DateAdded DATE,
    IsDiscontinued BOOLEAN,
    CategoryID INT,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
);

CREATE TABLE DiscountCode (
    Code VARCHAR(20) PRIMARY KEY,
    Description TEXT,
    DiscountPercent NUMERIC(5,2),
    ValidFrom DATE,
    ValidTo DATE
);

CREATE TABLE Invoice (
    InvoiceID VARCHAR(20) PRIMARY KEY,
    CustomerID INT,
    InvoiceDate TIMESTAMP,
    ShippingCost NUMERIC(8, 2),
    ShippingMethod VARCHAR(100),
    PaymentMethod VARCHAR(100),
    IsGift BOOLEAN,
    DiscountCode VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (DiscountCode) REFERENCES DiscountCode(Code)
);

CREATE TABLE InvoiceLineItem (
    InvoiceLineID SERIAL PRIMARY KEY,
    InvoiceID VARCHAR(20),
    StockCode VARCHAR(20),
    Quantity INT,
    FOREIGN KEY (InvoiceID) REFERENCES Invoice(InvoiceID),
    FOREIGN KEY (StockCode) REFERENCES Product(StockCode)
);

CREATE TABLE Payment (
    PaymentID SERIAL PRIMARY KEY,
    InvoiceID VARCHAR(20),
    PaymentStatus VARCHAR(50),
    PaymentDate DATE,
    Amount NUMERIC(10, 2),
    FOREIGN KEY (InvoiceID) REFERENCES Invoice(InvoiceID)
);