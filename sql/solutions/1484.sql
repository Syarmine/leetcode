/* Write your T-SQL query statement below */
SELECT 
    sell_date, 
    COUNT(product) num_sold, 
    STRING_AGG(product, ',') products
FROM (
    SELECT DISTINCT * 
    FROM activities) c 
GROUP BY sell_date