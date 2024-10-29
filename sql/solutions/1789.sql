/* Write your T-SQL query statement below */
SELECT employee_id, department_id
FROM Employee
WHERE primary_flag = 'Y'

UNION

SELECT employee_id, MAX(department_id)
FROM Employee
GROUP BY employee_id
HAVING COUNT(employee_id) = 1;