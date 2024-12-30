create database task;
use task;
CREATE TABLE Suppliers (
    SupplierID INT NOT NULL AUTO_INCREMENT,
    SupplierName VARCHAR(255) NOT NULL,
    PRIMARY KEY (SupplierID)
);
INSERT INTO Suppliers (SupplierName)
VALUES
('AMAZON'),
('NYKA'),
('AJIO'),
('BLINKIT'),
('COUNTRY DELIGHT'),
('MALABAR');
CREATE TABLE Categories (
    CategoryID INT NOT NULL AUTO_INCREMENT,
    CategoryName VARCHAR(50) NOT NULL,
    PRIMARY KEY (CategoryID)
);
INSERT INTO Categories (categoryName)
values
('home'),
('beautyproducts'),
('clothing'),
('groceries'),
('dairyproducts'),
('gold');
CREATE TABLE Products(
    ProductID INT NOT NULL AUTO_INCREMENT,
    ProductName VARCHAR(255) NOT NULL,
    SupplierID INT,
	CategoryID INT ,
    QuantityPerUnit int,
    UnitPrice INT,
    UnitsInStock INT,
    UnitsOnOrder INT,
    ReorderLevel INT,
    Discontinued BOOLEAN,
    PRIMARY KEY (ProductID),
    UNIQUE (ProductName),
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
INSERT INTO Products (ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock, UnitsOnOrder, ReorderLevel, Discontinued)
VALUES
    ('SPOONS', 1, 1, '40', 20, 100, 12, 3, 1),
    ('BOOKS', 1, 1, '12', 35, 60, 1, 5, 1),
    ('MILK', 5, 5, '2', 24, 60, 1, 1, 1), 
    ('LIPSTICK', 2, 2, '1', 30, 20, 1, 5, 1), 
    ('MAGGIE', 4, 4, '30', 5, 60, 1, 1, 0),
    ('EARRINGS', 6, 6, '2', 100, 2, 1, 0, 1),
    ('LIPBALM', 2, 2, '1', 10, 20, 1, 5, 1),
    ('SHIRT', 3, 3, '1', 100, 5, 1, 3, 1),
    ('SAREE', 3, 3, '1', 1000, 3, 1, 3, 1),
    ('GOODDAY BISCUIT', 1, 1, '4', 20, 5, 12, 3, 1),
    ('GHEE', 5, 5, '1', 50, 60, 1, 1, 1),
    ('BANGLES', 6, 6, '1', 5000, 1, 1, 0, 0);
select * from Products;
select * from suppliers;
select * from Categories;
select * from products order by ProductID asc;

-- task 2
-- 6 Write a MySQL query to get Product list (id, name, unit price) where products cost between $15 and 25 rupees.
SELECT ProductID,ProductName,UnitPrice from Products where UnitPrice between 15 and 25;

-- 7 Write a MySQL query to get Product list (name, unit price) of above average price.
select ProductName,UnitPrice from Products where UnitPrice>(select avg(UnitPrice) from Products);

-- 8 Write a MySQL query to get Product list (name, unit price) of ten most expensive products.
SELECT ProductName, UnitPrice from Products order by UnitPrice DESC limit 10;

-- 9 Write a MySQL query to count current and discontinued products.
SELECT Discontinued,COUNT(*) AS ProductCount FROM Products GROUP BY Discontinued;

-- 10 Write a MySQL query to get Product list (name, units on order , units in stock) of stock is less than the quantity on order.
SELECT ProductName, UnitsOnOrder, UnitsInStock FROM Products WHERE UnitsInStock < UnitsOnOrder;



select ProductName,QuantityPerUnit from Products;
SELECT ProductId,ProductName from Products where discontinued = 1;
SELECT ProductId,ProductName from Products where discontinued = 0;
(SELECT ProductName, unitprice FROM Products ORDER BY unitprice DESC LIMIT 1)
UNION
(SELECT ProductName, unitprice FROM Products ORDER BY unitprice ASC LIMIT 1);
SELECT ProductId,ProductName,unitprice FROM Products WHERE unitprice < 20;
