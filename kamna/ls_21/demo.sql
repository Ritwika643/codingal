--Activity - 1
CREATE TABLE IF NOT EXISTS NOBEL_WIN (
    YEAR INTEGER,
    SUBJECT TEXT,
    WINNER TEXT,
    COUNTRY TEXT,
    CATEGORY TEXT
); 
INSERT INTO NOBEL_WIN (YEAR, SUBJECT, WINNER, COUNTRY, CATEGORY) VALUES 
(1901, 'Physics', 'Wilhelm Conrad Röntgen', 'Germany', 'Nobel Prize in Physics'), 
(1901, 'Chemistry', 'Jacobus Henricus van Hoff', 'Netherlands', 'Nobel Prize in Chemistry'),
(1901, 'Medicine', 'Emil Adolf von Behring', 'Germany', 'Nobel Prize in Medicine'),
(1901, 'Literature', 'Sully Prudhomme', 'France', 'Nobel Prize in Literature'), 
(1901, 'Peace', 'Henry Dunant', 'Switzerland', 'Nobel Peace Prize'), 
(1901, 'Peace', 'Frédéric Passy', 'France', 'Nobel Peace Prize'), 
(1902, 'Physics', 'Hendrik Antoon Lorentz', 'Netherlands', 'Nobel Prize in Physics'),
(1902, 'Physics', 'Pieter Zeeman', 'Netherlands', 'Nobel Prize in Physics'), 
(1902, 'Chemistry', 'Emil Fischer', 'Germany', 'Nobel Prize in Chemistry'), 
(1902, 'Medicine', 'Sir Ronald Ross', 'United Kingdom', 'Nobel Prize in Medicine');

SELECT *
FROM NOBEL_WIN
WHERE SUBJECT NOT LIKE 'P%'; 

--Activity - 2
CREATE TABLE IF NOT EXISTS DEPARTMENT (
    EMPLOYEE_ID TEXT,
    NAME TEXT, 
    DEPARTMENT_ID TEXT,
    MANAGER_ID TEXT
    SALARY REAL
); 
INSERT INTO DEPARTMENT (EMPLOYEE_ID , NAME, DEPARTMENT, MANAGER_ID, SALARY) VALUES 
('E001', 'Alice', 'HR', 'M001', 50000), 
('E002', 'Bob', 'IT', 'M002', 60000),
('E003', 'Charlie', 'Finance', 'M001', 55000), 
('E004', 'David', 'IT', 'M002', 62000), 
('E005', 'Eve', 'HR', 'M001', 52000), 
('E006', 'Frank', 'Finance', 'M001', 58000), 
('E007', 'Grace', 'IT', 'M002', 61000),
('E008', 'Heidi', 'HR', 'M001', 53000);

SELECT DEPARTMENT_ID AS "DEPARTMENT CODE",
COUNT(*) AS NO.OF EMPLOYEES 
FROM DEPARTMENT 
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID, SUM(SALARY) 
FROM DEPARTMENT 
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID AS "DEPARTMENT CODE",
COUNT(*) AS NO.OF EMPLOYEES 
SUM(SALARY) AS "TOTAL SALARY"
FROM DEPARTMENT 
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID AS "DEPARTMENT CODE",
SUM(SALARY) AS "TOTAL SALARY"
FROM DEPARTMENT 
WHHERE MANAGER_ID = 'E005'
GROUP BY DEPARTMENT_ID;

SELECT DEPARTMENT_ID AS "DEPARTMENT CODE",
COUNT(*) AS NO.OF EMPLOYEES 
FROM DEPARTMENT 
GROUP BY DEPARTMENT_ID
HAVING COUNT(*) > 2;