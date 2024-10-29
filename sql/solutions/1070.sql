/* Write your T-SQL query statement below */
WITH CTE AS (
SELECT 
    product_id as product_id,
    MIN(year) as first_year
FROM 
    Sales
GROUP BY product_id
)

SELECT 
    s.product_id, 
    CTE.first_year,
    s.quantity,
    s.price
FROM Sales S
JOIN 
    CTE ON s.product_id = CTE.product_id AND
            s.year = CTE.first_year
ORDER BY 
s.product_id, CTE.first_year