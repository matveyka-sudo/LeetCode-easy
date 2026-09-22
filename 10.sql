WITH orders_static AS (
    SELECT
        user_id,
        COUNT(*) AS paid_orders_count,
        SUM(total) AS paid_total
    FROM orders
    WHERE status = 'paid'
    GROUP BY user_id
)

SELECT
    u.username,
    COALESCE(os.paid_orders_count, 0) AS paid_orders_count,
    COALESCE(os.paid_total, 0) AS paid_total
FROM users AS u
LEFT JOIN orders_static AS os
    ON u.id = os.user_id;