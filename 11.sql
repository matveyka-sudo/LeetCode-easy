WITH expensive_orders AS (
    SELECT user_id
    FROM orders
    WHERE total > 2000
)

SELECT
    id,
    username
FROM users
WHERE id IN (
    SELECT user_id
    FROM expensive_orders
);