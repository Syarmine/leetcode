/* Write your T-SQL query statement below */
SELECT 
    activity_date AS DAY , 
    COUNT(DISTINCT user_id) AS active_users 
FROM ACTIVITY 
WHERE activity_date <= '2019-07-27' AND DATEDIFF(DAY , activity_date , '2019-07-27')<30
GROUP BY activity_date;