/* Write your T-SQL query statement below */
SELECT 
    e1.employee_id,
    e1.name,
    COUNT(e2.reports_to) reports_count,
    ROUND(AVG(e2.age*1.00),0) average_age
FROM employees e1 
INNER JOIN employees e2 ON e2.reports_to=e1.employee_id
GROUP BY e1.employee_id,e1.name
ORDER BY e1.employee_id