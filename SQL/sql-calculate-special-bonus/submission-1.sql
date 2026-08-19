-- Write your query below
SELECT EMPLOYEE_ID,
    CASE
        WHEN EMPLOYEE_ID % 2 = 1 and name NOT LIKE 'M%'
            THEN Salary
        ELSE 0
    END AS bonus
FROM employees
ORDER BY employee_id
;