/* Write your T-SQL query statement below */
WITH cte AS
    (SELECT 
        *,
        SUM(weight)OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED 
        PRECEDING AND CURRENT ROW) w_sum
    FROM queue)
SELECT TOP 1 person_name 
FROM cte 
WHERE w_sum <= 1000 
ORDER BY turn DESC