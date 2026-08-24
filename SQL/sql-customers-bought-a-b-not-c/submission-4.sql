-- Write your query below
SELECT c.customer_id, c.customer_name
FROM customers c
WHERE customer_id IN (SELECT customer_ID from ORDERS WHERE product_name = 'A')
AND customer_id IN (SELECT customer_ID from ORDERS WHERE product_name = 'B')
AND customer_id NOT IN (SELECT customer_ID from ORDERS WHERE product_name = 'C')
ORDER BY customer_name
;