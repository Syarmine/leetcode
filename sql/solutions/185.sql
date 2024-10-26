WITH employee_department as
(
    SELECT 
    d.name AS Department,
    e.salary AS Salary,
    e.name as Employee,
    DENSE_RANK() OVER (PARTITION BY d.id ORDER BY salary DESC) AS rank
    FROM Department d
    JOIN Employee E
        ON d.id = e.departmentID
)

SELECT 
    Department,
    Employee,
    Salary
FROM employee_department
WHERE rank <= 3