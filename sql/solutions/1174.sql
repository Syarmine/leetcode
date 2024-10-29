/* Write your T-SQL query statement below */
WITH CTE AS (
    SELECT 
        DISTINCT customer_id, 
        MIN(order_date) as order_date, 
        MIN(customer_pref_delivery_date) as             customer_pref_delivery_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT
round(sum(iif(order_date=customer_pref_delivery_date, 100.0, 0)) / count(order_date), 2)
as immediate_percentage
FROM CTE