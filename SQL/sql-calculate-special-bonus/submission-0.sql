-- Write your query below
SELECT employee_id,
    CASE
        WHEN EMPLOYEE_ID % 2 = 1 AND name not like 'M%' 
            THEN salary
        ELSE 0
    END AS bonus
FROM EMPLOYEES
ORDER BY Employee_id
;