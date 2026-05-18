CREATE TABLE Customer (
  Customer_ID INT PRIMARY KEY,
  Customer_Name VARCHAR(50),
  customer_MO VARCHAR(10),
  City VARCHAR(30)
);

CREATE TABLE Branch (
  Branch_ID INT PRIMARY KEY,
  Branch_Name VARCHAR(50),
  Branch_City VARCHAR(50)
);
CREATE TABLE Account (
  Account_No INT PRIMARY KEY,
  Customer_ID INT,
  Account_Type VARCHAR(20),
  Balance DECIMAL(10,2),
  FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID)
);

CREATE TABLE Transaction_Table (
  Trans_ID INT PRIMARY KEY,
  Account_No INT,
  Trans_Type VARCHAR(10),
  Amount DECIMAL(10,2),
  Trans_Date DATE,
  FOREIGN KEY (Account_No) REFERENCES Account(Account_No)
);
