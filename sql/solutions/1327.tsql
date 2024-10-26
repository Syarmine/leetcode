/* Write your T-SQL query statement below */

SELECT 
    product_name, 
    SUM(unit) unit
FROM products p
JOIN orders o 
    ON p.product_id = o.product_id
WHERE o.order_date LIKE '2020-02%'
GROUP BY product_name
HAVING SUM(unit) >= 100