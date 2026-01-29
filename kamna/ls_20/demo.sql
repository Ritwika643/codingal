CREATE TABLE PRODUCTS (
    PRODUCT_ID INT PRIMARY KEY,
    PRODUCT_NAME VARCHAR(100),
    CATEGORY VARCHAR(100),
    PRICE DECIMAL(10,2)
);

INSERT INTO PRODUCTS (PRODUCT_ID, PRODUCT_NAME, CATEGORY, PRICE) VALUES
(1, 'Laptop', 'Electronics', 1200.00),
(2, 'Smartphone', 'Electronics', 800.00),
(3, 'Desk Chair', 'Furniture', 150.00),
(4, 'Notebook', 'Stationery', 5.00),
(5, 'Pen', 'Stationery', 2.00);

SELECT COUNT(*) AS Total_Products 
FROM PRODUCTS;

SELECT AVG(PRICE) AS Average_Price
FROM PRODUCTS;

SELECT SUM(PRICE) AS Total_Price
FROM PRODUCTS;