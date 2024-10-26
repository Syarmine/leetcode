/* Write your T-SQL query statement below */
SELECT 
    project_id, 
    round(avg(experience_years*1.0),2) as average_years 
FROM project p 
INNER JOIN employee e 
    ON p.employee_id = e.employee_id 
GROUP BY project_id;