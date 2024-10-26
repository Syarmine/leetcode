/* Write your T-SQL query statement below */
WITH CTE AS(
    SELECT  *, 
            ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS RowNum
    FROM Person
)
DELETE 
FROM CTE 
WHERE RowNum > 1;