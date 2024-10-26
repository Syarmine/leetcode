/* Write your T-SQL query statement below */
--table name is Product
SELECT 
    product_id
FROM Products
WHERE 
    low_fats = 'Y' AND
    recyclable = 'Y'