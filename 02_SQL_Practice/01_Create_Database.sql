
USE RetailDW;
GO

CREATE TABLE Customers
(
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender CHAR(1),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    City VARCHAR(50),
    State VARCHAR(50),
    CreatedDate DATE
);