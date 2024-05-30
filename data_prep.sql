
\c postgres

SELECT 'CREATE DATABASE dci_db'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'dci_db')\gexec

\c dci_db

CREATE TABLE IF NOT EXISTS Warehouse(
        Warehouse_Id SERIAL NOT NULL PRIMARY KEY,
        Warehouse_Name VARCHAR(100) NOT NULL,
        Employee_Count SERIAL
);

INSERT INTO Warehouse (Warehouse_Id, Warehouse_Name, Employee_Count)
VALUES
('1', 'Amazon Warehouse', 1000),
('2', 'Rewe Warehouse', 400),
('3', 'Tedi Warehouse', 200),
('4', 'Bahn Warehouse', 1500);

CREATE TABLE IF NOT EXISTS Employee(
        Employee_Id serial NOT NULL PRIMARY KEY,
        Employee_Name VARCHAR (100) NOT NULL,
        Warehouse_Id serial NOT NULL,
        Joining_Date DATE NOT NULL,
        Speciality VARCHAR (100) NOT NULL,
        Salary INTEGER NOT NULL,
        Experience SMALLINT
);


INSERT INTO Employee (Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience)
VALUES
('101', 'Mo', '1', '2005-2-10', 'HR Manager', '40000', NULL),
('102', 'Michael', '1', '2018-07-23', 'Driver', '30000', NULL),
('103', 'Lukaku', '2', '2016-05-19', 'Conveyor', '25000', NULL),
('104', 'Robert', '2', '2017-12-28', 'Logistics Spcialist', '28000', NULL),
('105', 'Linda', '3', '2004-06-04', 'Logistics Spcialist', '42000', NULL),
('106', 'Kahn', '3', '2012-09-11', 'Manager', '30000', NULL),
('107', 'Bernice', '4', '2014-08-21', 'Medic', '32000', NULL),
('108', 'Karen', '4', '2011-10-17', 'Driver', '30000', NULL);