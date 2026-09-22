SELECT
    id,
    user_id,
    total,
    LAG(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at
    ) AS previous_total,
    total - LAG(total) OVER (
        PARTITION BY user_id
        ORDER BY created_at
    ) AS difference
FROM orders;