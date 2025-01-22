CREATE TABLE sales_data (
    month VARCHAR(50),
    sales INTEGER
);

INSERT INTO sales_data (month, sales) VALUES 
('January', 30),
('February', 40),
('March', 55),
('April', 70),
('May', 60);

SELECT * FROM sales_data;