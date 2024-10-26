SELECT 
    user_id, 
    upper(
        left(name, 1)
        ) 
        + 
        lower(
        right(name, len(name)-1)
        ) as name 
FROM Users
ORDER BY user_id;