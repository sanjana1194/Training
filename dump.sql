CREATE TABLE Cashier (
	CashierID VARCHAR(10) PRIMARY KEY,
	CashierName VARCHAR(100) NOT NULL
);

CREATE TABLE Supplier (
	SupplierID VARCHAR(10) PRIMARY KEY,
	SupplierName VARCHAR(100) NOT NULL
);

CREATE TABLE Customer (
	CustomerID VARCHAR(10) PRIMARY KEY,
	CustomerName VARCHAR(100) NOT NULL
);

CREATE TABLE Item (
	ItemID VARCHAR(10) PRIMARY KEY,
	Description VARCHAR(255) NOT NULL,
	UnitPrice DECIMAL(10,2) NOT NULL CHECK (UnitPrice > 0),
	StockQty INT DEFAULT 0,
	SupplierID VARCHAR(10),
	FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

CREATE TABLE BillHeader (
	BillNumber INT PRIMARY KEY AUTO_INCREMENT,
	BillDate DATE DEFAULT (CURRENT_DATE()),
	CashierID VARCHAR(10),
	CustomerID VARCHAR(10),
	FOREIGN KEY (CashierID) REFERENCES Cashier(CashierID),
	FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE BillDetail (
	BillNumber INT,
	ItemID VARCHAR(10),
	SoldQty INT DEFAULT 1,
	PRIMARY KEY (BillNumber, ItemID),
	FOREIGN KEY (BillNumber) REFERENCES BillHeader(BillNumber),
	FOREIGN KEY (ItemID) REFERENCES Item(ItemID)
);

INSERT INTO Cashier VALUES
('C001','Anjali'),('C002','Ravi'),('C003','Kiran'),('C004','Neha'),
('C005','Vijay'),('C006','Swathi'),('C007','Arjun'),('C008','Deepa'),
('C009','Rahul'),('C010','Priya');

INSERT INTO Supplier VALUES
('S001','Fresh Mart'),('S002','Tech Hub'),('S003','Home Needs Store'),
('S004','Daily Groceries'),('S005','Gadget Zone'),('S006','Fashion Corner'),
('S007','Kitchen World'),('S008','Green Farms'),('S009','Appliance Store'),
('S010','Quick Buy Supermarket');

INSERT INTO Customer VALUES
('CU001','Sanjana'),('CU002','Rahul'),('CU003','Priya'),('CU004','Karthik'),
('CU005','Divya'),('CU006','Teja'),('CU007','Amit'),('CU008','Meena'),
('CU009','Nikhil'),('CU010','Sneha');

INSERT INTO Item VALUES
('I001','Apples 1kg',120.00,50,'S001'),
('I002','Bananas 1 dozen',60.00,100,'S001'),
('I003','Laptop Mouse',450.00,30,'S002'),
('I004','Keyboard',750.00,25,'S002'),
('I005','Detergent 1kg',95.00,40,'S003'),
('I006','Shampoo 500ml',180.00,60,'S004'),
('I007','T-shirt',350.00,80,'S006'),
('I008','Cooking Oil 1L',160.00,45,'S004'),
('I009','Pressure Cooker',1200.00,20,'S007'),
('I010','Air Fryer',4500.00,10,'S009');

INSERT INTO BillHeader (BillNumber, BillDate, CashierID, CustomerID) VALUES
(1,'2025-11-01','C001','CU001'),
(2,'2025-11-02','C002','CU001'),
(3,'2025-11-03','C003','CU002'),
(4,'2025-11-03','C004','CU003'),
(5,'2025-11-04','C005','CU004'),
(6,'2025-11-04','C006','CU005'),
(7,'2025-11-05','C007','CU006'),
(8,'2025-11-05','C008','CU001'),
(9,'2025-11-06','C009','CU007'),
(10,'2025-11-07','C010','CU008');

INSERT INTO BillDetail VALUES
(1,'I001',2),(1,'I002',1),
(2,'I003',1),(2,'I004',1),(2,'I005',2),
(3,'I006',3),(3,'I007',1),
(4,'I008',1),(4,'I005',2),
(5,'I009',1),
(6,'I001',1),(6,'I010',1),
(7,'I002',3),(7,'I006',2),
(8,'I007',2),(8,'I008',1),
(9,'I004',1),(9,'I005',1),
(10,'I009',1),(10,'I010',1);

COMMIT;
