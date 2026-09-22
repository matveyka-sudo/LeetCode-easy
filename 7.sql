SELECT
    id,
    user_id,
    total,
    DENSE_RANK() OVER (
        PARTITION BY user_id
        ORDER BY total DESC
    ) AS rank
FROM orders;