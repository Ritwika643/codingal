-- create two salesman and order tables
CREATE TABLE salesman (
    salesman_id INT PRIMARY KEY,
    Name VARCHAR(100),
    City VARCHAR(100),
    Commission DECIMAL(10,2)
);
INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(1, 'John Doe', 'New York', 0.10),
(2, 'Jane Smith', 'Los Angeles', 0.15),
(3, 'Jim Brown', 'Chicago', 0.12),
(4, 'Jake White', 'Miami', 0.11),
(5, 'Jill Black', 'Seattle', 0.14);
SELECT * FROM salesman;
--Salesman and orders table
CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    Name VARCHAR(20),
    City VARCHAR(20),
    Commissin DECIMAL(10,2)--Real
);
INSERT INTO orders (order_id, name, city, commissin) VALUES
(101, 'John Doe', 'New York', 0.10),
(102, 'Jane Smith', 'Los Angeles', 0.15),
(103, 'Jim Brown', 'Chicago', 0.12),
(104, 'Jake White', 'Miami', 0.11),
(105, 'Jill Black', 'Seattle', 0.14);
SELECT * FROM orders;

CREATE TABLE IF NOT EXISTS Orders(
Ord_no INT PRIMARY KEY,
Purch_amt DECIMAL(10,2),
Ord_date DATE,
Customer_id INT,
Salesman_id INT,
)
INSERT INTO Orders VALUES 
(70001, 150.5, '2023-06-15', 3001, 5001),
(70002, 250.75, '2023-06-16', 3002, 5002),
(70003, 350.0, '2023-06-17', 3003, 5003),
(70004, 450.25, '2023-06-18', 3004, 5004),
(70005, 550.5, '2023-06-19', 3005, 5005);
SELECT * FROM Orders;