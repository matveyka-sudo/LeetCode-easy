SELECT
    user_id,
    SUM(total) AS total_spent
FROM orders
WHERE status = 'paid'
GROUP BY user_id
HAVING SUM(total) > 3000;