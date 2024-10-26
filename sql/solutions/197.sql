SELECT 
w2.id
FROM Weather w1
CROSS JOIN Weather w2
WHERE DATEDIFF(DAY, w1.recordDate, w2.recordDate) = 1 AND 
    w2.temperature > w1.temperature